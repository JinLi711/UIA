from nltk.corpus import wordnet as wn
import pandas as pd

#======================================================================
# Create structures
#======================================================================


def create_word_structures(files, csv_dir):
    """
    Create the structures containing the words.
    Creates:
        dictionary mapping file name to words it contains
        set of all words

    :param files: list of files
    :type  files: list
    :param csv_dir: directory of the csv files
    :type  csv_dir: str
    :returns: (dictionary mapping file names to words,
               set of all words in all the files)
    :rtype:   (dict, set)

    """

    neighborhood_type_dict = {}
    for item in files:
        words = pd.read_csv(csv_dir + item)['WORDS'].values.tolist()
        words = [word.lower() for word in words]
        neighborhood_type_dict[item] = words

    all_words = set()
    for names, words in neighborhood_type_dict.items():
        all_words = all_words.union(set(words))

    return neighborhood_type_dict, all_words


#======================================================================
# Normalize Words
#======================================================================


def morphy_words(words):
    """
    Get the stem from the list words

    :param words: set of words
    :type  words: set
    :returns: set of words
    :rtype:   set
    """
    result = []

    from nltk.stem.snowball import SnowballStemmer
    stemmer = SnowballStemmer("english")

#     words = [stemmer.stem(word) for word in words]
    for word in words:
        morphed = wn.morphy(word)
        if morphed == None:
            result.append(word)
        else:
            result.append(morphed)
#         result.append(morphed)

    return result


def divide_words_by_pos(words):
    """
    Divide the words depending on their part of speech.

    :param words: set of words
    :type  words: set
    :returns: dictionary mapping pos to a list of synsets
    :rtype:   dict 
    """

    pos_synsets = {}

    # the only 4 part of speech in WordNet
    verbs = []
    nouns = []
    adj = []
    adv = []

    for word in words:
        verb_synsets = (wn.synsets(word, pos=wn.VERB))
        dup_verb = [word] * len(verb_synsets)
        verbs = verbs + list(zip(dup_verb, verb_synsets))

        noun_synsets = (wn.synsets(word, pos=wn.NOUN))
        dup_noun = [word] * len(noun_synsets)
        nouns = nouns + list(zip(dup_noun, noun_synsets))

        adj_synsets = (wn.synsets(word, pos=wn.ADJ))
        dup_adj = [word] * len(adj_synsets)
        adj = adj + list(zip(dup_adj, adj_synsets))

        adv_synsets = (wn.synsets(word, pos=wn.ADV))
        dup_adv = [word] * len(adv_synsets)
        adv = adv + list(zip(dup_adv, adv_synsets))

    pos_synsets['VERBS'] = sorted(verbs)
    pos_synsets['NOUNS'] = sorted(nouns)
    pos_synsets['ADJ'] = sorted(adj)
    pos_synsets['ADV'] = sorted(adv)

    return pos_synsets


def remove_terms(pos_synsets, remove_dict, issynset=False):
    """
    Remove synsets from the part of speech synset dictionary 
    based on the word.

    :param pos_synsets: dictionary mapping pos to list of 
                        bi-tuples, where first item is the word
                        and second item is the synset
    :type  pos_synsets: dict
    :param remove_dict: dictionary mapping pos to list of words to remove
    :type  remove_dict: dict
    :param issynset: is remove_dict refering to words or synsets
    :type  issynset: bool
    :returns: dictionary of pos_synsets after removal
    :rtype:   dict
    """

    out_dict = {}
    for pos, synsets in pos_synsets.items():
        remaining_synsets = []
        for synset in synsets:
            if issynset:
                if not (synset[1].name() in remove_dict[pos]):
                    #                     print(synset[1])
                    remaining_synsets.append(synset)
            else:
                if not (synset[0] in remove_dict[pos]):
                    remaining_synsets.append(synset)
        out_dict[pos] = remaining_synsets

    return out_dict


#======================================================================
# Finding Hyponyms
#======================================================================


class Keyword_synsets:
    """
    For storing hyponyms for each synset
    """
    
    def __init__(self, synset, pos, linked_word, hyponyms):
        """
        :param synset: wordnet synset
        :type  synset: nltk.corpus.reader.wordnet.Synset
        :param pos: part of speech of synset
        :type  pos: str
        :param linked_word: word that the synset was found from
        :type  linked_word: str
        :param hyponyms: list of hyponyms
        :type  hyponyms: list
        """
        
        self.synset = synset
        self.pos = pos
        self.linked_word = linked_word
        self.hyponyms = hyponyms
        
    def find_hyponyms(self):
        self.hyponyms = find_hypo(self.synset)


