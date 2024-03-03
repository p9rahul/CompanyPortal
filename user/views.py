""" 
Doc string : Views for user API
# CreateAPIView handels HTTP post request for creating objects in DB
"""
from rest_framework import generics
from user.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    """ Create a new user in the system. """
    serializer_class =UserSerializer
