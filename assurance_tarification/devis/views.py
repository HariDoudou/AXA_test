from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Devis
from .serializers import DevisSerializer
from django.http import FileResponse
from .utils import generate_pdf, generate_word

class DevisAction(APIView):
    def get(self, request):
        devis = Devis.objects.all()
        serializer = DevisSerializer(devis, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print('request.data : ', request.data)
        serializer = DevisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DevisExport(APIView):
    def get(self, request, id):
        try:
            # Récupérer le type de fichier souhaité (par défaut PDF)
            type = request.query_params.get('type', 'pdf')
            
            # Vérifier que le type est supporté (PDF ou Word)
            if type not in ['pdf', 'word']:
                return Response({'message': 'Type de fichier non supporté'}, status=status.HTTP_400_BAD_REQUEST)

            # Récupérer le devis en fonction de l'ID
            devis = Devis.objects.select_related('adresse').get(id=id)
            
            # Générer le fichier Word ou PDF
            if type == 'word':
                file_path = generate_word(devis)
                suffix = '.docx'
            else:
                file_path = generate_pdf(devis)
                suffix = '.pdf'

            # Créer le nom du fichier dynamique avec le numéro d'opportunité et la date
            filename = f"Proposition_commerciale_{devis.num_opportunite}_{devis.date_creation.strftime('%Y%m%d_%H%M%S')}{suffix}"
            
            # Retourner la réponse avec le fichier et l'en-tête Content-Disposition
            response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
            return response

        except Devis.DoesNotExist:
            return Response({'message': 'Devis non trouvé'}, status=status.HTTP_404_NOT_FOUND)
