# PYPDF2 com merger - "Unir arquivos"

# importar a biblioteca PDFWriter
from pathlib import Path
from PyPDF2 import PdfReader,PdfWriter,PdfMerger

# instancia raiz para criar Pastas dentro do VSCode 
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'Arquivos_novos '

VERBOS_INGLES = PASTA_ORIGINAIS / 'C:\\Users\\blaya\\OneDrive\\Documentos\\Cursos\\San Filipe\\Ingles\\Verbs Irregulares.pdf'

# instancia para receber novos arquivos usando mkdir

PASTA_NOVA.mkdir(exist_ok=True)

# Instancia que recebe o PdfReader e ler 
reader = PdfReader(VERBOS_INGLES)

page0 = reader.pages[0]

imagem0 = page0.images[0]

# writer - daqui para baixo


# for com i "contador" para inumerar cada pagina e criar varias paginas pdf

for i, page in enumerate (reader.pages):
    writer = PdfWriter()   
    with open(PASTA_NOVA / f' page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)

# Merger - daqui para baixo

files [

PASTA_NOVA / ' page0.pdf',
PASTA_NOVA / ' page1.pdf',

    
]
merger= PdfMerger()

for file in files: 
    merger.append(file)

merger.write(PASTA_NOVA / 'Pagina5.pdf')
merger.close()

