import asyncio
from aiohttp import web

# 版本号
from src.common.mysql import Mysql
from config.setting import config
from src.routes import set_up
from src.utils.request_utils import request_id
from src.utils.response_utils import success, error

__version__ = '1.0.0'


def create_app():
    # 增加响应处理
    my_app = web.Application(middlewares=[middleware])
    my_app['config'] = config
    # 初始化mysql
    asyncio.ensure_future(Mysql.init_engine())
    # 初始化路由
    set_up(my_app)
    return my_app


@web.middleware
async def middleware(request, handler):
    _request_id = request_id(request)
    try:
        request['request_id'] = _request_id
        data = await handler(request)
        if data:
            resp = success(_request_id, data)
        else:
            resp = success(_request_id)
    except ValueError as e:
        resp = error(_request_id, "RC_INVALID_PARAM", e.args[0] if e.args else 'params invalid')
    except Exception as e1:
        resp = error(_request_id, "RC_INTERNAL_ERROR", e1.args[0] if e1.args else 'inner error')
    return web.Response(body=resp.encode(), content_type='application/json')
