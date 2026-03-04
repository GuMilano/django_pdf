import io
from django.http import FileResponse
from django.views.generic import View
import tempfile
from reportlab.pdfgen import canvas

###################################

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string



class IndexView(View):
    def get(self, request, *args, **kwargs):
        # Cria um arquivo para receber os dados e gerar o PDF
        buffer = io.BytesIO()

        # Criar o arquivo pdf
        pdf = canvas.Canvas(buffer)

        # Insere 'coisas' no PDF
        pdf.drawString(100, 100, "Geek University")

        # Quando acabamos de inserir coisas no pdf
        pdf.showPage()
        pdf.save()

        # Por fim, retornamos o buffer para o início do arquivo
        buffer.seek(0)

        # Faz o download do arquivo em PDF gerado
        #return FileResponse(buffer, as_attachment=True, filename='report.pdf')

        # Abre o PDF direto no navegador
        return FileResponse(buffer, filename='relatorio1.pdf')

class Index2View(View):
    def get(self, request, *args, **kwargs):
        from weasyprint import HTML

        texto = ['Geek University', 'Evolua seu lado geek', 'Programação com Python e Django']
        html_string = render_to_string('relatorio.html', {'texto': texto})

        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
        HTML(string=html_string).write_pdf(target=tmp.name)
        tmp.close()

        return FileResponse(open(tmp.name, "rb"), content_type="application/pdf", as_attachment=True, filename="relatorio2.pdf")


