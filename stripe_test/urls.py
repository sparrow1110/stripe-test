from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def success(request):
    return HttpResponse("<h1>Оплата прошла успешно! Спасибо!</h1>")

def cancel(request):
    return HttpResponse("<h1>Платеж отменен.</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('success/', success),
    path('cancel/', cancel),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)