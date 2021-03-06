from rest_framework import serializers
from datetime import datetime

from main.models import User, Workshop, Enrollment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class WorkshopSerializer(serializers.ModelSerializer):
    start_date_time = serializers.DateTimeField(read_only=True, format="%A %m-%d-%Y at %I:%M %p")
    end_date_time = serializers.DateTimeField(read_only=True, format="%A %m-%d-%Y at %I:%M %p")
    class Meta:
        model = Workshop
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
