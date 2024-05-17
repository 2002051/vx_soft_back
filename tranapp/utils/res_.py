
from rest_framework.response import Response
class MyResponse:
    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        if response.exception:
            return response
        response.data = {"code": 0, "data": response.data}
        return response
