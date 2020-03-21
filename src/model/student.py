from sqlalchemy import BigInteger, SMALLINT, Integer
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import Table
from sqlalchemy import MetaData

from src.constants import const
from src.model.base_option import BaseOption
from src.utils.time_utils import current_sec_time


class Student(BaseOption):

    def __init__(self):
        meta = MetaData()
        self.student_tb = Table(
            "student",
            meta,
            Column(const.Student.ID, Integer, primary_key=True),
            Column(const.Student.NAME, String(40)),
            Column(const.Student.CLASS, String(40)),
            Column(const.Student.STATUS, SMALLINT, default=1),
            Column(const.Student.CREATE_TIME, BigInteger, default=current_sec_time()),
            Column(const.Student.UPDATE_TIME, BigInteger, default=current_sec_time())
        )

    async def insert_student(self, student_obj):
        sql = self.student_tb.insert().values(
            name=student_obj.get("name"),
            st_class=student_obj.get("st_class"),
            status=student_obj.get("status", 1),
            create_time=current_sec_time(),
            update_time=current_sec_time())
        return await self.insert_or_update(sql)

    async def get_update_student_sql(self, student_obj):
        sql = self.student_tb.update().values(
            name=student_obj.get("name"),
            st_class=student_obj.get("st_class"),
            status=student_obj.get("status"),
            create_time=current_sec_time(),
            update_time=current_sec_time()
        ).where(self.student_tb.c.id == student_obj.get(const.Student.ID))
        return self.query(sql)

    async def status(self, st_id):
        try:
            sql = self.student_tb.delete().where(self.student_tb.c.id == st_id)
            return await self.insert_or_update(sql)
        except Exception as e:
            raise Exception('update status failed, error info:{}.'.format(e))

    async def select_student_by_st_id(self, st_id):
        try:
            sql = self.student_tb.select().where(self.student_tb.c.id == st_id)
            cursor = await self.query(sql)
            records = await cursor.fetchall()
            return [dict(r) for r in records] if records else None
        except Exception as e:
            raise Exception('select_by_id failed, error info:{}.'.format(e))

    async def select_students(self):
        try:
            sql = self.student_tb.select()
            print(sql)
            cursor = await self.query(sql)
            records = await cursor.fetchall()
            return [dict(r) for r in records] if records else None
        except Exception as e:
            raise Exception('select_by_id failed, error info:{}.'.format(e))
