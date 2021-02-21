from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from boss_list.views import AddPlayerViewSet, BossListViewSet

router = routers.DefaultRouter() 
router.register(r'bossList', BossListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('addplayer/', AddPlayerViewSet.as_view())
]
