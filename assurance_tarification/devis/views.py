from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Devis
from .serializers import DevisSerializer

# Vue pour récupérer la liste des devis
class DevisList(APIView):
    def get(self, request):
        devis = Devis.objects.all()
        serializer = DevisSerializer(devis, many=True)
        return Response(serializer.data)

# Vue pour créer un nouveau devis
class DevisCreate(APIView):
    def post(self, request):
        serializer = DevisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
