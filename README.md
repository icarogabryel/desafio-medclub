# Desafio Medclub

Nesse repositório, se encontra o código fonte para um backend RESTful que gerencia usuários, pedidos e itens.Foi construído usando Python, Django, Django Rest Framework e Python Dotenv. Sua autenticação é feita via DRF Token.



## Instalação

1. Clone o repositório:

   ```bash
   git clone
   ```

2. Navegue até o diretório do projeto:

   ```bash
    cd desafio-medclub
    ```

3. Crie um ambiente virtual e ative-o:

   ```bash
   python -m .venv venv
   source .venv/bin/activate  # No Windows use: .venv\Scripts\activate
   ```

4. Instale as dependências:

   ```bash
    pip install -r requirements.txt
    ```

5. Configure a variável de ambiente `SECRET_KEY`. Você pode criar um arquivo `.env` na raiz do projeto.

   Exemplo de `.env`:

   ```
   SECRET_KEY=your_secret_key
   ```

6. Aplique as migrações do banco de dados:

   ```bash
   python manage.py migrate
   ```

7. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```
