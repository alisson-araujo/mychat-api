from sqlmodel import create_engine, Session


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            "mysql+pymysql", "root", "mypassword", "localhost", "3306", "mychat"
        )
        self.__engine = self.__create_engine()
        self.session = None

    def __create_engine(self):
        engine = create_engine(self.__connection_string, echo=True)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        self.session = Session(self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
