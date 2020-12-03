#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
import pandas as pd


def scrape():

    # #Using chrome to show the process
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)


    #NASA Mars News


    #Visiting the page through the test browser
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')


    #Assigning news title and paragraph to variables
    step_one=soup.select_one("ul.item_list li.slide")
    news_title=step_one.find('div', class_='content_title').text
    news_p=step_one.find("div", class_="article_teaser_body").text

    print(news_title)
    print(news_p)



    #JPL Mars Space Images



    # New url
    img_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(img_url)


    # Click button
    button = browser.find_by_id('full_image').click()



    # Click button on next page "more info"
    button2 = browser.links.find_by_partial_text("more info").click()



    # Get image
    #Use BeautifulSoup to parse the html
    html_image=browser.html
    b_soup = BeautifulSoup(html_image, 'html.parser')



    # Webscrape to find the image source


    img_src=b_soup.find(class_="lede")   
    img_src2=img_src.find("a", href=True)
    img_src3 = img_src2.find("img").get('src')


    # #Base URL
    base_url= "https://www.jpl.nasa.gov"

    # #Combined URL
    featured_image_url = base_url + img_src3
    print(featured_image_url)



    # Mars Facts



    # New url
    f_url = 'https://space-facts.com/mars/'
    browser.visit(f_url)



    # Pandas scraping
    tables = pd.read_html(f_url)



    # Selecting the table we want
    facts_df=tables[0]
    facts_df.head(10)



    # Converting data to HTML table string
    html_table = facts_df.to_html()
    html_table



    # Mars Hemispheres

    # New url
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/'
    browser.visit(usgs_url)

    # Beautiful Soup Parser
    usgs_html=browser.html
    usgs_soup = BeautifulSoup(usgs_html, 'html.parser')


    #List of dictionaries: titles and links
    hemisphere_image_urls = []

    #Create list of the four hemisphere link htmls
    hemi_list = usgs_soup.find_all("div", class_="item")

    #Loop to go through the four links
    for hemi in hemi_list:
        title_full = hemi.find("h3").text
        # Remove "Enhanced" from all titles
        title = title_full.replace("Enhanced","")
        # Clicking links
        browser.links.find_by_partial_text(title).click()
        # Because on new page, need to make new html object
        usgs_img_html=browser.html
        usgs_img_soup=BeautifulSoup(usgs_img_html, 'html.parser')
        # Saving the url string and title
        base_url_hemi='https://astrogeology.usgs.gov'
        source= usgs_img_soup.find("img", class_="wide-image").get('src')
        usgs_img_url = base_url_hemi + source
        # Appending info to list
        hemisphere_image_urls.append({"title": title, "img_url": usgs_img_url})
        
    #Print list of dictionaries
    hemisphere_image_urls

    #returning dictionary containing all of the scraped data
    scraped_data = {"News Title": news_title,
                    "News Paragraph": news_p,
                    "Featured Image": featured_image_url,
                    "Mars Facts": html_table,
                    "Hemispheres": hemisphere_image_urls
                    }
    
    browser.quit()
    
    return(scraped_data)
    print(scraped_data)
        

