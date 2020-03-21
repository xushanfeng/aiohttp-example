import asyncio

from src.service import student_svc


# 使用asyncio.shield 防止请求过程取消请求造成数据库阻塞

async def students(request):
    return await asyncio.shield(student_svc.students())


async def save_student(request):
    data = await request.json()
    return await asyncio.shield(student_svc.save_student(data))


async def student(request):
    st_id = request.rel_url.query.get("id")
    return await asyncio.shield(student_svc.single_student(st_id))
