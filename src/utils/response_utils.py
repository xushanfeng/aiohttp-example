
import ujson
import datetime


def error(_request_id, error_code, error_msg):
    return ujson.dumps({'message': error_msg,
                        'result_code': error_code,
                        'server_time': int(datetime.datetime.now().timestamp()),
                        'request_id': _request_id})


def success(_request_id, data=None):
    return ujson.dumps({'message': 'success',
                        'data': data,
                        'result_code': 'success',
                        'server_time': int(datetime.datetime.now().timestamp()),
                        'request_id': _request_id}) if data else ujson.dumps({'message': 'success',
                                                                              'result_code': 'success',
                                                                              'server_time': int(datetime.datetime
                                                                                                 .now().timestamp()),
                                                                              'request_id': _request_id})
