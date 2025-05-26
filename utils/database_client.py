from sqlalchemy import Row, create_engine, text
from sqlalchemy.engine import Engine
from typing import Optional, Sequence


class DatabaseConnection:
    def __init__(self, database_url: str) -> None:
        self.engine: Engine = create_engine(database_url, echo=True)

    def execute_query(
        self, query: str, chunk_size: int | None = None
    ) -> Optional[Sequence[Row]]:
        with self.engine.connect() as connection:
            result = connection.execute(text(query))
            if result.returns_rows is False:
                connection.commit()
                return None

            if chunk_size:
                return result.fetchmany(chunk_size)

            return result.fetchall()
