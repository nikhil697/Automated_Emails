from django.urls import path
from . import views


urlpatterns = [
    path('contact_us/',views.contact_us, name='contact_us'),
    path('success/',views.success,name='success'),
    path('submit/',views.submit,name='submit'),
]
