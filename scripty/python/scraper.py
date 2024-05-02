import requests

url = 'https://www.alphaspread.com/security/nasdaq/sofi/analyst-estimates'
response = requests.get(url)
html_content = response.text

# Otevřete soubor pro zápis
with open("test.html", "w", encoding="utf-8") as file:
    # Zapíše obsah HTML do souboru
    file.write(html_content)

print("Obsah byl uložen do souboru 'test.html'.")
