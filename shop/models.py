from django.db import models

import datetime
import os

# Usage
# 1. Uploading Files:
# When a file is uploaded to the image field, the getFileName function is called to generate a unique path for the file. The file will be saved in the uploads/ directory with a name prefixed by the current timestamp.

# 2. Saving Categories:
# When creating a Category object, you can optionally upload an image. If no image is provided, the image field will remain empty.

# Function to generate a unique file path for uploaded files
def getFileName(request,FileName):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_FileName="%s%s"%(now_time,FileName)
    return os.path.join('uploads/',new_FileName)

class Category(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    # trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE) # foreign key of the category class data
    name=models.CharField(max_length=50,null=False,blank=False)
    vendor=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
