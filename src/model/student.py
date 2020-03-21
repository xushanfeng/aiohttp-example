from sqlalchemy import BigInteger, select, Text, SMALLINT, Integer
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import MetaData

from src.constants.const import Student
from src.model.base import insert_or_update, query
from src.utils.time_utils import current_sec_time

meta = MetaData()

student_tb = Table(
    "student",
    meta,
    Column(Student.ID, Integer, primary_key=True),
    Column(Student.NAME, String(40)),
    Column(Student.CLASS, String(40)),
    Column(Student.STATUS, SMALLINT, default=1),
    Column(Student.CREATE_TIME, BigInteger, default=current_sec_time()),
    Column(Student.UPDATE_TIME, BigInteger, default=current_sec_time())
)


async def insert_student(student_obj):
    sql = student_tb.insert().values(
        name=student_obj.get("name"),
        st_class=student_obj.get("st_class"),
        status=1 if not student_obj.get("status") else student_obj.get("status"),
        create_time=current_sec_time(),
        update_time=current_sec_time())
    return await insert_or_update(sql)


async def get_update_student_sql(student_obj):
    return student_tb.update().values(
        name=student_obj.get("name"),
        st_class=student_obj.get("st_class"),
        status=student_obj.get("status"),
        create_time=current_sec_time(),
        update_time=current_sec_time()
    ).where(student_tb.c.id == student_obj.get(Student.ID))


async def status(st_id):
    try:
        sql = student_tb.delete().where(student_tb.c.id == st_id)
        return await insert_or_update(sql)
    except Exception as e:
        raise Exception('update status failed, error info:{}.'.format(e))


async def select_student_by_st_id(st_id):
    try:
        sql = student_tb.select().where(student_tb.c.id == st_id)
        cursor = await query(sql)
        records = await cursor.fetchall()
        return [dict(r) for r in records] if records else None
    except Exception as e:
        raise Exception('select_by_id failed, error info:{}.'.format(e))


async def select_students():
    try:
        sql = student_tb.select()
        print(sql)
        cursor = await query(sql)
        records = await cursor.fetchall()
        return [dict(r) for r in records] if records else None
    except Exception as e:
        raise Exception('select_by_id failed, error info:{}.'.format(e))
