"""
Doc string - serializers for the user API view.
serializers - are a way to convert object to or from python object, 
 it takes Json input validate input to secure and correct then convert to python object or
 in model actual DB.

"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """   serializer for user object. 
    # Meta class - here we tell Django rest framework the model and the fileds to pass to serializer ,
        serialzer need to know model it is representing
    # Overite the create method 
    # Define models in serialzer
    """
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password' : {'write_only': True, 'min_length':5}}

    def create(self, validated_data):
        """ create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
    