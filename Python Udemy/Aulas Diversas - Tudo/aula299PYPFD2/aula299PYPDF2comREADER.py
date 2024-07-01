# PYPDF2 com PDFReader " Le PDF"

"""

PYPDF2
É uma biblioteca poderosa para manipulação de arquivo PDF, 
que permite ler, manipular, dividir, juntar , recortar, transformar, 
escrever e unir e criptografar em PDF. Assim como adicionar 
anotações , transformar páginas, extrair texto e imagens e 
manipular metadados.  

OBS: Sempre por boa pratica criar uma pasta e colocar 
os arquivos ali dentro. 

e criar uma main.py para realizar atividades 

"""
# importar a biblioteca Reader
from pathlib import Path
from PyPDF2 import PdfReader

# instancia raiz para criar Pastas dentro do VSCode 
PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'Arquivos_novos '

VERBOS_INGLES = PASTA_ORIGINAIS / 'Verbos_irregulares.pdf'

# instancia para receber novos arquivos usando mkdir

PASTA_NOVA.mkdir(exist_ok=True)

# Instancia que recebe o PdfReader
reader = PdfReader(VERBOS_INGLES)

# For para ver a quantidade de paginas

for page in reader.pages:
    print(page)

