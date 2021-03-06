from django.urls import path
from . import views

app_name = 'monitor'

urlpatterns = [
    # トップ画面
    path('', views.IndexView.as_view(), name='index'),

    # 詳細画面
    path('monitor/<int:pk>/', views.DetailView.as_view(), name='detail'),

    # グラフ描画
    path('monitor/<int:pk>/plot/', views.get_svg, name='plot'),

    # 500エラー確認用
    path('test/', views.my_test_500_view, name='test'),



    path('', views.post_list, name='post_list'),

]
