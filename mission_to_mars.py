from bs4 import BeautifulSoup
import time
import pandas as pd
import cssutils
from splinter import Browser

# ### GET P and T

# In[3]:

def scrape():

    #get news
    browser = Browser('chrome', headless=False)
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    listings = {}
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    sidebar = soup.find('ul', class_='item_list ')

    categories = sidebar.find_all('li')

    listings["news_t"] = categories[0].find('h3').text
    listings["news_p"] = categories[0].find('a').text
    #GET IMG

    browser = Browser('chrome', headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    sidebar = soup.find('div', class_="carousel_items")
    div_style = sidebar.find('article')['style']
    style = cssutils.parseStyle(div_style)
    iurl = style['background-image']
    iurl = iurl.replace('url(', '').replace(')', '') 
    iurl
    listings["mars_image"]  = "https://www.jpl.nasa.gov/" + iurl


    #GET STATUS
    browser = Browser('chrome', headless=False)
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(2)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    sidebar = soup.find('div', class_="js-tweet-text-container")
    weather = sidebar.text
    weather = weather.rstrip()
    weather = weather.lstrip()
    listings["weather"] = weather

    listings["hemisphere_image_urls"] = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    ]

    return listings
