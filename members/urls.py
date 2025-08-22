from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartyMemberViewSet, UnitNameListView

router = DefaultRouter()
router.register(r'members', PartyMemberViewSet, basename='members')

urlpatterns = [
    path('', include(router.urls)),
    path('unit-names/', UnitNameListView.as_view(), name='unit-names'),
]
