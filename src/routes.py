from src.views.student_api import students, student, save_student
from .views.status import status


def set_up(app):
    # 项目状态
    app.router.add_get('/status', status, name='status')

    # 获取全部学生信息
    app.router.add_get('/students', students, name='students')

    # 获取单个学生信息
    app.router.add_get('/student', student, name='student')

    # 获取单个学生信息
    app.router.add_post('/save', save_student, name='save_student')
