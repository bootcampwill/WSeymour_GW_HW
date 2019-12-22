# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
from bs4 import BeautifulSoup
#import chromedriver
from splinter import Browser

url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)
browser.visit(url)
html = browser.html
soup = BeautifulSoup(html, 'html.parser')

#find titles and article teasers in html
titles = soup.find('div', class_='content_title').text
article_teasers = soup.find('div', class_='article_teaser_body').text


# %%
#save them as variables for later
news_title = titles
news_p     = article_teasers
print(news_title)
print(news_p)


# %%
#set browser for jpl site
url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url)


# %%
#click on image link and get url for image
browser.find_by_id('full_image').click()
featured_image_url = browser.find_by_css('.fancybox-image').first['src']

featured_image_url


# %%
#get martian weather report
#url
twitter_url = "https://twitter.com/marswxreport?lang=en"
#visit url
browser.visit(twitter_url)
twitter_html = browser.html


# %%
#set up web driver to read javascript?
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(twitter_url)
twitter_html = driver.page_source
driver.close()


# %%
#make soup
twitter_soup = BeautifulSoup(twitter_html, 'html.parser')
#grab first tweet out of soup
mars_weather = twitter_soup.find_all('p', class_="tweet-text")[0].text
print(mars_weather)


# %%
#mars facts table
#url
mars_facts_url = 'https://space-facts.com/mars/'
#visit url
browser.visit(mars_facts_url)
mars_facts_html = browser.html
#make soup
mars_facts_soup = BeautifulSoup(mars_facts_html, 'html.parser')
#find table
mars_facts = mars_facts_soup.find_all('table', class_="tablepress-id-p-mars")[0].prettify()
print(mars_facts)


# %%
#convert to pandas DF
import pandas as pd
mars_table = pd.read_html(mars_facts)
mars_df = mars_table[0]
mars_df_html = pd.DataFrame.to_html(mars_df)
print(mars_df_html)


# %%
#mars hemispheres
#url
mars_hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#visit url
browser.visit(mars_hemispheres_url)
mars_hemispheres_html = browser.html
#make soup
mars_hemispheres_soup = BeautifulSoup(mars_hemispheres_html, 'html.parser')
#find table
mars_hemispheres = mars_hemispheres_soup.find_all('h3')

#create empty list to store hemispher names
hemisphere_list = []
#show html

for hemisphere in mars_hemispheres:
    hemisphere_list.append(hemisphere.text)


#create list of hemisphere urls
hemisphere_image_urls = []

#for loop using splinter to find links, click on them
for hemisphere in hemisphere_list:
    #click on link with hemisphere name
    browser.click_link_by_partial_text(hemisphere)
    #open page to full res
    browser.find_link_by_text('Open').first.click()
    #grab url
    hemisphere_url = browser.find_by_css('.wide-image').first['src']
    #add to dictionary
    hemisphere_image_dict = {'title': hemisphere, "img_url":hemisphere_url}
    #add dictionary to list
    hemisphere_image_urls.append(hemisphere_image_dict)
    #go back to 'home'page
    browser.visit(mars_hemispheres_url)


# %%
#did it work?
hemisphere_image_urls

#creat scrape function
# Defining scrape & dictionary
def scrape():
    final_data = {}
    final_data["mars_news"] = news_title
    final_data["mars_paragraph"] = news_p
    final_data["mars_image"] = featured_image_url
    final_data["mars_weather"] = mars_weather
    final_data["mars_facts"] = mars_df_html
    final_data["mars_hemisphere"] = hemisphere_image_urls

    return final_data
