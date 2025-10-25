from django.http import JsonResponse, HttpResponse
from .Pdf.GK_pdf import create_pdf_GK
def status(request):
    return JsonResponse({"status": "ok"}, status=200)

def pdf_download(request):
    pdf_bytes = create_pdf_GK()
    response = HttpResponse(pdf_bytes, content_type="application/pdf")
    # inline prikaz u browseru; za preuzimanje postavi attachment
    response["Content-Disposition"] = 'inline; filename="primer.pdf"'
    return response
