
import aiomysql.sa

from config.setting import config

mysql_config = config["mysql"]


class Mysql(object):
    engine = None

    def __init__(self, engine):
        self.engine = engine

    @staticmethod
    async def init_engine():
        Mysql.engine = await aiomysql.sa.create_engine(user=mysql_config["user"], db=mysql_config["database"],
                                                       host=mysql_config["host"], password=mysql_config["password"],
                                                       autocommit=True, connect_timeout=10, echo=False)

    @staticmethod
    async def get_engine():
        if not Mysql.engine:
            await Mysql.init_engine()
        return Mysql.engine
