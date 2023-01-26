# PASSO A PASSO PARA RODAR O APP

# Abra o terminal e siga os passos:

1 - pip install -r requirements.txt

2 - python manage.py migrate

3 - python manage.py runserver

4 - Abrir uma nova aba no terminal

5 - python index.py

6 - digite o endereço do arquivo CNAB(ex: /home/fulano/CNAB.txt)

# Os dados seram salvos no db.sqlite3

# ROTAS DISPONIVEIS:

POST - http://127.0.0.1:8000/api/trasacoes/

GET - http://127.0.0.1:8000/api/trasacoes/ - Lista todas as transações

GET - http://127.0.0.1:8000/api/trasacoes/stg:cpf/ - Lista todas as transaçoes de uma determinada pessoa
