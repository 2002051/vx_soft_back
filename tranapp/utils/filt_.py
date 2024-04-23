# 过滤组件
from rest_framework.filters import BaseFilterBackend


class BookByTypeFilter(BaseFilterBackend):
    """ 图书按照分类过滤"""

    def filter_queryset(self, request, queryset, view):
        type_id = request.query_params.get('type', "")
        if type != "":
            return queryset
        return queryset.filter(type_id=type_id)


class OrderByUserFilter(BaseFilterBackend):
    """ 订单按照用户过滤 """

    def filter_queryset(self, request, queryset, view):
        userinfo = request.user
        return queryset.filter(user_id=userinfo.id)


class AddressBuUserFilter(BaseFilterBackend):
    """地址按照用户过滤"""

    # 这里过滤其实可以和上面订单一样的，但是设计数据库的时候两个表指向用户的外键字段名不一样，因此另写一个
    def filter_queryset(self, request, queryset, view):
        userinfo = request.user
        return queryset.filter(userinfo_id=userinfo.id)
