import requests,sys,os
from bs4 import BeautifulSoup
from urls import getUrl

#Pasta onde irá salvar o arquivo, pega a pasta raiz do Script Python,em seguida defino em qual pasta será
downloadPath = str(sys.path[0])+'/arquivos/' 

urls=getUrl() #Função que faz as leituras dos link no arquivo de texto e retorna uma lista
for url in urls:#for para percorrer a lista
    try:
        print("\nLink Page Pdf: ",url,"\n")
        soup = BeautifulSoup(requests.get(url).text,'lxml')

        #Aqui estamos Fazendo o parser do Html, e buscando pela class page-title, onde é definido o nome do livro ou pdf
        tag_title = str(soup.find("div", {"class" : "page-title"}).getText())
        tag_title = tag_title.replace('\n','')#substituindo o \n (Quebra de linha) para não dar erro quando for salvar o arquivo
        

        tags=soup.find("div", {"class" : "cta-button-container__item"})#Fazendo o parser e buscando pela class onde contém o link de dowload do pdf
        for i in tags.find_all('a',href=True):#percorrendo o html que foi encontrado, e buscando pela tag "a"
            link='http://link.springer.com'+i["href"]#i["href"] é o atributo que está o link do pdf
            
            response = requests.get(link)#aqui realiza um requisição para busar o pdf
            print("Nome Arquivo: ",tag_title)
            print("Link Download PDF: ",link)

            with open(downloadPath+tag_title+'.pdf', 'wb') as f:#aqui será onde iremos criar o arquivo com o path especificado
                f.write(response.content)#aqui salvamos o conteudo da requisição no arquivo criado
    except Exception as e: #caso aconteça algum erro ele entra no except, para não para a execução.
        print("\nOcorreu um erro, ao tentar fazer o download: ",url," Erro",e,"\n\n")

