from django.urls import path,include
from main import views
urlpatterns = [
path('list/',views.RecruitList.as_view()),
path('index/',views.RecruitList.as_view()),
    path('submit/',views.NewRecruit.as_view()),
path('bulkedit/',views.RecruitListUpdate.as_view()),
path('edit/<int:pk>/', views.RecruitDetail.as_view()),
]

