from sqlmodel import SQLModel, create_engine, Session

sqlite_file_name = "watct.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    """创建 db 和 table"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """获取 db 的 Session"""
    with Session(engine) as session:
        yield session


if __name__ == '__main__':
    create_db_and_tables()
