
from django.urls import path
from .views import PublicView, AdminOnlyView

urlpatterns = [
    path('public/', PublicView.as_view(), name='public'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
]