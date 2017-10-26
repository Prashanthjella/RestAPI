from rest_framework import serializers

from webapp.models import employees


class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model= employees
        fields=('firstname','lastname','emp_id')
        fields = '__all__'