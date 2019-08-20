# BankApi

### Tecnologias utilizadas:
-   Python 3.7
-   Flask
-   Gunicorn
-   Swagger-codegen


Para testar as requisições, é possivel importar o swagger.yaml no postman, para isso va em File, Import (ctrl+o) e aponte para o arquivo yaml ou para o link que o servico devolve o yaml (url/swagger.yaml)

O postman ira criar uma collection com as requisições presentes no arquivo.

Ao subir o servico, ele ficara acessilvel no ip 127.0.0.1:5000.

## Montagem ambiente:

Utilizando o  conda, monte o ambiente a partir do arquivo:

`conda env create -f environment.yml --name bankApi`

ou Utilizando o pip

`pip install -r requirements.txt`


## Para executar a api:

Utilizando o docker:

execute o script build.sh, ele ira montar um servidor nginx, o servico e ummongo proprio.


Para executar diretamente no python e necessario um mongo local, ou especifique a variavel de ambiente MONGO_URI, exemplo:

`export MONGO_URI=mongodb://127.0.0.1:27017`

para executar a aplicacao:

`python app.py`

ou, utilizando o gUnicorn:

`gunicorn --bind 0.0.0.0:5000 wsgi:app --worker-class=gevent`