# Funcionalidades do Sistema

## Gerenciamento de Usuários

### Cadastro de Usuário
Permite o cadastro de novos usuários no sistema através do preenchimento de:
- Nome de usuário;
- Senha.

### Login
Permite que usuários cadastrados acessem o sistema utilizando suas credenciais.

O sistema realiza a validação das informações antes de liberar o acesso às funcionalidades internas.

---

## Gerenciamento de Rendas

### Cadastro de Renda
Permite registrar entradas financeiras contendo:
- Valor;
- Descrição;
- Data de inclusão.

### Edição de Renda
Permite alterar informações de rendas previamente cadastradas.

### Exclusão de Renda
Permite remover registros de renda do sistema.

---

## Gerenciamento de Despesas

### Cadastro de Despesa
Permite registrar despesas financeiras contendo:
- Valor;
- Descrição;
- Categoria;
- Data de inclusão.

### Edição de Despesa
Permite alterar informações de despesas cadastradas.

### Exclusão de Despesa
Permite remover despesas do sistema.

---

## Gerenciamento de Categorias

### Cadastro de Categoria
Permite criar categorias personalizadas contendo:
- Nome;
- Descrição.

### Edição de Categoria
Permite alterar informações das categorias cadastradas.

### Exclusão de Categoria
Permite excluir categorias do sistema.

O sistema verifica se existem despesas vinculadas à categoria antes da exclusão.

### Categorias Padrão
O sistema possui categorias pré-cadastradas carregadas automaticamente na inicialização da aplicação.

---

## Cálculo Financeiro

O sistema realiza o cálculo do orçamento financeiro do usuário com base em:
- Total de rendas cadastradas;
- Total de despesas cadastradas.

Com isso, é possível visualizar o saldo financeiro atual.

---

## Persistência de Dados

O sistema realiza armazenamento permanente das informações utilizando arquivos JSON.

Os dados persistidos incluem:
- Usuários;
- Rendas;
- Despesas;
- Categorias.

As informações permanecem disponíveis entre diferentes execuções da aplicação.

---

## Interface em Linha de Comando

O sistema utiliza interface CLI (*Command Line Interface*) para interação com o usuário.

A navegação ocorre através de menus interativos utilizando a biblioteca `questionary`.