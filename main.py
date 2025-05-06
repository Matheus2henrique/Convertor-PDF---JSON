import PyPDF2
import json

# Função para extrair texto do PDF
def extrair_texto_pdf(pdf_path):
    with open(pdf_path, "rb") as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)
        texto = ""

        for pagina in range(len(leitor_pdf.pages)):
            pagina_pdf = leitor_pdf.pages[pagina]
            texto += pagina_pdf.extract_text()

    return texto

# Função para estruturar o conteúdo em JSON
def estruturar_json(texto):
    dados_json = {}
    paginas = texto.split("\n\n")  # Supondo que cada nova página no PDF tenha um espaço em branco entre elas

    for i, pagina in enumerate(paginas):
        dados_json[f"pagina_{i + 1}"] = pagina

    return dados_json

# Função principal para processar e salvar o arquivo JSON
def pdf_para_json(pdf_path, json_path):
    texto_pdf = extrair_texto_pdf(pdf_path)
    estrutura_json = estruturar_json(texto_pdf)

    with open(json_path, "w", encoding="utf-8") as arquivo_json:
        json.dump(estrutura_json, arquivo_json, ensure_ascii=False, indent=4)

    print(f"Arquivo JSON salvo em {json_path}")

# Caminho do seu arquivo PDF e onde deseja salvar o JSON
pdf_path = r"C:\Users\token\Downloads\livro\Dom_Casmurro-Machado_de_Assis.pdf"  # Caminho do PDF
json_path = r"C:\Users\token\Downloads\livro\Dom_Casmurro_Machado_de_Assis.json"  # Caminho para salvar o arquivo JSON

# Chamada da função
pdf_para_json(pdf_path, json_path)
