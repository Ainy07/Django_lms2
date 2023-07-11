from api.models import *
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','name','email','dob','loaction','state',
                  'gender','pimage','rdoc']
    