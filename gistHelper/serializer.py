from rest_framework import serializers

from gistHelper.models import Mealplan


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mealplan
        fields = '__all__'
