# Interface do Sistema

## Visão Geral

O *Budgetary Control Module* utiliza uma interface em linha de comando (CLI — *Command Line Interface*), permitindo a interação do usuário através do terminal.

A navegação é realizada por menus interativos desenvolvidos com a biblioteca `questionary`, proporcionando uma utilização simples e organizada das funcionalidades do sistema.

---

# Estrutura da Interface

A interface é organizada em menus hierárquicos, permitindo acesso às funcionalidades principais do sistema.

## Menu Principal

Ao iniciar a aplicação, o usuário visualiza o menu principal com as opções:
- Criar usuário;
- Fazer login;
- Sair do sistema.

---

## Tela de Cadastro de Usuário

Permite ao usuário:
- Informar nome de usuário;
- Informar senha;
- Realizar cadastro no sistema.

Após o cadastro, o usuário retorna ao menu principal.

---

## Tela de Login

Permite autenticação através de:
- Nome de usuário;
- Senha.

Após validação das credenciais, o usuário acessa o menu interno do sistema.

---

# Menu do Usuário

Após o login, a interface disponibiliza acesso aos módulos:

- Rendas;
- Despesas;
- Categorias;
- Cálculos financeiros.

---

## Interface de Rendas

Permite:
- Cadastro de rendas;
- Edição de rendas;
- Exclusão de rendas;
- Visualização das informações cadastradas.

---

## Interface de Despesas

Permite:
- Cadastro de despesas;
- Edição de despesas;
- Exclusão de despesas;
- Associação de categorias às despesas.

---

## Interface de Categorias

Permite:
- Cadastro de categorias;
- Edição de categorias;
- Exclusão de categorias;
- Visualização das categorias existentes.

---

## Interface de Cálculos

Exibe informações relacionadas ao orçamento financeiro do usuário, utilizando os dados cadastrados no sistema.

---

# Navegação

A navegação ocorre através da seleção de opções exibidas no terminal.

O sistema apresenta mensagens de:
- Confirmação;
- Erro;
- Validação;
- Avisos de operações.

---

# Objetivo da Interface

A interface foi projetada para:
- Facilitar o uso do sistema;
- Tornar a navegação intuitiva;
- Organizar as funcionalidades de forma simples;
- Permitir utilização diretamente pelo terminal.