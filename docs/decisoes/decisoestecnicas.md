# Decisões Técnicas

## Linguagem de Programação

O sistema foi desenvolvido utilizando a linguagem Python devido à sua simplicidade, legibilidade e facilidade de desenvolvimento para aplicações desktop em linha de comando.

---

# Arquitetura do Projeto

O projeto foi estruturado utilizando separação por módulos e classes, organizando as responsabilidades do sistema em diferentes arquivos.

As principais entidades da aplicação foram separadas em classes específicas:
- `Usuario`
- `Categoria`
- `Despesas`
- `Rendas`

Essa abordagem facilita:
- Organização do código;
- Reutilização;
- Manutenção;
- Escalabilidade do sistema.

---

# Interface CLI

Foi adotada uma interface CLI (*Command Line Interface*) para simplificar o desenvolvimento do MVP e permitir foco na lógica de negócio da aplicação.

A biblioteca `questionary` foi utilizada para:
- Criação de menus interativos;
- Navegação entre funcionalidades;
- Captura de entradas do usuário.

---

# Persistência de Dados

A persistência foi implementada utilizando arquivos JSON.

Essa decisão foi tomada devido:
- Facilidade de implementação;
- Leitura simples dos dados;
- Compatibilidade nativa com Python;
- Adequação ao escopo do MVP.

Os arquivos JSON armazenam:
- Usuários;
- Rendas;
- Despesas;
- Categorias.

---

# Manipulação de Objetos

O sistema utiliza `dataclasses` para representar as entidades da aplicação.

Essa abordagem reduz código repetitivo e facilita:
- Criação de objetos;
- Serialização;
- Organização dos atributos.

---

# Serialização de Dados

Foi implementado um encoder personalizado (`EnhancedJSONEncoder`) para permitir:
- Conversão de objetos `dataclass` para JSON;
- Conversão de objetos `datetime` para formato serializável.

---

# Armazenamento em Memória

Durante a execução, os dados são mantidos em listas em memória:
- `usuarios`
- `rendas`
- `despesas`
- `categorias`

As alterações realizadas são persistidas posteriormente nos arquivos JSON.

---

# Estrutura de Diretórios

O projeto foi organizado em diretórios separados para:
- Classes;
- Menus;
- Armazenamento;
- Arquivos principais da aplicação.

Essa estrutura melhora a organização e manutenção do sistema.

---

# Categorias Padrão

O sistema possui categorias financeiras pré-definidas carregadas automaticamente na inicialização da aplicação.

Essa decisão foi adotada para:
- Melhorar a experiência do usuário;
- Facilitar os primeiros cadastros;
- Padronizar categorias iniciais.