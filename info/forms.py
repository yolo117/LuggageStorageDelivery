from django import forms
from info.models import Activities

class DateInput(forms.DateInput):
    input_type = 'date'

class NewActivityForm(forms.ModelForm):
    pickup_date = forms.DateField(widget=DateInput)
    delivery_date = forms.DateField(widget=DateInput)

    class Meta:
        model = Activities
        fields = ['activity_id', 'pickup_date', 'pickup_location', 'delivery_date', 'delivery_address','number_of_boxes']
    #we overide the method to set the current user as the creator of the current activity


class UpdateActivityUser(forms.ModelForm):

    class Meta:
        model = Activities
        fields = ['pickup_date', 'delivery_date', 'delivery_address']

class UpdateActivityPickup(forms.ModelForm):
    # date_picked_up = forms.DateField(widget=DateInput)
    class Meta:
        model = Activities
        fields = []

class UpdateActivityStorage(forms.ModelForm):

    class Meta:
        model = Activities
        fields = []

class UpdateActivityDelivery(forms.ModelForm):
    date_delivered = forms.DateField(widget=DateInput)
    class Meta:
        model = Activities
        fields = ['date_delivered']
