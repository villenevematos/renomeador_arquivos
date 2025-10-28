import os

extensoes_documentos = ['.pdf', '.PDF', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx']
extensoes_imagens = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
extensoes_videos = ['.mp4', '.avi', '.mov', '.mkv', '.flv']
extensoes_musicas = ['.mp3', '.wav', '.aac', '.flac']
extensoes_comprimidos = ['.zip', '.rar', '.7z', '.tar', '.gz']
extensoes_programas = ['.exe', '.msi', '.dmg', '.pkg', '.py', '.ics', '.epub']

# 🔧 Dicionário que agrupa as extensões por categoria
# Isso permite iterar de forma mais organizada e evitar repetição de código
categorias = {
    "documentos": extensoes_documentos,
    "imagens": extensoes_imagens,
    "videos": extensoes_videos,
    "musicas": extensoes_musicas,
    "comprimidos": extensoes_comprimidos,
    "programas": extensoes_programas
}

categoria, extensoes = categorias.popitem()

# Caminho da pasta de categorias
caminho_pasta_categorias = os.path.expanduser(f'~\Downloads\{categoria}')

# Contentúdo atual da pasta de categorias
lista_conteudo_categorias = os.listdir(caminho_pasta_categorias)    

# 🔁 Percorre todos os arquivos categorizados
for conteudo in lista_conteudo_categorias:
    for extensao in extensoes:
        if conteudo.endswith(extensao):  # ✅ Usa endswith para evitar falsos positivos
            print(f'Arquivo ({conteudo}) é uma {extensao}.')

            # 📁 Define o caminho da pasta correspondente à extensão
            caminho_pasta_extensao = os.path.join(caminho_pasta_categorias, extensao)

            # 📄 Lista todos os arquivos da pasta
            lista_documentos = os.listdir(caminho_pasta_extensao)

            # 🔢 Inicializa contador para nomear sequencialmente
            contador = 1

            for documento in lista_documentos:
                print(f'Renomeando {documento}...')

                # 🧠 Garante que o arquivo tenha a extensão correta
                if documento.endswith(extensao):
                    nome_antigo = os.path.join(caminho_pasta_extensao, documento)
                    nome_novo = os.path.join(caminho_pasta_extensao, f'{categoria}_{contador}{extensao}')

                    # 🔄 Renomeia o arquivo
                    os.rename(nome_antigo, nome_novo)
                    contador += 1
