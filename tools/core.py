from django.utils.deprecation import MiddlewareMixin
# 响应头中 添加 Access-Control-Allow-Origin
class CorsMiddleWare(MiddlewareMixin):
    def process_response(self,request,response):
        response["Access-Control-Allow-Origin"] = "*" #所有响应的响应头都添加该响应头，主要用于解决跨域问题。
        response["Access-Control-Allow-Headers"] = "*"
        response["Access-Control-Allow-Methods"] = "*"
        return response