from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from . models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = userdata
        fields = ['username', 'fname','lname','password','email','phone','country','DOB']



