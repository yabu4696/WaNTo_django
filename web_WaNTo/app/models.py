from django.db import models

from . import def_chrome 

    

class Item_maker(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Wantoitem(models.Model):
    item_name = models.CharField(blank=True,null=True,max_length=255)
    maker_name = models.ForeignKey(Item_maker,on_delete=models.PROTECT)
    tag = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)
            
    def __str__(self):
        return self.item_name

    def scraping(self):
        driver = def_chrome.make_driver()
        driver.get("https://google.com")
        search_word = self.maker_name.name + ' ' + self.item_name
        def_chrome.search(driver, search_word)
        except_file_main = './app/pattern/except_main_list.txt'
        except_file_sub = './app/pattern/except_sub_list.txt'
        contain_title = './app/pattern/contain_title.txt'
        except_title = './app/pattern/except_title.txt'

        in_keyword,out_keyword = def_chrome.get_url(driver,except_file_main,except_file_sub,contain_title,except_title)
        driver.close()
        return in_keyword,out_keyword

class Main(models.Model):
    wantoitem = models.ForeignKey(Wantoitem, on_delete=models.CASCADE) 
    main_url = models.URLField(max_length=200)
    main_title = models.CharField(max_length=255)
    main_ogp_img = models.URLField(max_length =200,blank=True,null=True)

class Sub(models.Model):
    wantoitem = models.ForeignKey(Wantoitem, on_delete=models.CASCADE)
    sub_url = models.URLField(max_length =200)
    sub_title = models.CharField(max_length=255)
    sub_ogp_img = models.URLField(max_length =200,blank=True,null=True)
