# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w-q6murOQrUGyS3EqprgAe-thqYaN9Yv
"""

!apt install chromium-chromedriver

pip install selenium

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)

pip install beautifulsoup4

from bs4 import BeautifulSoup
import pandas as pd

products=[] #List to store name of the product
prices=[] #List to store price of the product
features=[] #List to store rating of the product

driver.get("https://www.flipkart.com/televisions/~cs-tmg2qb14kf/pr?sid=ckf%2Cczl&collection-tab-name=32%20Inch%20TVs&param=708&fm=neo%2Fmerchandising&iid=M_bd01b162-4352-4584-9b16-db320c6e80a3_4.K6WU5OYIZ1GM&ppt=browse&ppn=browse&ssid=eqyzjlgu000000001627208263761&otracker=hp_omu_Top%2BOffers_1_4.dealCard.OMU_K6WU5OYIZ1GM_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers_NA_dealCard_cc_1_NA_view-all_3&cid=K6WU5OYIZ1GM")

content = driver.page_source
soup = BeautifulSoup(content)


for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
    name=a.find('div',attrs={'class':'_4rR01T'})
    price=a.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    feature=a.find('div',attrs={'class':'fMghEO'})
    products.append(name.text)
    prices.append(price.text)
    features.append(feature.text)

df = pd.DataFrame({'Product Name':products,'Price':prices , 'Feature':features})
print(df.head())
df.to_csv('products.csv', index=False, encoding='utf-8')