from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Activities(models.Model):
     activity_id = models.CharField(max_length=100)
     pickup_date = models.DateTimeField()
     pickup_destination = models.TextField()
     date_picked_up = models.DateTimeField(null=True)
     delivery_date = models.DateTimeField()
     date_delivered = models.DateTimeField(null=True)
     delivery_address = models.TextField(null=False)
     number_of_boxes = models.IntegerField(null=False)
     date_user_requested_service = models.DateTimeField(default=timezone.now)
     user_name = models.ForeignKey(User, on_delete=models.CASCADE)

     def __str__(self):
         return self.activity_id

class HashTable(models.Model):
    hash1 = models.TextField() #hash of the username+pickup_destination+delivery_destination+boxes
    hash2 = models.TextField() #hash of h1+date_picked_up+pickup_guy_name
    hash3 = models.TextField() #hash of h2+date_stored+storage_guy+Number_of_days
    hash4 = models.TextField() #hash 0f h3+delivery_date+delivery_guy
    activity_id = models.ForeignKey(Activities, on_delete=CASCADE)

    def __str__(self):
