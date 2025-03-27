from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Devis
from .serializers import DevisSerializer
from django.http import FileResponse, JsonResponse
from .utils import generate_pdf, generate_word

class DevisAction(APIView):
    def get(self, request):
        devis = Devis.objects.all()
        serializer = DevisSerializer(devis, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DevisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DevisExport(APIView):
    def get(self, request, id):
        try:
            type = request.query_params.get('type', 'pdf')
            if type not in ['pdf', 'word']:
                return JsonResponse({'message': 'Type de fichier non supporté'}, status=status.HTTP_400_BAD_REQUEST)
            devis = Devis.objects.get(id=id)        
            
            # Générer les fichiers Word et PDF
            if type == 'word':
                file_path = generate_word(devis)
                suffix = '.docx'
            else:
                file_path = generate_pdf(devis)
                suffix = '.pdf'

            response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename= f"Proposition_commerciale_{devis.num_opportunite}_{devis.date_creation.strftime('%Y%m%d:%H%M%S')}{suffix}")
            return response
        except Devis.DoesNotExist:
            return JsonResponse({'message': 'Devis non trouvé'}, status=status.HTTP_404_NOT_FOUND)