import requests
from bs4 import BeautifulSoup

print("/ncenctando ao site")
ur1 = "https://www.uo1.com.br"
reposta = requests.get(ur1)

if reposta.status_code == 200:
    print("conexao bem-sucedida!")
else:
    print("conexao mal-sucedida. codigo do erro:", reposta.status_code)
    exit()

print("/analizando a estrutura do site")
    
soup = BeautifulSoup4(reposta.content, 'html.parser')

pagetitle = soup.title.string
print(f" exibindo titulo da pagina: {pagetitle}")

print("\nProcurando os titulos das noticias")
titulos = soup.find_all(["h2" , "h3"])
                                  
print("/n=========titulos enumerados==========")
for i, titulo in enumerate(titulos, 1):
    print(f" {i}.{titulo.get_text(strip = True)}")