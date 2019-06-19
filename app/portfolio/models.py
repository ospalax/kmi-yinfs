from django.db import models

class Menu(models.Model):
    menu_item = models.CharField(max_length=100)
    order = models.IntegerField('Menu item order', default=0)
    def __str__(self):
        return self.menu_item

class Content(models.Model):
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    markup = models.CharField(max_length=2000)
    def __str__(self):
        return self.menu_item + '_Content'
