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

        except_file = '/workspace/app/except_list.txt'
        page_range = 1

        url_dict,except_url_dict = def_chrome.get_url(driver,page_range,except_file)
        driver.close()
        return url_dict,except_url_dict

class Main(models.Model):
    wantoitem = models.ForeignKey(Wantoitem, on_delete=models.CASCADE) 
    main_url = models.URLField(max_length=200)
    main_title = models.CharField(max_length=200)

class Except(models.Model):
    wantoitem = models.ForeignKey(Wantoitem, on_delete=models.CASCADE)
    except_url = models.URLField(max_length =200)
    except_title = models.CharField(max_length=200)




