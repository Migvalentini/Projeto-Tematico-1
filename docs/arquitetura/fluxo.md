# Fluxo do Sistema

1. Usuário acessa a aplicação.

2. O sistema exibe o menu principal com as opções:
    - Criar usuário;
    - Fazer login;
    - Sair do sistema.

3. Caso o usuário escolha **Criar usuário**:
    - Informar nome de usuário e senha;
    - Sistema realiza o cadastro;
    - Retorno ao menu principal.

4. Caso o usuário escolha **Fazer login**:
    - Informar nome de usuário e senha;
    - Sistema valida as credenciais;
    - Se autenticado, acessa o menu do usuário.

5. No menu do usuário, estarão disponíveis os módulos:

    ## Renda
    - Cadastrar renda:
        - Informar valor e descrição;
    - Editar renda:
        - Selecionar renda e alterar dados;
    - Excluir renda:
        - Selecionar renda para exclusão.

    ## Despesa
    - Cadastrar despesa:
        - Informar valor, descrição e categoria;
    - Editar despesa:
        - Selecionar despesa e alterar dados;
    - Excluir despesa:
        - Selecionar despesa para exclusão.

    ## Categoria
    - Cadastrar categoria:
        - Informar nome e descrição;
    - Editar categoria:
        - Selecionar categoria e alterar dados;
    - Excluir categoria:
        - Selecionar categoria;
        - Sistema verifica vínculo com despesas;
        - Caso haja vínculo, exibir aviso antes da exclusão.

    ## Cálculos
    - Realizar cálculo do orçamento mensal do usuário.

6. O usuário poderá sair do sistema a qualquer momento através da opção “Sair”.