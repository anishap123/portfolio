
from rest_framework import serializers
from base.models import *

class AboutSerializers(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class ServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class TestimonialSerializers(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'