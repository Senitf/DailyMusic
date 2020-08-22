from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import uuid
import os
from uuid import uuid4
from django.utils import timezone

def get_file_path(instance, filename):
    filename = instance.title + "_" + str(instance.author) + ".jpeg"
    return os.path.join("playlist_image/%Y/%m/%d", filename)
