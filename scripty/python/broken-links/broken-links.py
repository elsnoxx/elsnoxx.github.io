import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.parse import urljoin
import webbrowser

searched_links = []
broken_links = []

# Web on internet testing
BASE_URL = sys.argv[1] if len(sys.argv) > 1 else "https://elsnoxx.github.io"
# Local testing
# BASE_URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:3000/"
# FILE_PATH = "C:/Users/admin/Documents/GitHub/JA-MON-O-03-23/"
FILE_PATH = "C:/Users/ficek/Documents/GitHub/JA-MON-O-03-23/"

print(
    f'Running script for {BASE_URL} and saving the file to: {FILE_PATH}broken-links.html')


def getLinksFromHTML(html):
    def getLink(el):
        return el["href"]
    return list(map(getLink, BeautifulSoup(html, features="html.parser").select("a[href]")))


def find_broken_links(domainToSearch, URL, parentURL):
    is_searchable = (not (URL in searched_links)) and (not URL.startswith("mailto:")) and (not ("javascript:" in URL)) and (
        not URL.endswith(".png")) and (not URL.endswith(".jpg")) and (not URL.endswith(".jpeg"))
    if is_searchable:
        try:
            resetObj = requests.get(URL)
            searched_links.append(URL)
            if(resetObj.status_code == 404):
                broken_links.append({
                    "url": URL,
                    "parent_url": parentURL or 'Home',
                    'message': resetObj.reason
                })
            else:
                if urlparse(URL).netloc == domainToSearch:
                    for link in getLinksFromHTML(resetObj.text):
                        find_broken_links(
                            domainToSearch, urljoin(URL, link), URL)
        except Exception as e:
            print("ERROR: " + str(e))
            searched_links.append(domainToSearch)


find_broken_links(urlparse(BASE_URL).netloc, BASE_URL, "")

# Converting above errors to html file
with open('broken-links.html', 'w') as myFile:
    myFile.write('<html>')
    myFile.write(f'''
        <head>
            <style>
            table {{
                font-family: arial, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }}

            td, th {{
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }}

            tr:nth-child(even) {{
                background-color: #dddddd;
            }}
            h2 {{
                text-align: center;
            }}
            </style>
        </head>
    ''')
    myFile.write('<body>')
    myFile.write(f'<h2>Broken links for site: {BASE_URL}</h2>')
    myFile.write('<table>')
    myFile.write('<tbody>')
    myFile.write(
        '<tr><th>SN</th><th>URL</th><th>Parent URL</th><th>Message</th></tr>')
    for index, link in enumerate(broken_links):
        myFile.write(
            '<tr><td>{0}</td><td> <a href="{1}" style="color:red;" target="_blank">{1}</a></td><td> <a href="{2}" target="_blank">{2}</a></td><td>{3}</td></tr>'.format(index+1, link['url'], link['parent_url'], link['message']))

    myFile.write('</tbody>')
    myFile.write('</table>')
    myFile.write('</body>')
    myFile.write('</html>')