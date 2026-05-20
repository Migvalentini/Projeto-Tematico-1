# Integração do Sistema

O *Budgetary Control Module* é integrado através de módulos responsáveis pelo gerenciamento de usuários, rendas, despesas e categorias. A interação com o usuário ocorre por meio de uma interface em linha de comando (CLI), utilizando a biblioteca `questionary`.

## Estrutura do Sistema

O sistema utiliza classes separadas para cada entidade principal:
- `Usuario`
- `Categoria`
- `Despesas`
- `Rendas`

Os dados são armazenados temporariamente em listas durante a execução da aplicação.

## Persistência de Dados

A persistência é realizada utilizando arquivos JSON armazenados no diretório:

```
src/armazenamento
```

Arquivos utilizados:
- `usuarios.json`
- `rendas.json`
- `despesas.json`
- `categorias.json`

A função `gravardados()` é responsável por salvar os dados nos arquivos JSON, enquanto a função `carregardados()` realiza a leitura e reconstrução dos objetos durante a inicialização do sistema.

## Integração entre os Módulos

O módulo de despesas possui integração com o módulo de categorias, exigindo que cada despesa esteja vinculada a uma categoria.

Os módulos de rendas e despesas fornecem os dados utilizados no cálculo do orçamento financeiro do usuário.

O sistema também possui categorias padrão carregadas automaticamente na inicialização.

## Fluxo de Integração

1. Usuário interage com a aplicação via terminal;
2. O sistema processa as informações;
3. Os dados são manipulados em memória;
4. As alterações são persistidas em arquivos JSON.