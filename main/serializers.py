from rest_framework import serializers
from .helper import check_formula
from .models import Logger

class FormulaValidationSerializer(serializers.Serializer):
    formula = serializers.CharField(max_length=255, required=True)

    
    def validate_formula(self, formula):
        value = check_formula(formula)
        if value:
            return value
        raise serializers.ValidationError


class LoggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logger
        fields = '__all__'