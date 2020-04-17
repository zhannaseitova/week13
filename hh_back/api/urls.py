from django.urls import path
from api import views_cbv

urlpatterns = [
    
    path('login/', obtain_jwt_token),
    path('companies/', views_cbv.CompanyListAPIView),
    path('companies/<int:id>/', views_cbv.CompanyDetailAPIView),
   # path('companies/<int:id>/vacancies/', views_cbv.company_vacancies),
    path('vacancies/', views_cbv.VacancyListAPIView),
    path('vacancies/<int:id>/', views_cbv.VacancyDetailAPIView),
   # path('vacancies/top_ten/', views.top_vacancies)
]