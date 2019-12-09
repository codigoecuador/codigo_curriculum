# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:06:25 2019

@author: rayde
https://towardsdatascience.com/easily-scrape-and-summarize-news-articles-using-python-dfc7667d9e74
https://github.com/chaimgluck/blog-posts/blob/master/scrape-news/scraping-and-summarizing-news-articles.ipynb
"""

#Scrape and Summarize News Articles Using Python

'''
In today's digital world, we're bombarded with endless information.
1) scrape using requests and BeautifulSoup packages
2) summarize using the gensim library. 
'''

import requests 
from bs4 import BeautifulSoup
from gensim.summarization import summarize

#retrieve page text

url = 'https://www.npr.org/2019/07/10/740387601/university-of-texas-austin-promises-free-tuition-for-low-income-students-in-2020'

page = requests.get(url).text

#Turn page into beautifulsoup object to access HTML tags
soup = BeautifulSoup(page)

#Entonces, nosotros buscamos cual HTML tags contienen titular y texto principal de la articulo. 

'''
To do this, we'll use Google Chrome's excellent Inspect tool. Open the news article we chose in a new tab, right click on the page and choose inspect
Open the news article we chose in a new tab, right-click on the page and choose inspect rom the drop-down menu. 
That will bring up the Inspect tool which looks like this:

Click on the little button outlined above to find the HTML tags corresponding to anything you see on the page. 
When you hover over the text of the article, you'll see which HTML tags are used to identify that text.

The headline of the article is surrounded by the <h1> tag. We'll select the first <h1> tag on the page like this:
    
'''

#Get Headline

headline = soup.find('h1').get_text()

'''
The main text of the article is surrounded by the <p> tag. This time we'll have to find all of the <p> tags contained
on the page since the paragraphs of the article are each contained in a <p> tag.

'''

#Get text from all <p> tags.
p_tags = soup.find_all('p')
#Get the text from each of the "p" tags and strip surrounding whitespace.
p_tags_text = [tag.get_text().strip() for tag in p_tags]

'''
If you examine the text we've retrieved in the 'p_tags_text' variable, you'll notice there are some bits of text
that aren't from the main article, like the author's name and some image captions. Since theya re also delineated using <p> tags, 
we've selected them too. To clean up the text we have, we can use a couple of quick list comprehensions to filter out types of text we know aren't part of the 
main article. 
'''

#Filter out sentences that contain newline characters '\n' or don't contain periods. 

sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]

sentence_list = [sentence for sentence in sentence_list if '.' in sentence]

#combine list items into string. 

article = ' '.join(sentence_list)

'''
Now that we have the text of the article, we can summarize it. 

Gensim is an excellent Python package for a variety of NLP tasks.
It includes a fairly robust summarization function that is easy to use. 
It's a variation of the TextRank algorithm. 
'''

summary = summarize(article, ratio = 0.3)

print(f'Length of original article: {len(article)}')
print(f'Length of summary: {len(summary)} \n')
print(f'Headline: {headline} \n')
print(f'Article Summary: \n{summary}')


