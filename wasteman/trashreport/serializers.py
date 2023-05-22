from rest_framework import serializers
from .models import TrashReport

class TrashReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashReport
        fields = '__all__'
