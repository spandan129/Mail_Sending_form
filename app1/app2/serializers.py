from rest_framework import serializers

class ContactFormSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()
    message = serializers.CharField()
