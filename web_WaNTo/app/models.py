from django.db import models

class Wantoitem(models.Model):
    item_name = models.CharField(blank=True,null=True,max_length=255)
    # maker_name = models.CharField(blank=True,null=True,max_length=255)
    # key_word = models.CharField(blank=True,null=True,max_length=255)

    def __str__(self):
        return self.item_name

