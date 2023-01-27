from .models import Transacao
from .serializers import TransacaoSerializer
from rest_framework import generics
from rest_framework.views import APIView, Request, Response


class TransacaoView(generics.ListCreateAPIView):
    serializer_class = TransacaoSerializer
    queryset = Transacao.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TransacaoDetailView(APIView):
    
    def get(self, request: Request, cpf: str) -> Response:
        transacoes = Transacao.objects.all()

        transacoes_cpf = []

        # Filtra as transações usando o cfp passado na url
        for transacao in transacoes:
            if transacao.cpf == cpf:
                transacoes_cpf.append(transacao)
        
        serializer = TransacaoSerializer(transacoes_cpf, many=True)

        return Response(serializer.data)

