# 过滤组件
from rest_framework.filters import BaseFilterBackend

class BookByTypeFilter(BaseFilterBackend):
    """ 图书按照分类过滤"""
    def filter_queryset(self, request, queryset, view):
        type_id = request.query_params.get('type')
        if not type:
            return queryset
        return queryset.filter(type_id=type_id)


class OrderByUserFilter(BaseFilterBackend):
    """ 订单按照用户过滤 """
    def filter_queryset(self, request, queryset, view):
        userinfo = request.user
        return queryset.filter(user_id=userinfo.id)
