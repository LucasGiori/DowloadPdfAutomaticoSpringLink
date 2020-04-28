import requests
from bs4 import BeautifulSoup
from urls import getUrl

urls=getUrl()
for i in urls:
    try:
        print("\nLink Page Pdf: ",i,"\n")
        url = i#'http://link.springer.com/openurl?genre=book&isbn=978-0-306-48048-5'
        soup = BeautifulSoup(requests.get(url).text,'lxml')


        tag_title = str(soup.find("div", {"class" : "page-title"}).getText())
        tag_title = tag_title.replace('\n','')
        #page = soup.find('p')
        #print(tag_title)

        tags=soup.find("div", {"class" : "cta-button-container__item"})
        for i in tags.find_all('a',href=True):
            link='http://link.springer.com'+i["href"]
            name_arquivo = i["href"].split('/')[-1]
            response = requests.get(link)
            print("Nome Arquivo: ",tag_title)
            print("Link Download PDF: ",name_arquivo)

            with open(tag_title+'.pdf', 'wb') as f:
                f.write(response.content)
    except:
        print("\nOcorreu um erro, ao tentar fazer o download: ",i,"\n\n")
