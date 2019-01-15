# Yelp

This repository contains code for scraping Yelp and performing text analysis on Yelp Reviews.

## API

For Yelp API, I gathered data on cafes in Chicago through the overlapping circle tessellation method.
We send a query containing the coordinates of the grid and the radius of search.

Turned out to be incredibly inefficient and slow because for each iteration, we would get repeated results. Also, we were extremely limited by what we were allowed to get.

## Crawler

Used BeautifulSoup to first extract business links, then for each link, extract the reviews. 

Problems: not scalable. Would work well if there weren't methods that Yelp uses to block scrapers.

Instead, used Scrapy to scrape websites. Also works pretty well.

The crawler project has been abandoned because professor Clark said a professor from Toronto can deal with the scraping (though it has been 2 monthes and we haven't heard anything from that professor), and Clark wants me to focus more on the sociological thinking.

## Natural Language Processing

Since I have a small, but working scraper, I can extract info from a few websites. I currently use this data as a warm-up for when the real data arrives.

Calculated word frequencies of certain words that can describe Bohemian culture. Made plots.

I completely disagreed with my professor about how to analyze Yelp reviews, but was able to change his mind about how to approach Yelp reviews. I thought it would be a good idea to use Word2Vec to cateogorize words without having to manually do it. The description of the process can be viewed [here](https://github.com/JinLi711/UIA/tree/master/Notes%20and%20Record%20Files). Also made a lot of plots.