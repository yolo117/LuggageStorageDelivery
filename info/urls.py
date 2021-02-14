from django.urls import path
from . import views
from info.views import (
UserActivitiesListView,
 NewActivityView,
  HomePageDispatchView,
  DetailedActivityView,
   PickupActivityViewNew,
   PickupActivityListView,
   StorageActivityViewNew,
   StorageActivitiesNonAcceptedListView,
   StorageActivityViewNew,
   NonDeliveredActivitiesListView,
   DeliveryActivityViewNew
)

urlpatterns = [
    path('', HomePageDispatchView.as_view(), name='info-home'),
    path('info/pickuppending/', PickupActivityListView.as_view(), name='unaccepted-activity'),
    path('info/deliverypending/', NonDeliveredActivitiesListView.as_view(), name='nondeliver-activity'),
    path('info/storeluggage/', StorageActivitiesNonAcceptedListView.as_view(), name='store-luggage'),
    path('detail/<int:pk>/', DetailedActivityView.as_view(), name='activity-detail'),
    path('info/new/', NewActivityView.as_view(), name='new-order'),
    path('info/<int:pk>/pickedupnew/', PickupActivityViewNew.as_view(), name='pic-new-order'),
    path('info/<int:pk>/storednew/', StorageActivityViewNew.as_view(), name='store-order'),
    path('info/<int:pk>/delivernew/', DeliveryActivityViewNew.as_view(), name='deliver-order'),
    path('about/', views.About, name='info-about'),
]
