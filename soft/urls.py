"""
URL configuration for soft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from tranapp.views import user, books, order, address, upload, wbchat, cart, search, other,analysis,article
from soft import settings

# from tranapp.views.wbchat import MessageView

urlpatterns = [
    path('admin/', admin.site.urls),
    # 用户登录相关
    path("api/register/", user.RegisterView.as_view()),
    path("api/login/", user.LoginView.as_view()),
    path("api/campus/", user.CampusView.as_view()),
    path("api/edited/user/", user.EditView.as_view()),
    # 二手书
    path("api/type/", books.TypeView.as_view()),
    path("api/book/", books.BookView.as_view({"get": "list", "post": "create"})),
    path("api/book/<int:pk>/", books.BookView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path("api/self/book/", books.BookSelfView.as_view({"get": "list", "post": "create"})),
    path("api/self/book/<int:pk>/",
         books.BookSelfView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    # 订单
    path("api/order/", order.OrderView.as_view({"get": "list", "post": 'create'})),
    path("api/order/<int:pk>/", order.OrderView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path("api/sell/order/", order.OrderSellView.as_view({"get": "list"})),
    path("api/sell/order/<int:pk>/", order.OrderSellView.as_view({"get": "retrieve", "put": "update"})),
    # 地址
    path("api/address/", address.AddressView.as_view({"get": "list", "post": 'create'})),
    path("api/address/<int:pk>/",
         address.AddressView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path('api/address/default/<int:pk>/', address.AddDefault.as_view()),

    

    # 消息记录
    path("api/message/", wbchat.MessageView.as_view()),
    # 获取聊天室信息
    path("api/session/", wbchat.SessionView.as_view()),
    # 获取用户相关的聊天室列表
    path("api/session/list/", wbchat.SessionListView.as_view()),

    ##  文件上传视图
    path("upload/avatar/", upload.AvatarUpload.as_view()),
    path("upload/book_img/", upload.BookImgUpload.as_view()),
    # 购物车
    path("api/cart/", cart.CartView.as_view({"get": "list", "post": "create"})),
    path("api/cart/<int:pk>/", cart.CartView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    # 帖子
    path("api/article/self/", article.SelfAtricleView.as_view()),
    path("api/article/", article.ArticleView.as_view({"get": "list", "post": "create"})),
    path("api/article/<int:pk>/", article.ArticleView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    path("api/article/comment/",article.CommentView.as_view()),
    # path("api/article/comment/<int:pk>",article.CommentDetailView.as_view()),
    # 搜索相关
    path("api/book/search/", search.BookSearchVie.as_view()),

    # 轮播图获取
    path("api/banner/", other.BannerView.as_view()),

    # 修改当前用户校区
    path("api/user/campus/<int:cid>/", user.UserCampusChangeView.as_view()),

    # 数据分析路由
    path('book/statistics/', analysis.BookStatistics, name='custom_login'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
