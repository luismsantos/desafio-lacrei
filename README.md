# Desafio Lacre Saúde - Desenvolver uma API para consultas médicas

## Introdução
O desafio da Lacre Saúde é uma API, que foi desenvolvida com Django e Django Rest Framework

## Arquitetura 
> Para esse projeto, três tabelas foram criadas: Medico, Paciente, Consulta.
A tabela "Medico" conta com nome completo, nome social, profissão, endereço, idade.
A tabela "Paciente" conta com nome completo, nome social, endereço, idade.
A tabela "Consulta" herda os dados de o nome do medico da tabela Medico e o nome do paciente da tabela Paciente.
O nome social irá aparecer nas requisições GET.

> Nas views, herdei a classe ModelViewSet, para o desenvolvimento ser mais rápido, já que trás um CRUD completo, mas foi necessário reescrever o método DELETE de todas as views.

> Visando a facilidade, mantive o sqLite.

## Preparando o ambiente
1. Faça o clone do repositório;
2. Acesse a pasta do repositório;
3. Crie um ambiente virtual usando o comando:
  ```
  Com windows:
  python -m venv venv

  Para linux:
  python3 -m venv venv
  ```

4. Ative o ambiente virtual:
  ```
  Com windows:
  venv/Scripts/activate

  Para linux:
  source venv/bin/activate
  ```
5. Instale as dependências com o comando: `pip install -r requirements.txt`;
6. Rode as migrações para o banco de dados com o comando: `python manage.py migrate`;
7. Inicie o servidor com o comando: `python manage.py runserver`;

## Funcionalidades 

### Adicionar médicos
Por meio da requisição POST, é permitido criar novos médicos.
http://localhost:8000/api/medicos/

### Editar médicos
Por meio da requisição PUT, é permitido editar registros já criados
http://localhost:8000/api/medicos/{idMedico}

### Deletar médicos
Por meio da requisição DELETE, é permitido deletar registros
http://localhost:8000/api/medicos/{idMedico}

### Listar todos os médicos
Por meio da requisição GET, é permitido buscar registros
http://localhost:8000/api/medicos/

### Buscar médico por ID
Por meio da requisição GET, é permitido buscar registros (neste caso, registro)
http://localhost:8000/api/medicos/{îdMedico}




