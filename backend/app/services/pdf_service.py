from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os


def generate_sanction_pdf(application_id, customer_name, amount):
    os.makedirs("sanctions", exist_ok=True)

    file_path = f"sanctions/loan_{application_id}.pdf"
    c = canvas.Canvas(file_path, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, 800, "LOAN SANCTION LETTER")

    c.setFont("Helvetica", 12)
    c.drawString(100, 760, f"Customer Name: {customer_name}")
    c.drawString(100, 740, f"Application ID: {application_id}")
    c.drawString(100, 720, f"Sanctioned Amount: ₹{amount}")

    c.drawString(100, 680, "Congratulations! Your loan has been approved.")

    c.save()
    return file_path
