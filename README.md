# DataWarehouse

Os diagramas da modelagem conceitual e lógica e o script SQL estão localizados no diretório `modelagem/`.

Este projeto utiliza Docker Compose para:

1.  **Inicializar um container do banco de dados PostgreSQL.**
2.  **Executar um script Python que é responsável por executar comandos DDL para criar e configurar o esquema do banco de dados.

## Como Usar

Com Docker e Docker Compose instalados, execute na raiz deste diretório:

```bash
docker compose up

