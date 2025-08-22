# Documentação da API

Neste documento, você encontrará informações sobre a API do Desafio MedClub, incluindo detalhes sobre os endpoints disponíveis, formato de requisições/respostas e orientações sobre como utilizar a API.

- [Gerenciamento de Usuários](#gerenciamento-de-usuários)
- [Gerenciamento de Itens](#gerenciamento-de-itens)
- [Gestão de Pedidos](#gestão-de-pedidos)

## Gerenciamento de Usuários

- **Criar novo usuário com nome e senha exclusivos**

    Descrição: Registrar novos usuários. Retorna os dados do usuário criado. O nome de usuário precisa ser único e a senha precisa seguir as regras de complexidade definidas no `settings.py`.

    Endpoint: `registrar/`

    Método: `POST`

    **Corpo da requisição:**

    ```json
    {
    "username": "^w$",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "password": "string"
    }
    ```

    **Corpo da resposta:**

    Código: `201`

    ```json
    {
    "id": 0,
    "username": "^w$",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string"
    }
    ```

- **Autenticar um usuário usando seu nome de usuário e senha**

    Descrição: Permite que usuários existentes façam login. Retorna um token de autenticação.

    Endpoint: `logar/`

    Método: `POST`

    **Corpo da requisição:**

    ```json
    {
        "username": "string",
        "password": "string"
    }
    ```

    **Corpo da resposta:**

    Código: `200`

    ```json
    {
        "token": "string"
    }
    ```

- **Atualizar as informações do perfil de um usuário**

    Descrição: Pega o token de autenticação do usuário e permite que um usuário atualize suas informações de perfil.

    Endpoint: `/usuario/perfil/`

    Método: `PUT`

    **Corpo da requisição:**

    ```json
        {
            "username": "^w$",
            "email": "user@example.com",
            "first_name": "string",
            "last_name": "string"
        }
    ```

    **Corpo da resposta:**

    Código: `200`

    ```json
    {
        "id": 0,
        "username": "^w$",
        "email": "user@example.com",
        "first_name": "string",
        "last_name": "string"
    }
    ```

- **Recupere as informações do perfil de um usuário**

    Descrição: Pega o token de autenticação do usuário. Retorna os dados do usuário.

    Endpoint: `/usuario/perfil/`

    Método: `GET`

    **Corpo da resposta:**

    Código: `200`

    ```json
    {
        "id": 0,
        "username": "^w$",
        "email": "user@example.com",
        "first_name": "string",
        "last_name": "string"
    }
    ```

## Gerenciamento de Itens

- **Crie um novo item com nome e preço**

    Descrição: Permite criação de novos itens. Retorna os dados do item criado.

    Endpoint: `itens/`

    Método: `POST`

    **Corpo da requisição:**

    ```json
    {
        "nome": "string",
        "preco": 0.0
    }
    ```

    **Corpo da resposta:**

    Código: `201`

    ```json
    {
        "id": 0,
        "nome": "string",
        "preco": 0.0
    }
    ```

- **Atualize o nome e o preço de um item**

    Descrição: Permite atualização de itens existentes. Retorna os dados do item atualizado.

    Endpoint: `itens/{id}/`

    Método: `PUT`

    **Corpo da requisição:**

    ```json
    {
        "nome": "string",
        "preco": 0.0
    }
    ```

    **Corpo da resposta:**

    Código: `200`

    ```json
    {
        "id": 0,
        "nome": "string",
        "preco": 0.0
    }
    ```

- **Excluir um item**

    Descrição: Permite a exclusão de um item existente.

    Endpoint: `itens/{id}/`

    Método: `DELETE`

    **Resposta:**

    Código: `204`

- **Recupere uma lista de todos os itens**

    Descrição: Retorna uma lista de todos os itens disponíveis.

    Endpoint: `itens/`

    Método: `GET`

    **Corpo da resposta:**

    Código: `200`

    ```json
    [
        {
            "id": 0,
            "nome": "string",
            "preco": 0.0
        }
    ]
    ```

## Gestão de Pedidos

- **Crie um novo pedido para um usuário, contendo um ou vários itens**

    Descrição: Permite que um usuário crie um pedido com um ou mais itens. Retorna os dados do pedido criado. Usa o token de autenticação do usuário para associar o pedido ao usuário correto.

    Endpoint: `pedidos/`

    Método: `POST`

    **Corpo da requisição:**

    ```json
    {
        "itens": [
        0
        ]
    }
    ```

    **Corpo da resposta:**

    Código: `201`

    ```json
    {
        "id": 0,
        "usuario": 0,
        "itens": [
            0
        ],
    }
    ```

- **Recupere todos os pedidos de um usuário**

    Descrição: Permite que um usuário recupere todos os seus pedidos. Usa o token de autenticação do usuário para filtrar os pedidos.

    Endpoint: `pedidos/`

    Método: `GET`

    **Corpo da resposta:**

    Código: `200`

    ```json
    [
        {
            "id": 0,
            "usuario": 0,
            "itens": [
                0
            ]
        }
    ]
    ```

- **Recupere detalhes de um pedido específico, incluindo os itens**

    Descrição: Permite que um usuário recupere detalhes de um pedido específico, incluindo os itens associados. Usa o token de autenticação do usuário para verificar a propriedade do pedido.

    Endpoint: `pedidos/{id}/`

    Método: `GET`

    **Corpo da resposta:**

    Código: `200`

    ```json
    {
        "id": 0,
        "usuario": 0,
        "itens": [
            0
        ]
    }
    ```
