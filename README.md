# Projeto-Tematico-1

## Nome do Projeto: 
Budgetary Control Module

## Integrantes: 
Diego Silveira, Miguel Valentini e Nícolas Buzin Gomes

## Temática: 
Sistema para controle orçamentário mensal e calculo de metas de compras.

## Descrição geral do sistema e objetivo da aplicação: 
Diversas pessoas não têm como hábito o controle de suas finanças.
Pensando nisso, torna-se interessante desenvolver um método prático para auxiliar
essa organização pessoal, a fim de dar mais liberdade financeira aos usuários. Com
isso, surge a ideia do Budgetary Control Module, que é um aplicativo desktop
baseado em linhas de comando desenvolvido em Python. Ele visa auxiliar os
usuários no controle de suas finanças pessoais, permitindo registrar, categorizar e
monitorar receitas e despesas a fim de promover maior saúde financeira

## Lista inicial de funcionalidades: 
Entregar uma interface em linhas de comando (terminal), com
funcionalidades de inserção de dados para proventos, despesas e categorias de
gastos. Módulo de cálculo de orçamento do mês para o controle de gastos.
Integração com arquivos para armazenamento dos dados informados no programa.

## Estrutura do projeto:
projeto/
│
├── README.md
├── src/ = pasta principal dos arquivos python para a execução do projeto
│ ├── armazenamento/ = pasta responsável por armazenar os dados para que o usuário não precisa inserí-los novamente a cada abertura do sistema
│ ├── interface / = pasta responsável por gerenciar e executar a interface do usuário com o sistema, contendo diferentes arquivos para cada menu
│ └── logica/ = pasta responsável por executar as funções, cálculos e algoritmos
├── docs/ = pasta responsável por documentar as etapas e ferramentas do projeto
│ ├── arquitetura/ = pasta responsável por armezenar as informações referentes à ferramenta Miro, usada para a elaboração do diagrama de casos de uso
│ ├── calendario/ = pasta responsável por detalhar o que foi feito em cada semana, com o intuito de facilitar o desenvolvimento da documentação final do projeto, ao final do semestre
│ ├── testes/ = pasta responsável por documentar os testes no sistema, garantindo que todos os requisitos sejam atingidos
│ ├── rastreabilidade / = pasta responsável por ...
│ └── decisoes/ = pasta responsável por ...



## Semanas:

### Semana 1 (07/04):
- Miguel foi responsável pela criação inicial do repositório, compartilhando com os membros do grupo e professora. 
  Além disso, incluiu as informações iniciais no arquivo README.md e criou a organização inicial das pastas do projeto.
  Todo esse processo foi feito durante o período da aula, compartilhando a tela com os demais membros do grupo.
- Diego e Nicolas ajudaram o Miguel com ideias, ajustes e apontamentos, de forma que todos os integrantes estejam conectados e participativos no desenvolvimento do projeto.

### Semana 2 (14/04):
- Diego foi responsável pela inicialização do menu principal, assim como o desenvolvimento inicial do sistema de login e cadastros de usuários
- Miguel foi responsável pela documentação do que foi realizado na semana 2
- Nicolas foi responsável por pesquisar e sugerir a biblioteca Questionary que foi instalada e utilizada no projeto para o desenvolvimento dos menus

### Semana 3 (21/04) - Feriado Tiradentes:
- Mesmo no feriado, Miguel prosseguiu com o desenvolvimento do projeto, implementando novos recursos no menu principal do sistema, como:
-- Criação do id_usuario para o usuário logado
-- Criação do menu logado, para que os usuários possam fazer login no sistema e conseguirem operarem nos seus dados específicos. Nesse momento, foram criados apenas a estrutura inicial
-- Criação das categorias das despesas

### Semana 4 (28/04):
- Nicolas desenvolveu a criação das classes do sistema, como categorias, despesas, rendas e usuarios, adaptando as variáveis criadas inicialmente dentro do menu para as novas classes criadas 
- Criação do .gitignore
- Ajustes de inicialização em variáveis de dataclass, criação de arquivos json separados para cada classe, uso de arquivo para armazenamento geral de dados

### Semana 5 (05/05): 
- Documentação dos dados.md, detalhando a entidade de armazenamento, modelagem de dados, entidades, atributos, fluxo de leitura e escrita e localização de arquivos
- Gravação e Leitura em arquivos json, correção id_despesa, melhorias menus e renomeação de arquivos

### Semana 6 (12/05):
- Cadastro de categorias
- Edição e exclusão de rendas, despesas e categorias
- Documentação do que foi realizado durante as semanas passadas

### Semana 7 ():
- Ajustes nas categorias, de modo que elas sejam restritas por usuário
- Ajustes no gerenciador, de modo que retorne as listas filtradas por id_usuario
- No menu, ajustes para inicializar corretamente o usuário logado dentro do gerenciador
- Separação de menus em arquivos distintos
- Inicio dos cálculos
- Cadastro e edição de categoria
- Documentação da visão geral, funcionalidades, fluxo, integração, decisões técnicas e interface