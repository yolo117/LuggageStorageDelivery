from django.db.models.signals import post_save
from django.contrib.auth.models import User
from info.models import Activities, HashTable
from django.dispatch import receiver
import qrcode
from datetime import datetime
import os

@receiver(post_save, sender=Activities)
def create_hash_and_generate_qrcode(sender, instance, created, **kwargs):
    print(instance)
    # hashed_value = hash(instance.activity_id + "" + instance.pickup_date.strftime("%m/%d/%Y") + "" +instance.pickup_location + "" +instance.delivery_date.strftime("%m/%d/%Y") + instance.delivery_address+ "" + str(instance.number_of_boxes)+instance.user_name.username)
    # if the HashT object is not found then creates a new object else pulls the old instance
    new_hash_object, created = HashTable.objects.get_or_create(activity_id=instance)
    if created:
        hashed_value = hash(instance.activity_id + "" + instance.pickup_date.strftime("%m/%d/%Y") + "" +instance.pickup_location + "" +instance.delivery_date.strftime("%m/%d/%Y") + instance.delivery_address+ "" + str(instance.number_of_boxes)+instance.user_name.username)
        new_hash_object.hash1 = hashed_value
        new_hash_object.save()
        generate_qr(hashed_value)
    else:
        if new_hash_object.hash3 == "" and new_hash_object.hash4 == "" and new_hash_object.hash1 != "" and new_hash_object.hash2 == "" :
            new_hash_object.hash2 = hash(str(hashed_value)+""+ instance.date_picked_up.strftime("%m/%d/%Y")+""+str(instance.pickup_name) )
            print(new_hash_object.hash2)
            # new_hash_object.
            new_hash_object.save()
            generate_qr(new_hash_object.hash2)
        elif new_hash_object.hash4 == "" and new_hash_object.hash1 != "" and new_hash_object.hash2 != "" and new_hash_object.hash3 == "":
            new_hash_object.hash3 = hash(str(hashed_value)+""+ instance.date_picked_up.strftime("%m/%d/%Y")+""+str(instance.pickup_name) )
            print(new_hash_object.hash3)

            new_hash_object.save()
            generate_qr(new_hash_object.hash3)
        elif new_hash_object.hash1 != "" and new_hash_object.hash2 != "" and new_hash_object.hash3 != "" and new_hash_object.hash4 == "":
            new_hash_object.hash4 = hash(str(hashed_value)+""+ instance.date_picked_up.strftime("%m/%d/%Y")+""+str(instance.pickup_name) )
            print(new_hash_object.hash4)
            # new_hash_object.
            new_hash_object.save()
            generate_qr(new_hash_object.hash4)

    # if created:
    #     if not activity_present(instance): # if no hashtable object no hashes then create a HashTable
    #         hashed_value = hash(instance.activity_id + "" + instance.pickup_date.strftime("%m/%d/%Y") + "" +instance.pickup_location + "" +instance.delivery_date.strftime("%m/%d/%Y") + instance.delivery_address+ "" + str(instance.number_of_boxes)+instance.user_name.username)
    #         new_hash_object = HashTable.objects.create(activity_id=instance)
    #         new_hash_object.hash1 = hashed_value
    #         new_hash_object.save()
    #         generate_qr(hashed_value)
    #     else :
    #         hashObject = HashTable.objects.get(activity_id=instance.pk)
    #         print
    #         if hashObject.hash3 == "" and hashObject.hash4 == "" and hashObject.hash1 != "" and hashObject.hash2 == "" :
    #             print('create Hash2')
    #         elif hashObject.hash4 == "" and hashObject.hash1 != "" and hashObject.hash2 != "" and hashObject.hash3 == "":
    #             print('create Hash3')
    #         elif hashObject.hash1 != "" and hashObject.hash2 != "" and hashObject.hash3 != "" and hashObject.hash4 == "":
    #             print('create Hash4')
    #
    #         hashObject.hash2 =hash(hashObject.hash1 + instance.pickup_date.strftime("%m/%d/%Y") + instance.pickup_name.username)
    #         hashObject.save()

        #
        # generate_qr(hashed_value)
    # if HashTable.objects.get(activity_id=instance.pk):
    #     print(' There is already a hashtable object for the activity')
    # if HashTable.objects.get(activity_id=instance).hash1 == None:
    #     print('There is no hash1')

def activity_present(hash_object):
    if HashTable.objects.filter(activity_id=hash_object).exists():
        return True
    else:
        return False

def generate_qr(string):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 10,
        border = 4,
    )
    qr.add_data(string)
    qr.make(fit=True)
    img = qr.make_image()
    os.mkdir('/Users/clinton/Django/TT/TT/media/QRCodes/'+str(string))
    img.save('/Users/clinton/Django/TT/TT/media/QRCodes/'+str(string)+'/'+str(string)+'.jpg')


# @receiver(post_save, sender=Activities)
# def save_hash(sender, instance, **kwargs):
#     # print(sender)
#     # print(instance)
#     HashTable.objects.save()
# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
