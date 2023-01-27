# PASSO A PASSO PARA RODAR O APP

# Abra o terminal e siga os passos:

1 - python -m venv venv

2 - source venv/bin/activate

3 - pip install -r requirements.txt

4 - python manage.py makemigrations

5 - python manage.py migrate

6 - python manage.py runserver

7 - Abrir uma nova aba no terminal

8 - python index.py

9 - digite o endereço do arquivo CNAB(ex: /home/fulano/CNAB.txt)

# Os dados seram salvos no db.sqlite3

# ROTAS DISPONIVEIS:

POST - http://127.0.0.1:8000/api/trasacoes/

GET - http://127.0.0.1:8000/api/trasacoes/ - Lista todas as transações

GET - http://127.0.0.1:8000/api/trasacoes/stg:cpf/ - Lista todas as transaçoes de uma determinada pessoa
