
def getUrl():
    with open('lista.txt','r') as r:
        conteudo = r.readlines()
        #conteudo = conteudo.split('\n')
        return conteudo
