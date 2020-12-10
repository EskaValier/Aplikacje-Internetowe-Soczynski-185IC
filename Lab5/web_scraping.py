import requests
from bs4 import BeautifulSoup

URL = 'http://127.0.0.1:8000'
page = requests.get(URL)

# soup = BeautifulSoup(page.content, 'html.parser')
soup = BeautifulSoup(page.content, 'lxml')

# Wyswietla calego html strony
# print(soup)

print('HTML Title: ', soup.title.text)
posts = soup.find_all('div', class_='post')

for el in posts:
    title_el = el.h1
    content_el = el.find('p')
    create_date_el = el.find('div', class_='date')
    link_el = el.a['href']

    # wypisanie z tagami HTML
    # print(title_el, end='\n')

    # wypisanie bez tagów HTML
    print('Creation date: ', create_date_el.text)
    print('Post title: ',title_el.text, end='\n')
    print(content_el.text, end='\n'*2)
    print('Link do strony z detalem postu: ',URL + link_el)

#nazwa klasy / klas pierwszego znalezionego div'a
div_Class = soup.div['class']
print(div_Class)

#zmiana zawartości elementu
footer = soup.find('div', class_='page-footer')
print("Old footer:\n", footer)
newFooter = BeautifulSoup("<footer> stopka </footer>", 'lxml')

footer.find('button').replace_with(newFooter)
print("New footer:\n", footer)
