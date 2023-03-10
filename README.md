# bookstore-services

Serviços do backend do [bookstore](https://github.com/victormt4/bookstore)

## Instruções para rodar o projeto localmente

### Requisitos na máquina do host

* [Docker](https://docs.docker.com/get-started/)
* [Docker Compose](https://docs.docker.com/compose/)

### Variáveis de ambiente

Copiar o .env.example para .env e definir a variável "FLASK_SECRET_KEY" com uma chave aleatória, ela serve para
criptografar o cookie de sessão do Flask

### Comandos para inicializar aplicação

`docker compose up`

### Para criar as tabelas do banco

`docker compose exec app flask db upgrade`

### Para inserir dados de testes no banco

`docker compose exec app flask seed`
