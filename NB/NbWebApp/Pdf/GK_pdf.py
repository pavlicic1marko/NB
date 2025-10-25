from fpdf import FPDF

def create_pdf_GK():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(0, 10, "Hello PDF iz Django view-a", ln=True)

    # generiši PDF u memoriji
    df_bytes = bytes(pdf.output(dest="S"))  # fpdf2 vraća str, pretvori u bytes


    return df_bytes