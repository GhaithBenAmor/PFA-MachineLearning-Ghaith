"""
	Why we add serializers.py : Convert the http request to JSON format
"""
from rest_framework import serializers
from . models import approvals

class approvalsSerializers(serializers.ModelSerializer):
	class Meta:
		model=approvals
		fields='__all__'
