from django.contrib import admin
from tranapp.models import UserInfo, Session, Message, Campus, Type, Book, Cart, Order, Address, Banner
from django.contrib import admin


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'username', 'campus')  # 在列表中显示的字段


class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'sellerid', 'buyerid')  # 可根据需要显示的字段


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sessionID', 'senderID', 'recipientID', 'create_time')  # 可根据需要显示的字段


from django.contrib import admin
from .models import Banner
from django.utils.html import mark_safe


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag', 'link', 'remark')  # 在 admin 列表页显示的字段
    search_fields = ('link', 'remark')  # 允许在 admin 搜索框中搜索的字段

    def image_tag(self, obj):
        # 获取图片路径，去除多余的 media 前缀
        image_url = obj.image_url.url.replace("/media/", "/")
        # 返回 HTML 标签，渲染图片
        return mark_safe(
            '<img src="/media{}" style="max-width: 200px; max-height: 200px;" />'.format(image_url))


admin.site.site_title = "后台管理系统"
# 登录页导航条和首页导航条标题
admin.site.site_header = "二手书后台管理系统"
# 主页标题
admin.site.index_title = "欢迎登陆"

# 注册模型和管理类到后台
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Campus)
admin.site.register(Type)
admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Address)
# admin.site.register(Banner)
