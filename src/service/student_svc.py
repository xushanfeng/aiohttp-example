from src.model import student


async def save_student(data):
    info = student_info(data)
    return await student.insert_student(info)


async def students():
    return await student.select_students()


async def single_student(st_id):
    return await student.select_student_by_st_id(st_id)


def student_info(data):
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "st_class": data.get("class")
    }
