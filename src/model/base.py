from src import Mysql


async def insert_or_update(*sqls):
    try:
        engine = await Mysql.get_engine()
        async with engine.acquire() as conn:
            await conn.connection.autocommit(False)
            trans = None
            try:
                trans = await conn.begin()
                for sql in sqls:
                    await conn.execute(sql)
                await trans.commit()
                return "success"
            except Exception as t:
                if trans:
                    await trans.rollback()
                raise Exception(t)
            finally:
                await conn.connection.autocommit(True)
                conn.connection.close()
    except Exception as e:
        raise Exception(e)


async def query(sql):
    try:
        engine = await Mysql.get_engine()
        async with engine.acquire() as conn:
            try:
                return await conn.execute(sql)
            except Exception as exec_err:
                raise Exception(exec_err)
            finally:
                conn.connection.close()
    except Exception as e:
        raise Exception(e)
