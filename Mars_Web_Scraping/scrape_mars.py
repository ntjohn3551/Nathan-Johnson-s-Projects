from bs4 import BeautifulSoup as bs
import requests
import os
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager 
import pandas as pd
import time


def scrape_info():

    
    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # Define database and collection
    db = client.news_db
    collection = db.articles

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # URL to scrape
    url = 'https://redplanetscience.com'
    browser.visit(url) 

    time.sleep(1)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    # Retrieve the parent divs
    news_title = str(soup.find('div', class_='content_title').text)
    news_p = str(soup.find('div', class_='article_teaser_body').text)

    # Second URL to scrape
    url = 'https://spaceimages-mars.com'
    browser.visit(url) 

    time.sleep(1)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    # img = str(soup.find('a', class_='showimg fancybox-thumbs'))
    # img = img[41:65]

    # featured_image_url = 'https://spaceimages-mars.com/' + str(img) 
    featured_image_url = 'https://spaceimages-mars.com/' + str(soup.find('img', class_='headerimage fade-in')['src'])

    # Third URL to scrape
    url = 'https://galaxyfacts-mars.com'
    browser.visit(url) 

    time.sleep(1)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    tables = pd.read_html(url)

    # Create an HTML table
    df = tables[0]

    html_table = df.to_html(index=False, header=False, bold_rows=True)
    
    # df.to_html('table.html')

    # Fourth URL to scrape
    url = 'https://marshemispheres.com'
    browser.visit(url) 

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced').click()
    browser.links.find_by_partial_text('Open').click()

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    Cerberus_Hemisphere = 'https://marshemispheres.com/' + str(soup.find('img', class_='wide-image')['src'])

    # Fourth URL to scrape, used again
    url = 'https://marshemispheres.com'
    browser.visit(url) 

    time.sleep(1)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced').click()
    browser.links.find_by_partial_text('Open').click()

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    Schiaparelli_Hemisphere = 'https://marshemispheres.com/' + str(soup.find('img', class_='wide-image')['src'])

    # Fourth URL to scrape, used once again
    url = 'https://marshemispheres.com'
    browser.visit(url) 

    time.sleep(1)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced').click()
    browser.links.find_by_partial_text('Open').click()

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    Syrtis_Major_Hemisphere = 'https://marshemispheres.com/' + str(soup.find('img', class_='wide-image')['src'])

    # Fourth URL to scrape, used once again (This is necessary each time, to navigate the browser correctly)
    url = 'https://marshemispheres.com'
    browser.visit(url) 

    time.sleep(1)

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced').click()
    browser.links.find_by_partial_text('Open').click()

    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')

    Valles_Marineris_Hemisphere = 'https://marshemispheres.com/' + str(soup.find('img', class_='wide-image')['src'])


     # Store data in a dictionary
    mars_data = {
        "Cerberus_Hemisphere" : Cerberus_Hemisphere,
        "Schiaparelli_Hemisphere": Schiaparelli_Hemisphere,
        "Syrtis_Major_Hemisphere": Syrtis_Major_Hemisphere,
        "Valles_Marineris_Hemisphere": Valles_Marineris_Hemisphere,
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url" : featured_image_url,
        "html_table" : html_table
    }


    browser.quit()

    return mars_data