from django.db import models

#ประะเภทสินค้า
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True,primary_key=True)
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
#คอมพิวเตอร์เซ็ต    
class Computer(models.Model):    
    id = models.CharField(max_length=3,default="",primary_key=True)       
    cid = models.CharField(max_length=5,default="") 
    name = models.CharField(max_length=100, default="") 
    brand = models.CharField(max_length=50, default="")
    price = models.FloatField(default=0.00)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    cpu = models.CharField(max_length=255, default="")
    cpuCooler = models.CharField(max_length=255, default="")
    mainboard = models.CharField(max_length=255, default="")
    ram = models.CharField(max_length=255, default="")
    storage = models.CharField(max_length=255, default="")
    case = models.CharField(max_length=255, default="")
    category = models.CharField(max_length=50, default="คอมพิวเตอร์")
    images = models.ImageField(upload_to='static/images',default='') 
    
    def __str__(self):
        return str(self.cid) + ':' + self.name + '('+ str(self.price) + ')'
    
class Monitor(models.Model):
    mid = models.CharField(max_length=5,default='',primary_key=True)
    name = models.CharField(max_length=255,default='')
    brand = models.CharField(max_length=50)
    price = models.FloatField(default=0.00)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    images = models.ImageField(upload_to='static/images',default='') 
    
    def __str__(self):
        return str(self.mid) + ':' + self.name + '('+ str(self.price) + ')'
    
    
class Printer(models.Model):
    pid = models.CharField(max_length=5,default='',primary_key=True)
    name = models.CharField(max_length=255,default='')
    brand = models.CharField(max_length=50)
    price = models.FloatField(default=0.00)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    images = models.ImageField(upload_to='static/images',default='') 
    
    def __str__(self):
        return str(self.pid) + ':' + self.name + '('+ str(self.price) + ')'
    
class Accessories(models.Model):
    aid = models.CharField(max_length=5,default='',primary_key=True)
    name = models.CharField(max_length=255,default='')
    brand = models.CharField(max_length=50)
    price = models.FloatField(default=0.00)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    images = models.ImageField(upload_to='static/images',default='') 
    
    def __str__(self):
        return str(self.aid) + ':' + self.name + '('+ str(self.price) + ')'
    
    
    
    
