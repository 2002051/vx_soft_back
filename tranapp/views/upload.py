# 文件上传视图
import os

from tranapp.utils.auth_ import LoginAuth
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from tranapp.utils.res_ import MyResponse
from rest_framework.exceptions import APIException


class FileUploadException(APIException):
    """文件上传异常"""
    status_code = status.HTTP_200_OK


class AvatarUpload(MyResponse, APIView):
    authentication_classes = [LoginAuth]
    """上传头像"""
    def post(self, request, format=None):
        userinfo = request.user
        file_obj = request.FILES.get('file')
        if file_obj is None:
            # return Response({'error': '上传失败'}, status=status.HTTP_200_OK)
            raise FileUploadException("上传失败")

        file_name = str(userinfo.id) + "_" + userinfo.nickname + "_" + file_obj.name
        file_path = os.path.join(settings.MEDIA_ROOT, "avatar", file_name)
        to_save_path = settings.MEDIA_URL + "avatar" + "/" + file_name
        with open(file_path, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        return Response({'message': '上传成功', "path": to_save_path}, status=status.HTTP_200_OK)


class BookImgUpload(APIView):
    """上传图书图片"""

    def post(self, request, format=None):
        print(request.FILES)
        file_obj = request.FILES.get('file')
        if file_obj is None:
            # return Response({'error': '上传失败'}, status=status.HTTP_200_OK)
            raise FileUploadException("上传失败")
        file_path = os.path.join(settings.MEDIA_ROOT, "book_img", file_obj.name)
        to_save_path = settings.MEDIA_URL + "book_img" + "/" + file_obj.name
        with open(file_path, 'wb+') as destination:
            for chunk in file_obj.chunks():
                destination.write(chunk)
        return Response({'message': '上传成功', "path": to_save_path}, status=status.HTTP_200_OK)
