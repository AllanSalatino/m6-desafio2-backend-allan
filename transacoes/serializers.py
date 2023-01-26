from rest_framework import serializers
from .models import Transacao

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = "__all__"


    def create(self, validated_data: dict) -> Transacao:
            
        transacao_obj = Transacao.objects.create(**validated_data)

        return transacao_obj