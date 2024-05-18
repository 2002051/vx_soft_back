# 过滤组件
from rest_framework.filters import BaseFilterBackend


class BookByTypeFilter(BaseFilterBackend):
    """ 图书按照分类,如果没有type，则跳过"""

    def filter_queryset(self, request, queryset, view):
        type_id = request.query_params.get('type', "")
        # print(type_id,type(type_id))
        if type_id == "" or type_id == "0":
            return queryset
        return queryset.filter(type_id=type_id)


from tranapp import models


class BookExcludeSelfFilter(BaseFilterBackend):
    """过滤当前用户自己发布的书籍"""

    def filter_queryset(self, request, queryset, view):
        userinfo = request.user
        return queryset.exclude(userinfo=userinfo)


class BookByCampusFilter(BaseFilterBackend):
    """按照校区过滤"""

    def filter_queryset(self, request, queryset, view):
        userinfo = request.user
        campus = userinfo.campus
        # models.Book.objects.filter()
        print(queryset)
        return queryset.filter(userinfo__campus_id=campus.id)


class BookByUserFilter(BaseFilterBackend):
    """按照认证用户过滤图书条目"""

    def filter_queryset(self, request, queryset, view):
        userinfo = request.user
        return queryset.filter(userinfo=userinfo)


class OrderByUserFilter(BaseFilterBackend):
    """ 订单按照用户过滤 """

    def filter_queryset(self, request, queryset, view):
        userinfo = request.user
        return queryset.filter(user_id=userinfo.id)


class OrderBySellerFilter(BaseFilterBackend):
    """ 订单按照卖家身份过滤过滤 """

    def filter_queryset(self, request, queryset, view):
        userinfo = request.user
        return queryset.filter(seller_id=userinfo.id)


class AddressByUserFilter(BaseFilterBackend):
    """地址按照用户过滤"""

    # 这里过滤其实可以和上面订单一样的，但是设计数据库的时候两个表指向用户的外键字段名不一样，因此另写一个
    def filter_queryset(self, request, queryset, view):
        userinfo = request.user
        return queryset.filter(userinfo_id=userinfo.id)


class CartByUserFilter(BaseFilterBackend):
    """购物车条目根据用户信息过滤"""

    def filter_queryset(self, request, queryset, view):
        userinfo = request.user
        return queryset.filter(user_id=userinfo.id)
