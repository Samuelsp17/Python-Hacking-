import socket

dominio = "google.com"

# Lê todos os nomes do arquivo e remove os espaços em branco (como quebras de linha)
with open("/Emuneração_dns/subdomains-1000.txt") as arquivo:
    nomes = [linha.strip() for linha in arquivo]

# Tenta resolver o DNS de cada subdomínio e imprime o IP, caso exista
for nome in nomes:
    DNS = f"{nome}.{dominio}"  # Usando f-string para montar o endereço DNS
    try:
        ip = socket.gethostbyname(DNS)
        print(f"{DNS}: {ip}")
    except socket.gaierror:
        continue  # Ignora erros para subdomínios que não existem
