from django.db import models
import datetime
import os

def filename(request,filename):
  now_time=datetime.datetime.now().strftime("%y%m%d%H:%M:%S")
  new_filename="%s%s"%(now_time,filename)
  return os.path.join('uploads/',new_filename)


class Catagory(models.Model):
  name=models.CharField(max_length=150,null=False,blank=False)
  image=models.ImageField(upload_to=filename,null=True,blank=True)
  descrption=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-hidden")
  trending=models.BooleanField(default=False,help_text="0-default,1-trending")
  created_at=models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now_add=True)
  is_active = models.BooleanField(default=True)
  is_deleted = models.BooleanField(default=False)
  
  def __str__(self):
    return self.name  

class Products(models.Model):
  Catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
  name=models.CharField(max_length=150,null=False,blank=False)
  vendor=models.CharField(max_length=150,null=False,blank=False)
  Product_image=models.ImageField(upload_to=filename,null=True,blank=True)
  quantity=models.IntegerField(null=False,blank=False)
  original_price=models.IntegerField(null=False,blank=False)
  selling_price=models.IntegerField(null=False,blank=False)
  descrption=models.TextField(max_length=500,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-hidden")
  trending=models.BooleanField(default=False,help_text="0-default,1-trending")
  created_at=models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now_add=True)
  is_active = models.BooleanField(default=True)
  is_deleted = models.BooleanField(default=False)