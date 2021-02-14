from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Activities(models.Model):
     activity_id = models.CharField(max_length=100, unique=True)
     pickup_date = models.DateTimeField()
     pickup_location = models.TextField()
     date_picked_up = models.DateTimeField(null=True)
     delivery_date = models.DateTimeField()
     date_delivered = models.DateTimeField(null=True)
     delivery_address = models.TextField(null=False)
     number_of_boxes = models.IntegerField(null=False, default=1)
     date_user_requested_service = models.DateTimeField(default=timezone.now)
     user_name = models.ForeignKey(User,related_name="custom_user", on_delete=models.CASCADE)
     pickup_name = models.ForeignKey(User,related_name="Pick_up_guy",null=True, on_delete=models.CASCADE)
     delivery_name = models.ForeignKey(User, related_name="Delivery_guy",null=True, on_delete=models.CASCADE)
     storage_name = models.ForeignKey(User, related_name="Storage_guy",null=True, on_delete=models.CASCADE)

     def __str__(self):
         return self.activity_id

     def get_absolute_url(self):
        return reverse('info-home') #, kwargs={'pk': self.pk}

class HashTable(models.Model):
    hash1 = models.TextField(blank=True)
    hash2 = models.TextField(blank=True)
    hash3 = models.TextField(blank=True)
    hash4 = models.TextField(blank=True)
    activity_id = models.ForeignKey(Activities, on_delete=models.CASCADE)

    def __str__(self):
        return_string = str(self.activity_id)
        return return_string.format(self)
