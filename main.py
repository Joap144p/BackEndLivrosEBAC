#API de Livros
#Get, post, put, delete

#Post - Adicionar novos livros(Create)
#Get - Buscar os dados dos livros(Read)
#Put - Atualizar informações dos livros(Update)
#Delete - Deletar informações dos livros(Delete)

#CRUD
#Create
#Read
#Update
#Delete

#Bibliotecas e Classificações
from fastapi import FastAPI, HTTPException
app = FastAPI()

livros = {}

#Mostrando os livros
@app.get("/livros")
def get_livros():
    if not livros:
        return{"message":"Não existe nenhum livro"}
    else:
        return{'livros':livros}

#Adicionando um livro
@app.post('/adiciona')
def post_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: int):
    if id_livro in livros:
        raise HTTPException(status_code=400, detail="Esse livro já existe, meu amigo!")
    else:
        livros[id_livro] = {'nome_livro':nome_livro, 'autor_livro':autor_livro, 'ano_livro':ano_livro}
        return{'message':'Livro adicionado com sucesso'}

#Atualizando algum livro
@app.put('/Atualizar/{id_livro}')
def put_livros(id_livro: int, nome_livro: str, autor_livro: str, ano_livro: int):
    meu_livro = livros.get(id_livro)
    if not meu_livro:
        raise HTTPException(status_code=404, detail='Esse livro não existe!')
    else:
        if nome_livro:
            meu_livro['nome_livro'] = nome_livro
        if autor_livro:
            meu_livro['autor_livro'] = autor_livro
        if ano_livro:
            meu_livro['ano_livro'] = ano_livro
        return{'message':'As informações do seu livros foram atualizadas com sucesso!'}

#Deletando um livro
@app.delete('/Deletar/{id_livro}')
def delete_livro(id_livro: int):
    if id_livro not in livros:
        raise HTTPException(status_code=404, detail='Esse livro não foi encontrado!')
    else:
        del livros[id_livro]
        return{'message':'Seu livro foi deletado com sucesso!'}