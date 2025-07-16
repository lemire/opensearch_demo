import requests
import re
from colorama import init, Fore, Back, Style

OPENSEARCH_URL = 'http://localhost:9200'
INDEX_NAME = 'pdfs'

def search_keyword(keyword):
    query = {
        "query": {
            "match": {
                "content": keyword
            }
        }
    }
    resp = requests.post(f"{OPENSEARCH_URL}/{INDEX_NAME}/_search", json=query)
    results = resp.json()
    hits = results.get('hits', {}).get('hits', [])
    if not hits:
        print(f"\n{Fore.RED}Aucun résultat trouvé pour :{Style.RESET_ALL}", keyword)
        return
    print(f"\nRésultats pour le mot-clé : {Style.BRIGHT}{keyword}{Style.RESET_ALL}\n")
    for i, hit in enumerate(hits, 1):
        filename = hit['_source']['filename']
        content = hit['_source']['content'].replace('\n', ' ')
        # Cherche le mot-clé (insensible à la casse)
        match = re.search(re.escape(keyword), content, re.IGNORECASE)
        if match:
            start = max(match.start() - 80, 0)
            end = min(match.end() + 80, len(content))
            extrait = content[start:end]
            # Met en surbrillance le mot-clé
            extrait = re.sub(re.escape(keyword), f"{Back.RED}{keyword}{Style.RESET_ALL}", extrait, flags=re.IGNORECASE)
        else:
            extrait = content[:80] + '...'
        print(f"{Fore.BLUE}[{i}] Fichier : {filename}{Style.RESET_ALL}")
        print(f"   {Fore.GREEN}Contexte :{Style.RESET_ALL} {extrait}")
        print(f"{Fore.LIGHTBLACK_EX}{'-' * 60}{Style.RESET_ALL}")

if __name__ == "__main__":
    init(autoreset=True)
    mot_cle = input("Mot-clé à rechercher : ")
    search_keyword(mot_cle)