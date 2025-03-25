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

    file_path = f"devis_{devis.num_opportunite}_{devis.date_creation.strftime('%Y%m%d_%H%M%S')}.docx"
    doc.save(file_path)
    return file_path


def generate_pdf(devis):
    file_path = f"devis_{devis.num_opportunite}_{devis.date_creation.strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(file_path, pagesize=letter)
    
    c.drawString(100, 750, f"Proposition Commerciale")
    c.drawString(100, 730, f"Numéro d'opportunité : {devis.num_opportunite}")
    c.drawString(100, 710, f"Nom du client : {devis.nom_client}")
    c.drawString(100, 690, f"Tarif proposé : {devis.tarif_propose}€")
    c.drawString(100, 670, f"Date de création : {devis.date_creation}")
    
    c.save()
    return file_path
