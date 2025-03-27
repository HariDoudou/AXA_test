import tempfile
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_word(devis):
    # Créer un document Word
    doc = Document()
    doc.add_heading('Proposition Commerciale', 0)

    # Ajouter les informations du devis dans le document
    doc.add_paragraph(f"Numéro d'opportunité : {devis.num_opportunite}")
    doc.add_paragraph(f"Nom du client : {devis.nom_client}")
    doc.add_paragraph(f"Tarif proposé : {devis.tarif_propose}€")
    doc.add_paragraph(f"Date de création : {devis.date_creation}")

    # Créer un fichier temporaire
    with tempfile.NamedTemporaryFile(delete=False, suffix='.docx', mode='wb') as tmp_file:
        file_path = tmp_file.name
        # Sauver le document dans le fichier temporaire
        doc.save(file_path)

    return file_path

def generate_pdf(devis):
    # Créer un fichier PDF temporaire
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf', mode='wb') as tmp_file:
        file_path = tmp_file.name
        c = canvas.Canvas(file_path, pagesize=letter)

        # Ajouter les informations du devis dans le PDF
        c.drawString(100, 750, "Proposition Commerciale")
        c.drawString(100, 730, f"Numéro d'opportunité : {devis.num_opportunite}")
        c.drawString(100, 710, f"Nom du client : {devis.nom_client}")
        c.drawString(100, 690, f"Tarif proposé : {devis.tarif_propose}€")
        c.drawString(100, 670, f"Date de création : {devis.date_creation}")

        # Sauver le PDF dans le fichier temporaire
        c.save()

    return file_path