def find_hypo(synset):
    """
    Given a synset, find all the hyponyms.

    :param synset: wordnet synset
    :type  synset: nltk.corpus.reader.wordnet.Synset
    :returns: list of hyponyms of a synset
    :rtype:   list
    """

    def hypo(s): return s.hyponyms()
    synsets = list(synset.closure(hypo))
    names = [name for synset in synsets for name in synset.lemma_names()]

    # do not want phrases
    filtered = list(filter(lambda x: '_' not in x, names))

    return sorted(filtered)


def create_synset_tree(synset, path):
    """
    Create a graph connecting each hyponym to the synset

    :param synset: wordnet synset
    :type  synset: nltk.corpus.reader.wordnet.Synset
    :param path: output path
    :type  path: str
    """

    from graphviz import Digraph

    str_numbers = []

    name = synset.name().split('.')[0]
    dot = Digraph(comment=name)
    hyponyms = find_hypo(synset)
    for i, hyponym in enumerate(hyponyms):
        number = str(i)
        dot.edge(name, hyponym)
        str_numbers.append(number)

    dot.render(path, view=True)


def find_hypo_for_all_synsets(pos_synsets):
    """
    Create a list of instances of Keyword_synsets,
    and find the hyponyms

    :param pos_synsets: dictionary mapping pos to list of 
                        bi-tuples, where first item is the word
                        and second item is the synset
    :type  pos_synsets: dict
    :returns: list of Keyword_synsets instances
    :rtype:   list
    """

    list_of_keywords_synset_instances = []

    for pos, synsets in pos_synsets.items():
        for synset in synsets:
            instance = Keyword_synsets(synset[1], pos, synset[0], [])
            instance.find_hyponyms()
            list_of_keywords_synset_instances.append(instance)

    return list_of_keywords_synset_instances


#======================================================================
# Printing Outputs
#======================================================================


def print_definitions(pos_synsets, file_name):
    """
    Print the word, synset, definitions

    :param pos_synsets: dictionary mapping pos to list of 
                        bi-tuples, where first item is the word
                        and second item is the synset
    :type  pos_synsets: dict
    :param file_name: file name to write to
    :type  file_name: str
    """

    file = open(file_name, 'w')

    def print_write(string):
        """
        Print the string and write the string to the file

        :param string: string
        :type  string: str
        """

        file.write(string)
        print(string)

    for pos, synsets in pos_synsets.items():
        pos = "Part of Speech is: {}\n".format(pos) + '\n'
        print_write(pos)
        for synset in synsets:
            name = "\tName: " + synset[0] + '\n'
            str_synset = "\t\tSynset: " + synset[1].name() + '\n'
            definition = "\t\tDefinition: " + synset[1].definition() + '\n'

            print_write(name)
            print_write(str_synset)
            print_write(definition)

            example_list = synset[1].examples()
            if len(example_list) != 0:
                examples = "\t\tExample: " + example_list[0] + '\n'
                print_write(examples)


def write_out_hyponyms(list_synsets, file_name):
    """
    Print out the hyponyms and pertaining infomatuon

    :param list_synsets: list of Keyword_synsets instances
    :type  list_synsets: list
    :param file_name: file name to write to
    :type  file_name: str
    """

    file = open(file_name, 'w')

    def print_write(string):
        """
        Print the string and write the string to the file

        :param string: string
        :type  string: str
        """

        file.write(string)
        print(string)

        # (self, synset, pos, linked_word, hyponyms)
    for synset in list_synsets:
        word = "Linked Word: " + synset.linked_word + '\n'
        pos = "\tPart of Speech: " + synset.pos + '\n'
        out_synset = '\tSynset: ' + synset.synset.name() + '\n'
        definition = "\tDefinition: " + synset.synset.definition() + '\n'

        print_write(word)
        print_write(pos)
        print_write(out_synset)
        print_write(definition)

        out_hyponyms = ', '.join(synset.hyponyms)
        print_write("\tHyponyms:\n")
        print_write('\t' + out_hyponyms)
        print_write('\n')


def write_resulting_words(list_synsets, file_name):
    """
    Create a file that only contains the hyponyms.
    
    :param list_synsets: list of Keyword_synsets instances
    :type  list_synsets: list
    :param file_name: file name to write to
    :type  file_name: str
    """
    
    file = open(file_name, 'w')

    file.write('WORDS\n')
    for synset in list_synsets:
        out_hyponyms = '\n'.join(synset.hyponyms)
        file.write(out_hyponyms)