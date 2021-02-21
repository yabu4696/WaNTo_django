from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time 
import re
import requests
import os


def make_driver():
    CHROME_BIN = '/opt/google/chrome/chrome'
    CHROME_DRIVER = '/opt/chrome/chromedriver'

    options = Options()
    options.binary_location = CHROME_BIN
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument('--lang=ja-JP')
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options,executable_path = CHROME_DRIVER)
    driver.implicitly_wait(1)
    return driver


def search(driver, kw):
    # kw = input('検索：')
    input_element = driver.find_element_by_name('q')
    input_element.clear()
    input_element.send_keys(kw)
    input_element.send_keys(Keys.RETURN)
    time.sleep(2)

def re_pattern(except_file_main,except_file_sub):
    with open(except_file_main) as f:
        pattern_main_lists = [s.strip() for s in f.readlines()]
    with open(except_file_sub) as f:
        pattern_sub_lists = [s.strip() for s in f.readlines()]
    pattern_lists = pattern_main_lists + pattern_sub_lists
    pattern_list = '|'.join(pattern_lists)
    pattern = re.compile(pattern_list)
    return pattern  

def get_title(url):
    headers_dic = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    # os.environ['CURL_CA_BUNDLE'] = ''
    ssl_path = '/usr/local/lib/python3.8/dist-packages/certifi/cacert.pem'
    url_info = requests.get(url, verify=ssl_path ,headers=headers_dic)
    url_html = BeautifulSoup(url_info.content, "html.parser")
    title = url_html.find('title')
    return title.text

def macth_search(dictionary, domain_name):
    flag=False
    for key in dictionary.keys():
        if domain_name in key :
            flag = True
            break
    return flag

def next_page(driver):
    next_button = driver.find_element_by_id("pnnext")
    next_button.click()

def re_pattern_title(contain_file):
    with open(contain_file) as f:
        pattern_lists = [s.strip() for s in f.readlines()]
    pattern_list = '|'.join(pattern_lists)
    title_pattern = re.compile(pattern_list)
    return title_pattern

def adress_list(driver,in_keyword,out_keyword,pattern,title_pattern):
    class_name = "yuRUbf"
    class_elems = driver.find_elements_by_class_name(class_name)

    for elem in class_elems:
        a_tag = elem.find_element_by_tag_name("a")
        url = a_tag.get_attribute("href")
        domain_name = urlparse(url).netloc

        if not bool(pattern.search(url)):
            try:
                title = get_title(url)
            except AttributeError:
                continue
            if (len(title) > 255) or (len(url) > 200):
                continue
            flag_in = macth_search(in_keyword,domain_name)
            flag_out = macth_search(out_keyword,domain_name)
            if flag_in or flag_out:
                continue
            if bool(title_pattern.search(title)):
                in_keyword[url] = title
            else:
                out_keyword[url] = title                
    return in_keyword,out_keyword


def get_url(driver,page_range,except_file_main,except_file_sub,contain_file):
    page_range += 1
    pattern = re_pattern(except_file_main,except_file_sub)
    title_pattern = re_pattern_title(contain_file)
    in_keyword = {}
    out_keyword = {}
    for page_num in range(1,page_range):
        in_keyword,out_keyword = adress_list(driver,in_keyword,out_keyword,pattern,title_pattern)
        next_page(driver)
        
    return in_keyword, out_keyword