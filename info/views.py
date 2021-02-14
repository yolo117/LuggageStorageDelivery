from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from info.models import Activities, HashTable
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.widgets import AdminDateWidget
from info.forms import NewActivityForm, UpdateActivityPickup, UpdateActivityStorage, UpdateActivityDelivery
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from users.models import Profile
from datetime import datetime

# Create your views here.

# def Home(request):
#     # print(request.user)
#     context = {
#     'Activities': Activities.objects.filter(user_name=request.user)
#     }

    # return render(request, 'info/home.html', context)

class HomePageDispatchView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        # print(request.user.profile.user_type)
        if request.user.is_authenticated:

            if request.user.profile.user_type == 'Pickup':
                return PickedupActivitiesListView.as_view()(request, *args, **kwargs)
            elif request.user.profile.user_type == 'User':
                return UserActivitiesListView.as_view()(request, *args, **kwargs)
            elif request.user.profile.user_type =='Delivery':
                return DeliveryActivitiesListView.as_view()(request, *args, **kwargs)
            elif request.user.profile.user_type =='Storage':
                return StorageActivitiesAcceptedListView.as_view()(request, *args, **kwargs)
            else:
                messages.success(request, f'You do not have the appropriate user priveleges')
                return redirect('login')
        else:
            return redirect('login')


class UserActivitiesListView(LoginRequiredMixin, ListView):

    template_name = 'info/home.html'
    context_object_name = 'Activities'


    def get_queryset(self): #overided the get_queryset method to show case values of only the logged in user
        # print(self.request.user)
        return Activities.objects.filter(user_name=self.request.user).order_by('-date_user_requested_service')

#view for the pickup_guy
class PickedupActivitiesListView(LoginRequiredMixin, ListView): #list of all the activities that the pick_up guy has picked

    template_name = 'info/home.html'
    context_object_name = 'Activities'
    # form_class = UpdateActivityPickup
    def get_queryset(self): #overided the get_queryset method to show case values of only the logged in user
        # print(self.request.user)
        return Activities.objects.filter(pickup_name=self.request.user).order_by('-date_user_requested_service')




class PickupActivityListView(LoginRequiredMixin, ListView):

    template_name = 'info/home.html'
    context_object_name = 'Activities'
    def get_queryset(self): #overided the get_queryset method to show case values of only the logged in user
        # print(self.request.user)
        checker = 'Pickup-from-list'
        return Activities.objects.filter(pickup_name=None).order_by('-date_user_requested_service')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     checker = 'Pickup-from-list'
    #     return {'checker':checker}


# view for  the Storage guy
class StorageActivitiesAcceptedListView(LoginRequiredMixin, ListView):

    template_name = 'info/home.html'
    context_object_name = 'Activities'

    def get_queryset(self): #overided the get_queryset method to show case values of only the logged in user
        # print(self.request.user)
        return Activities.objects.filter(storage_name=self.request.user).order_by('-date_user_requested_service')

class StorageActivitiesNonAcceptedListView(LoginRequiredMixin, ListView):

    template_name = 'info/home.html'
    context_object_name = 'Activities'

    def get_queryset(self): #overided the get_queryset method to show case values of only the logged in user
        # print(self.request.user)
        return Activities.objects.filter(storage_name=None).order_by('-date_user_requested_service')



# view for the delivery guy





class DeliveryActivitiesListView(ListView):

    template_name = 'info/home.html'
    context_object_name = 'Activities'

    def get_queryset(self): #overided the get_queryset method to show case values of only the logged in user
        # print(self.request.user)
        return Activities.objects.filter(delivery_name=self.request.user).order_by('-date_user_requested_service')

class NonDeliveredActivitiesListView(ListView):

    template_name = 'info/home.html'
    context_object_name = 'Activities'

    def get_queryset(self): #overided the get_queryset method to show case values of only the logged in user
        # print(self.request.user)
        return Activities.objects.filter(delivery_name=None).order_by('-date_user_requested_service')











class DetailedActivityView(LoginRequiredMixin, DetailView):
    model = Activities

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activity_current = self.object   # retrive the current activity
        # print(activity_current)
        hash = HashTable.objects.get(activity_id=activity_current.pk)
        # print(hash.hash1)
        context['hash'] = hash
        return context


class NewActivityView(LoginRequiredMixin, CreateView):
    model = Activities
    # fields = ['activity_id', 'pickup_date', 'pickup_location', 'delivery_date', 'delivery_address','number_of_boxes']
    form_class = NewActivityForm
    # permission_required = 'activities.can_create'

    # def get_form(self, form_class=None):
    #     form = super(NewActivityView, self).get_form(form_class)
    #     form.fields['pickup_date'].widget.attrs.update({'class': 'datepicker'})
    #     form.fields['delivery_date'].widget.attrs.update({'class': 'datepicker'})
    #     return form
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

    # def dispatch(self, request, *args, **kwargs):
    #     if self.request.user.user_type =='User':



class PickupActivityViewNew(LoginRequiredMixin, UpdateView):
    model = Activities

    form_class = UpdateActivityPickup
    def form_valid(self, form):
        form.instance.pickup_name = self.request.user
        print(datetime.now())
        form.instance.date_picked_up = datetime.now()
        return super().form_valid(form)


class StorageActivityViewNew(LoginRequiredMixin, UpdateView):
    model = Activities
    form_class = UpdateActivityStorage

    def form_valid(self, form):
        form.instance.storage_name = self.request.user
        return super().form_valid(form)


class DeliveryActivityViewNew(LoginRequiredMixin, UpdateView):
    model = Activities
    form_class = UpdateActivityDelivery

    def form_valid(self, form):
        form.instance.delivery_name = self.request.user
        return super().form_valid(form)




def About(request):
    return render(request, 'info/about.html',{ 'title': 'About Us'})
############ Old new_activity #########
# def new_activity(request):
#     if request.method == 'POST':
#         form = NewActivityForm(request.POST)
#         if form.is_valid():
#             form.save()
#             activities = form.cleaned_data.get('activity_id')
#             print('-------'+username)
#             messages.success(request, f'Account created for {username}! You can now login to access the site ')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})
