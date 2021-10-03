# bookstore-services

Serviços do backend do [bookstore](https://github.com/victormt4/bookstore)

## Documentação da API disponível em

[https://bookstore-services.herokuapp.com/](https://bookstore-services.herokuapp.com/)

## Comandos para rodar projeto

### Utilizando o [poetry](https://python-poetry.org/)

### `poetry install`

Para instalar as dependências necessárias

### `poetry run flask start`

Roda o projeto em modo de desenvolvimento no [http://localhost:5000](http://localhost:5000)

### Utilizando o [Docker](https://docs.docker.com/)

###`docker build -t <NOME_IMAGEM> .`

Para gerar uma build da imagem a partir do Dockerfile do projeto

###`docker run -p 5000:5000 -v $PWD:/var/bookstore-services <NOME_IMAGEM>`

Para inicializar o servidor da aplicação dentro de um container, em modo de desenvolvimento no endereço [http://localhost:5000](http://localhost:5000)


###`bash start-dev-server.sh`

Script para executar os comandos do docker citados acima

