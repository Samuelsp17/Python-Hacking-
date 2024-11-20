import requests

def check_directories(domain, wordlist_path):
    """
    Verifica a existência de subdiretórios em um domínio a partir de uma wordlist.
    """
    try:
        with open(wordlist_path, "r") as file:
            directories = file.read().splitlines()
    except FileNotFoundError:
        print(f"Wordlist não encontrada: {wordlist_path}")
        return

    print(f"Verificando subdiretórios em: {domain}")
    for directory in directories:
        url = f"{domain}/{directory}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"Subdiretório encontrado: {url} -> {response.status_code}")
        except requests.RequestException:
            pass
if __name__ == "__main__":
    # URL do site base
    domain = "https://google.com"
    
    # Caminho para a wordlist
    wordlist_path = "subdirectory.txt"
    
    check_directories(domain, wordlist_path)
