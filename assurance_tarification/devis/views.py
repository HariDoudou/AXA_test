from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Devis
from .serializers import DevisSerializer
from django.http import JsonResponse
from .utils import generate_pdf, generate_word

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
            devis = serializer.save()
            
            # Générer les fichiers Word et PDF
            word_file = generate_word(devis)
            pdf_file = generate_pdf(devis)
            
            # Retourner les chemins des fichiers générés
            return JsonResponse({
                'devis': serializer.data,
                'word_file': word_file,
                'pdf_file': pdf_file
            }, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)