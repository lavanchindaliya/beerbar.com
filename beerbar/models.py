from django.db import models




class Beer(models.Model):
    def __str__(self):
        return self.name
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='beer')
    image = models.ImageField(default='Images/None/No0img.jpg')


class Whisky(models.Model):
    def __str__(self):
        return self.name
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='whisky')
    image = models.ImageField(default='Images/None/No0img.jpg')


class Rum(models.Model):
    def __str__(self):
        return self.name
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='rum')
    image = models.ImageField(default='Images/None/No0img.jpg')


class Vodka(models.Model):
    def __str__(self):
        return self.name
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='vodka')
    image = models.ImageField(default='Images/None/No0img.jpg')


class Wine(models.Model):
    def __str__(self):
        return self.name
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='wine')
    image = models.ImageField(default='Images/None/No0img.jpg')
    

class Gin(models.Model):
    def __str__(self):
        return self.name
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='gin')
    image = models.ImageField(default='Images/None/No0img.jpg')


class Mezcal(models.Model):
    def __str__(self):
        return self.name
    brand = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='mezcal')
    image = models.ImageField(default='Images/None/No0img.jpg')
    
    
class Order(models.Model):
    def __str__(self):
        return self.name
    customer = models.CharField(max_length=70, default='admin')
    name = models.CharField(max_length=70)
    price = models.CharField(max_length=70)
    



class Task(models.Model):
    def __str__(self):
        return self.task_name
    task_name = models.CharField(max_length=200)
    task_desc = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='Images/', default='Images/None/No0img.jpg')
