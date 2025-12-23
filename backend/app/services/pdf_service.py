from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from datetime import date


def generate_sanction_pdf(
    application_id: int,
    customer_name: str,
    loan_amount: float,
    tenure_months: int,
    interest_rate: float = 12.0
):
    os.makedirs("sanctions", exist_ok=True)

    file_path = f"sanctions/loan_sanction_{application_id}.pdf"
    c = canvas.Canvas(file_path, pagesize=A4)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "Loan Sanction Letter")

    c.setFont("Helvetica", 11)
    c.drawString(50, 760, f"Date: {date.today()}")
    c.drawString(50, 730, f"Applicant Name: {customer_name}")
    c.drawString(50, 700, f"Application ID: {application_id}")

    c.drawString(50, 660, f"Loan Amount Approved: ₹{loan_amount}")
    c.drawString(50, 630, f"Tenure: {tenure_months} months")
    c.drawString(50, 600, f"Interest Rate: {interest_rate}% per annum")

    c.drawString(
        50,
        550,
        "We are pleased to inform you that your loan application has been approved."
    )

    c.drawString(
        50,
        520,
        "Please contact LoanEase Finance for further disbursement formalities."
    )

    c.drawString(50, 480, "Regards,")
    c.drawString(50, 460, "LoanEase Finance Team")

    c.showPage()
    c.save()

    return file_path
