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
from tranapp.views import user, books, order, address
from soft import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("api/register/", user.RegisterView.as_view()),
    path("api/login/", user.LoginView.as_view()),
    path("api/campus/", user.CampusView.as_view()),

    path("api/type/", books.TypeView.as_view()),
    path("api/book/", books.BookView.as_view({"get": "list", "post": "create"})),
    path("api/book/<int:pk>/", books.BookView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    path("api/order/", order.OrderView.as_view({"get": "list", "post": 'create'})),
    path("api/order/<int:pk>/", order.OrderView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    path("api/address/", address.AddressView.as_view({"get": "list", "post": 'create'})),
    path("api/address/<int:pk>/",
         address.AddressView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
