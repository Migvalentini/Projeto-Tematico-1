# Persistência de dados

## Estratégia de Armazenamento
Para o MVP do sistema, optou-se pela persistência em arquivos **JSON**. Foi escolhida essa estrutura de dados devido a:
- Facilidade de leitura tanto por humanos quanto pela linguagem Python.
- Estrutura nativa de dicionários e listas em Python e biblioteca json já integrada nativamente.

## Modelagem dos Dados
O sistema utiliza quatro entidades principais vinculadas pelo `id_usuario`:

### Entidades e Atributos
| Entidade | Atributos Principais | Relacionamento |
| :--- | :--- | :--- |
| **Usuario** | id_usuario, nome, senha | dono dos registros |
| **Categoria** | id_categoria, nome, descricao | classifica Despesas |
| **Despesas** | id_despesa, id_categoria, valor, data | n para 1 (categoria) |
| **Rendas** | id_rendas, valor, descricao, data | n para 1 (usuário) |

## Fluxo de Leitura e Escrita
1. **Inicialização:** O `main.py` solicita ao `gerenciador.py` que carregue em memória os dados presentes nos arquivos da pasta `src/armazenamento`.
2. **Persistência:** Ao realizar qualquer alteração, o método `gravadados` sobrescreve os arquivos JSON correspondentes com os estados atualizados das listas.

## Localização dos Arquivos
Os dados são armazenados na raiz do projeto dentro do diretório:
`src/armazenamento`
- `usuarios.json`
- `categorias.json`
- `despesas.json`
- `rendas.json`