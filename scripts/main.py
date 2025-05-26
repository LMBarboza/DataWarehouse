import argparse
import logging
import os
from utils.database_client import DatabaseConnection
from queries.create_db import CREATE_DB
from queries.drop_tables import DROP_TABLES


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("locadora.log"), logging.StreamHandler()],
    )

    parser = argparse.ArgumentParser(
        description="Script Para Criação de Banco de Dados PostgreSQL"
    )

    parser.add_argument(
        "--drop_tables",
        action="store_true",
        help="Remove Todas Tabelas",
    )

    parser.add_argument(
        "--create_db",
        action="store_true",
        help="Cria As Tabelas",
    )
    args = parser.parse_args()
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    db_pg = DatabaseConnection(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"
    )
    try:

        if args.drop_tables:
            logging.info("Dropando Tabelas...")
            db_pg.execute_query(DROP_TABLES)
            logging.info("Tabelas Dropadas!!!")

        if args.create_db:
            logging.info("Criando Bancos de Dados...")
            db_pg.execute_query(CREATE_DB)
            logging.info("Banco de Dados Criado com Sucesso!!!")

    except Exception as e:
        logging.error(f"Erro : {e}", exc_info=True)


if __name__ == "__main__":
    main()
