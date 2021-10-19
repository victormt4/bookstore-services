# bookstore-services

Serviços do backend do [bookstore](https://github.com/victormt4/bookstore)

## Documentação da API disponível em

[https://bookstore-services.herokuapp.com/](https://bookstore-services.herokuapp.com/)

## Instruções para rodar o projeto localmente

### Requisitos na máquina do host

* [Docker](https://docs.docker.com/get-started/)
* [Docker Compose](https://docs.docker.com/compose/)

### Variáveis de ambiente

Copiar o .env.example para .env e definir a variável "FLASK_SECRET_KEY" com uma chave aleatória, ela serve para
criptografar o cookie de sessão do Flask

### Comandos para inicializar aplicação

`bash start-dev-server.sh`

Irá gerar uma build do projeto, instalar as dependências da aplicação e inicializar os containers necessários

### Comandos para rodar os testes automatizados

`bash run-tests.sh`

Irá subir os containers da aplicação e rodar os testes utilizando o pytest.

`docker-compose exec app poetry run pytest`

Utilize esse comando caso os containers já estejam em execução pelo "start-dev-server.sh"