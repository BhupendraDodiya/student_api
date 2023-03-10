from django.urls import path,include
from .models import Student
from .serializer import StudentSerializer
from .viewset import StudentViewset
from rest_framework import routers

res = routers.DefaultRouter()
res.register('stud',StudentViewset)
urlpatterns = [
    path('',include(res.urls))
]
