
# 📋 Aplicação de Lista de Tarefas em Python

Esta é uma aplicação simples em Python para gerenciamento de tarefas. O programa permite **adicionar**, **listar**, **remover** e **salvar tarefas** com diferentes níveis de prioridade. As tarefas são armazenadas em um arquivo `tarefas.json`, garantindo que você não perca seus dados ao fechar o programa.

---

## 🧠 Funcionalidades

- ✅ Adicionar uma nova tarefa com prioridade
- 📄 Listar todas as tarefas cadastradas
- ❌ Remover uma tarefa específica
- 💾 Salvar todas as tarefas em um arquivo `.json`
- 🔁 Interface de linha de comando com menu interativo

---

## 🛠️ Como Usar

### 1. Clone ou baixe este repositório

```bash
git clone https://github.com/seuusuario/tarefas-python.git
cd tarefas-python
```

### 2. Execute o script

```bash
python tarefas.py
```

---

## 📦 Estrutura do Projeto

```
tarefas.py
tarefas.json (gerado automaticamente após salvar)
README.md
```

---

## 🧾 Exemplo de Uso

Ao executar o programa, você verá o seguinte menu:

```
** Menu de Opções **
1. Adicionar Tarefa
2. Listar Tarefas
3. Remover Tarefa
4. Salvar Tarefas
5. Sair
```

### ✅ Adicionar Tarefa

- Exemplo:  
  `Digite uma tarefa:` **Estudar Python**  
  `Digite a prioridade da tarefa:` **Alta**

### 📄 Listar Tarefas

Exibe todas as tarefas cadastradas com suas respectivas prioridades:
```
Lista de Tarefas:
- Estudar Python (Prioridade Alta)
```

### ❌ Remover Tarefa

- Exemplo:  
  `Digite a tarefa a ser removida:` **Estudar Python**

### 💾 Salvar Tarefas

Salva todas as tarefas no arquivo `tarefas.json`. Você verá a mensagem:
```
Tarefas salvas com sucesso!
```

---

## 🧪 Tecnologias Utilizadas

- Python 3.x
- Biblioteca Padrão `json`

---

## ⚠️ Observações

- O arquivo `tarefas.json` será criado automaticamente na primeira vez que você salvar tarefas.
- Se o arquivo não for encontrado ao iniciar o programa, uma nova lista será iniciada.

---
