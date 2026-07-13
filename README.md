# Sistema de Gerenciamento de Tarefas

## Objetivo

Desenvolver um sistema web para gerenciamento de tarefas utilizando conceitos de Engenharia de Software, permitindo cadastrar, visualizar, editar e excluir tarefas.

## Escopo

O projeto tem como objetivo implementar um CRUD de tarefas utilizando Python e Flask, aplicando práticas de versionamento, testes automatizados e integração contínua.

## Metodologia Ágil

Foi utilizada a metodologia Kanban para organização das atividades, utilizando o GitHub Projects para controle das tarefas durante o desenvolvimento.

## Tecnologias

- Python
- Flask
- HTML
- Bootstrap
- Pytest
- GitHub
- GitHub Actions

## Como executar

1. Criar o ambiente virtual:

```bash
python -m venv venv
```

2. Ativar o ambiente:

Windows:

```bash
.\venv\Scripts\Activate.ps1
```

3. Instalar as dependências:

```bash
pip install -r requirements.txt
```

4. Executar o sistema:

```bash
python app.py
```

## Testes

Para executar os testes:

```bash
pytest
```

## Mudança de Escopo

Inicialmente o projeto contemplava apenas um CRUD básico para gerenciamento de tarefas.

Durante o desenvolvimento foi adicionada a funcionalidade de **priorização das tarefas**, visando melhorar a organização das atividades dos usuários, simulando uma alteração de escopo comum em projetos ágeis.

## Mudança de Escopo

Durante o desenvolvimento foi adicionada uma melhoria ao sistema.

Agora o usuário pode informar a prioridade da tarefa utilizando uma identificação como:

- [Alta]
- [Média]
- [Baixa]

Essa alteração foi registrada no Kanban e no histórico de commits.