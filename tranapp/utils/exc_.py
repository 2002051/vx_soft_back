# 统一化处理错误信息
from rest_framework.views import exception_handler, set_rollback

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.db import connections, models
from django.http import Http404
from django.http.response import HttpResponseBase
from django.utils.cache import cc_delim_re, patch_vary_headers
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from rest_framework import exceptions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.schemas import DefaultSchema
from rest_framework.settings import api_settings
from rest_framework.utils import formatting
from rest_framework.exceptions import AuthenticationFailed

class MyAuthenticationFeild(AuthenticationFailed):
    # 无论何种权限异常，状态码都是200
    status_code = status.HTTP_200_OK



def MyExcHandler(exc, context):

    if isinstance(exc, Http404):
        exc = exceptions.NotFound(*(exc.args))
        exc.detail = 'no_found'
        exc.x_code = 1001
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied(*(exc.args))
        exc.x_code = 1002
    elif isinstance(exc, AuthenticationFailed):
        exc = MyAuthenticationFeild(*(exc.args))
        exc.x_code = 1003

    if isinstance(exc, exceptions.APIException):
        print("exc", type(exc))

        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail

        else:
            data = {'detail': exc.detail}

        set_rollback()
        exc_code = getattr(exc,"x_code",None) or -1
        data = {"code":exc_code,'detail': exc.detail}
        return Response(data, status=200, headers=headers)
        # return Response(data, status=exc.status_code, headers=headers)
    data = {"code":-2,"detail":str(exc)}

    return Response(data, status=500)
