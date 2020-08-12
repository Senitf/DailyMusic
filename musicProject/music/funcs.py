from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import uuid
import os

options = webdriver.ChromeOptions()
options.add_argument('headless')

def PlayTrailerOnYoutube(title, artist):
    driver = webdriver.Chrome("music/chromedriver", chrome_options=options)
    query = "https://www.youtube.com/results?search_query=" + title + " " + artist
    driver.get(query)

    link = driver.page_source
    soup = BeautifulSoup(link, "lxml")

    lists = soup.select('#video-title')
    links = lists[0].attrs['href']
    links = links[9:]

    return "https://www.youtube.com/embed/" + links

def get_file_path(instance, filename):
    filename = instance.title + "_" + instance.artist + ".jpeg"
    return os.path.join('album_image/%Y/%m/%d', filename)

def get_file_path_playlist(instance, filename):
    filename = instance.title + "_" + str(instance.author) + ".jpeg"
    return os.path.join('playlist_image/%Y/%m/%d', filename)
