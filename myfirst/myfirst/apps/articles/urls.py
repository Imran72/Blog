from django.urls import path

from . import views

app_name = "articles"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:articleID>/', views.detail, name='detail'),
    path('<int:articleID>/leave_comment/', views.leave_comment, name='leave_comment')
]
