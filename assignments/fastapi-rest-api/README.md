# ⚙️ Construindo APIs REST com FastAPI

## 🎯 Objetivo

Nesta tarefa você vai construir uma API REST simples usando o framework FastAPI. O objetivo é aprender a definir rotas, usar modelos Pydantic para validação, e executar o servidor com Uvicorn.

## 📝 Descrição

Implemente uma pequena API para gerenciar recursos (por exemplo: itens, tarefas ou usuários) com operações CRUD básicas (Create, Read, Update, Delete). A API deve usar modelos Pydantic para validar payloads e retornar respostas JSON.

## ✅ Requisitos mínimos

- Criar endpoints REST para criar, listar, recuperar por id, atualizar e deletar o recurso.
- Usar modelos Pydantic para validação de entrada e documentação automática.
- Manter os dados em memória (por exemplo, um dicionário) — não é necessário banco de dados para esta tarefa.
- Documentação automática disponível em `/docs` (Swagger) e `/redoc`.
- Instruções claras de como executar o servidor localmente (uvicorn).

## 🔧 Starter code / Como começar

Use o arquivo `starter-code.py` na mesma pasta como ponto de partida. Requer Python 3.8+. Instale dependências com:

```
pip install -r requirements.txt
```

Execute localmente com:

```
uvicorn starter-code:app --reload
```

A API estará disponível em `http://localhost:8000` (Swagger UI: `http://localhost:8000/docs`).

## 📚 Melhoria/Extra (opcional)

- Persistir dados em um arquivo JSON simples ou usar SQLite.
- Adicionar testes automatizados com `pytest` para os endpoints.
- Implementar autenticação simples (token) para rotas protegidas.
- Validar e documentar códigos de resposta HTTP apropriados.

## Arquivos nesta pasta

- `starter-code.py` — servidor FastAPI mínimo com endpoints CRUD.
- `requirements.txt` — dependências necessárias (`fastapi`, `uvicorn`).

Boa sorte! Foque em escrever código claro e testável. 🚀
