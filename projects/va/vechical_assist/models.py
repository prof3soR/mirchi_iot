from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    dp=models.ImageField(upload_to="static/images")
    def __str__(self):
        return f"{self.user.first_name}"
    

class mechanic(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    alt_mobile=models.CharField(max_length=10)
    dp=models.ImageField(upload_to="static/images")
    shop_dp=models.ImageField(upload_to="static/images")
    address=models.TextField()
    status=models.BooleanField(default=False)
    car_company=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.user.first_name}"
    

class service_Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    request_status=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Address= models.CharField(max_length=512)
    contact=models.PositiveIntegerField()
    lat=models.FloatField()
    log=models.FloatField()
    car_company=models.CharField(max_length=100)
    dateandtime=models.DateTimeField()
    def __str__(self):
        return f"{self.user} request"
