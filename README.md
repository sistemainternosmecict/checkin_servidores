# Software de checkin da festa do servidor

Pequeno software de checkin para a festa dos servidores de saquarema 2025. Foi criado com a intenção de realizar duas funções básicas.

Na primeira página:
- Buscar servidores pelo CPF, validar e registrar a passagem pela entrada.

Na segunda página:
- Buscar número da pulseira, no caso de cortesia para registrar nome completo, cpf e registrar a passagem pela entrada.

## Como rodar o servidor localmente?

Na planilha do drive, insira uma nova coluna a direita da última com o título "validado".

É preciso baixar o arquivo csv dessa planilha de base. O app está pronto para ler as colunas como estão lá, incluindo a coluna "validado".

Coloque o arquivo da lista em formato .csv na pasta raiz (a pasta do main) do projeto com o nome: **"data.csv"** e rode o servidor com os seguintes comandos:

## Windows
```bash
# Crie o ambiente virtual venv
$ py -m venv venv

# Ative-o
$ source venv/Scripts/activate

# Instale as dependências do projeto
$ pip install -r requirements.txt

# Rode o arquivo principal para iniciar o servidor
$ py main.py
```

## Mac/Linux
```bash
# Crie o ambiente virtual venv
$ python3 -m venv venv

# Ative-o
$ source venv/Scripts/activate

# Instale as dependências do projeto 
$ pip install -r requirements.txt

# Rode o arquivo principal para iniciar o servidor
$ python3 main.py
```

## Como acessar o sistema após rodar o servidor?

No navegador dos smartphones, acesse o ip do servidor indicado no terminal.

Exemplo:
http://[ip_do_servidor]:5000


---
## Desenvolvimento

Autor: Thyéz de Oliveira Monteiro (Sala 25)

Pedido: 16/10/2025

Conclusão: 21/10/2025

### SMECICT - Secretaria Municipal de Educação, Cultura, Inclusão, Ciência e Tecnologia 