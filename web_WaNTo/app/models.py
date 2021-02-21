from django.db import models

from . import def_chrome 

class Wantoitem(models.Model):
    item_name = models.CharField(blank=True,null=True,max_length=255)
    # maker_name = models.CharField(blank=True,null=True,max_length=255)
    # key_word = models.CharField(blank=True,null=True,max_length=255)

    def __str__(self):
        return self.item_name

    def scraping(self):
        driver = def_chrome.make_driver()
        driver.get("https://google.com")
        def_chrome.search(driver,self.item_name)

        except_file_main = './app/except_main_list.txt'
        except_file_sub = './app/except_sub_list.txt'
        contain_file = './app/contain_file.txt'
        page_range = 2

        in_keyword,out_keyword = def_chrome.get_url(driver,page_range,except_file_main,except_file_sub,contain_file)
        driver.close()
        return in_keyword,out_keyword
    
class Main(models.Model):
    wantoitem = models.ForeignKey(Wantoitem, on_delete=models.CASCADE) 
    main_url = models.URLField(max_length=200)
    main_title = models.CharField(max_length=255)

class Sub(models.Model):
    wantoitem = models.ForeignKey(Wantoitem, on_delete=models.CASCADE)
    sub_url = models.URLField(max_length =200)
    sub_title = models.CharField(max_length=255)




