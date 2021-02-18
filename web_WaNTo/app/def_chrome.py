from bs4 import BeautifulSoup
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time 
import re
import requests

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
    driver.implicitly_wait(10)
    return driver


def search(driver, kw):
    input_element = driver.find_element_by_name('q')
    input_element.clear()
    input_element.send_keys(kw)
    input_element.send_keys(Keys.RETURN)
    time.sleep(2)  

def re_pattern(except_file):
    with open(except_file) as f:
        pattern_lists = [s.strip() for s in f.readlines()]
    pattern_list = '|'.join(pattern_lists)
    pattern = re.compile(pattern_list)
    return pattern

def get_title(url):
    headers_dic = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    url_info = requests.get(url,headers=headers_dic)
    url_html = BeautifulSoup(url_info.content, "html.parser")
    title = url_html.find('title')
    return title.text

def macth_search(url_dict, domain_name):
    flag=False
    for key in url_dict.keys():
        if domain_name in key :
            flag = True
            break
    return flag

def adress_list(driver,pattern,url_dict,except_url_dict):
    class_name = "yuRUbf"
    class_elems = driver.find_elements_by_class_name(class_name)
    for elem in class_elems:
        a_tag = elem.find_element_by_tag_name("a")
        url = a_tag.get_attribute("href")
        domain_name = urlparse(url).netloc
        if bool(pattern.search(domain_name)):
            title = get_title(url)
            flag = macth_search(except_url_dict,domain_name)
            if flag:
                continue
            except_url_dict[url] = title
        else:
            title = get_title(url)
            flag = macth_search(url_dict,domain_name)
            if flag:
                continue
            url_dict[url] = title
    return url_dict,except_url_dict

def next_page(driver):
    next_button = driver.find_element_by_id("pnnext")
    next_button.click()


# main
def get_url(driver,page_range,except_file):
    page_range += 1
    pattern = re_pattern(except_file)
    url_dict = {}
    except_url_dict = {}
    for page_num in range(1,page_range):
        url_dict,except_url_dict = adress_list(driver,pattern, url_dict, except_url_dict)
        next_page(driver)
    return url_dict,except_url_dict

