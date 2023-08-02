from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('add-contact/',views.addcontact,name = 'add-contact'),
    path('profile/<str:pk>',views.contactprofile,name ='profile' ),
    path('edit-contact/<str:pk>',views.editcontact,name = 'edit-contact'),
    path('delete/<str:pk>',views.deletecontact,name = 'delete')
]