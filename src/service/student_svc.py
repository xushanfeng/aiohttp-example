from src.model.student import Student


async def save_student(data):
    info = student_info(data)
    return await Student().insert_student(info)


async def students():
    return await Student().select_students()


async def single_student(st_id):
    return await Student().select_student_by_st_id(st_id)


def student_info(data):
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "st_class": data.get("class")
    }
