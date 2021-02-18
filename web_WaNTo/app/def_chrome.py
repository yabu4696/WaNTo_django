import urllib.request as req
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time 
import re

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
    # kw = input('検索：')
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

def adress_list(driver,url_list,except_url_list,pattern):
    class_name = "yuRUbf"
    class_elems = driver.find_elements_by_class_name(class_name)

    for elem in class_elems:
        a_tag = elem.find_element_by_tag_name("a")
        url = a_tag.get_attribute("href")
        if pattern.search(url):
            except_url_list.append(url)
        else:
            url_list.append(url)
    return url_list,except_url_list

def next_page(driver):
    next_button = driver.find_element_by_id("pnnext")
    next_button.click()


def get_url(driver,page_range,except_file):
    page_range += 1
    pattern = re_pattern(except_file)
    url_list = []
    except_url_list = []
    for page_num in range(1,page_range):
        url_list,except_url_list = adress_list(driver,url_list,except_url_list,pattern)
        next_page(driver)
    # print('Get URL!')
    return url_list,except_url_list

def screen_shot(driver):
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    print('page_width', page_width, sep=':')
    print('page_height', page_height, sep=':')
    driver.set_window_size(page_width, page_height)
    driver.save_screenshot('search_results.png')

