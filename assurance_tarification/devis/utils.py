<<<<<<< HEAD
import os
=======
>>>>>>> 23c61299005c76e4390916c8a20a70918a83672e
import tempfile
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_word(devis):
    doc = Document()

    doc.add_heading('Proposition Commerciale', 0)

    doc.add_paragraph(f"Numéro d'opportunité : {devis.num_opportunite}")
    doc.add_paragraph(f"Nom du client : {devis.nom_client}")
    doc.add_paragraph(f"Tarif proposé : {devis.tarif_propose}€")
    doc.add_paragraph(f"Date de création : {devis.date_creation}")

    with tempfile.NamedTemporaryFile(delete=False, suffix='.docx', mode='wb') as tmp_file:
        file_path = tmp_file.name
<<<<<<< HEAD
        try:
            doc.save(file_path)
        except Exception as e:
            os.remove(file_path)  # Supprimer le fichier temporaire en cas d'erreur
            raise Exception(f"Erreur lors de la sauvegarde du fichier Word: {e}")

=======
        doc.save(file_path)
>>>>>>> 23c61299005c76e4390916c8a20a70918a83672e
    return file_path


def generate_pdf(devis):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf', mode='wb') as tmp_file:
        file_path = tmp_file.name
<<<<<<< HEAD
        
        try:
            # Création du PDF avec reportlab
            c = canvas.Canvas(file_path, pagesize=letter)
            
            # Ajout du contenu dans le PDF
            c.drawString(100, 750, "Proposition Commerciale")
            c.drawString(100, 730, f"Numéro d'opportunité : {devis.num_opportunite}")
            c.drawString(100, 710, f"Nom du client : {devis.nom_client}")
            c.drawString(100, 690, f"Tarif proposé : {devis.tarif_propose}€")
            c.drawString(100, 670, f"Date de création : {devis.date_creation}")
            
            c.save()
        except Exception as e:
            os.remove(file_path)  # Supprimer le fichier temporaire en cas d'erreur
            raise Exception(f"Erreur lors de la génération du fichier PDF: {e}")
    
=======
        c = canvas.Canvas(file_path, pagesize=letter)
        
        c.drawString(100, 750, f"Proposition Commerciale")
        c.drawString(100, 730, f"Numéro d'opportunité : {devis.num_opportunite}")
        c.drawString(100, 710, f"Nom du client : {devis.nom_client}")
        c.drawString(100, 690, f"Tarif proposé : {devis.tarif_propose}€")
        c.drawString(100, 670, f"Date de création : {devis.date_creation}")
        
>>>>>>> 23c61299005c76e4390916c8a20a70918a83672e
    return file_path
