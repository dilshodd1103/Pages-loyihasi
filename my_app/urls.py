from django.urls import path
from .views import HomePageView, AboutPageView, SettingPageView, CommonPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/',AboutPageView.as_view(), name='about'),
    path('setting/', SettingPageView.as_view(), name='setting'),
    path('common', CommonPageView.as_view(), name='common',)
]