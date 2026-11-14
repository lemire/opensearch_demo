import os
from urllib.parse import quote

import requests
from pdfminer.high_level import extract_text

OPENSEARCH_URL = 'http://localhost:9200'
INDEX_NAME = 'pdfs'
DATA_DIR = 'data'

def index_pdf(file_path):
    text = extract_text(file_path)
    doc = {
        'filename': os.path.basename(file_path),
        'content': text
    }
    # Le nom du fichier sert d'identifiant : relancer le script remplace
    # les documents existants au lieu de créer des doublons.
    doc_id = quote(os.path.basename(file_path), safe='')
    resp = requests.put(f"{OPENSEARCH_URL}/{INDEX_NAME}/_doc/{doc_id}", json=doc)
    print(f"Indexé {file_path}: {resp.status_code}")

if __name__ == "__main__":
    # Créer l'index (optionnel, sinon auto-créé)
    requests.put(f"{OPENSEARCH_URL}/{INDEX_NAME}")
    for fname in os.listdir(DATA_DIR):
        if fname.endswith('.pdf'):
            index_pdf(os.path.join(DATA_DIR, fname))
