# Bemol Challenge

## 🚀 Começando

Faça o clone do projeto que está no github

no seu terminal digite:

```
git clone https://github.com/dielito2010/OmnichannelBemol.git
```

### 📋 Pré-requisitos

Python3 com pip instalados, verifique conforme seu sistema operacional

```
cd OmnichannelBemol
```

Instalação de requirements.txt

```
pip3 install -r requirements.txt
```

### 🔧 Instalação

O Banco de dados mongo está na nuvem, caso queira usar, precisa criar as variaveis de ambiente conforme seu sistema operacional e ter um cluster no MongoDB Atlas ao qual irá lhe fornecer uma string de conexão que será colocado na váriável de ambiente.

Caso queira usar o banco local, precisa ter MongoDB instalado e com status ativo, vá em Ominichannel/settings.py tem configurações comentadas, só trocar de nuvem para local.

```
python3 manage.py makemigrations
```

Rode o projeto com o comando:

```
python3 manage.py runserver
```

## ⚙️ Executando os testes de usabilidade

Acesse o enderço fornecido no terminal:

```
 http://127.0.0.1:8000
 ```

testes:

1 - Tente fazer login

2 - Tente fazer um cadastro

3 - Tente fazer o logout

### 🔩 Analise os testes de ponta a ponta

Os campos estão fazendo todas as validações corretamente?

CEP válidos?

Emails válidos?

Senhas válidas?

## 📦 Implantação

Todo projeto roda em servidor backend que tenha suporte a Python, pode ser usado localmente ou na nuvem.

## 🛠️ Tecnologias

- [HTML5](https://www.w3schools.com/html/) - HTML5
- [CSS3](https://www.w3schools.com/Css/) - CSS3
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) - Linguagem JavaScript Vanilla.
- [Python](https://www.python.org/downloads/) - Linguagem Python
- [MongoDB](https://www.mongodb.com/) - Banco de dados não relacional para salvar dados de usuário na nuvem.
- [Bootstrap](https://getbootstrap.com/) - framework para estilizar páginas e componentes web.
- [Django](https://www.djangoproject.com/) - Django é uma estrutura web Python de alto nível que incentiva o desenvolvimento rápido.
- [Viacep](https://viacep.com.br/) - API web para buscar e validar ceps.

## 📌 Versão

1.0

## ✒️ Autores

Daniel Antunes Ribeiro

https://danielribeiro.dev.br/

https://www.linkedin.com/in/daniel-antunes-ribeiro/

## 📄 Licença

MIT

---

⌨️ com ❤️ por [Daniel](https://gist.github.com/dielito2010) 😊
