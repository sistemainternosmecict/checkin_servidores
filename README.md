# Software de checkin da festa do servidor

Pequeno software de checkin para a festa dos servidores de saquarema 2025. Foi criado com o intuito de realizar duas funções básicas.

Na primeira página:
- Buscar servidores pelo CPF, validar e registrar a passagem pela entrada.

Na segunda página:
- Buscar número da pulseira, no caso de cortesia para registrar nome completo, cpf e registrar a passagem pela entrada.

## Como rodar o servidor localmente?

Coloque o arquivo da lista em formato .csv na pasta raiz (a pasta do main) do projeto com o nome: **"data.csv"** e rode o servidor com os seguintes comandos:

## Windows
```bash
$ py -m venv venv
$ source venv/Scripts/activate
$ py main.py
```

## Mac/Linux
```bash
$ python3 -m venv venv
$ source venv/Scripts/activate
$ python3 main.py
```

No navegador dos smartphones, acesse o ip do servidor indicado no terminal.

---
## Desenvolvimento
Autor: Thyéz de Oliveira Monteiro (SMECICT / Sala 25)