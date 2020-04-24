from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
#from api import views_cbv
from api.views_fbv import company_list, company_detail, vacancy_list, vacancy_detail
from api.views_cbv import CompanyList, VacancyList, CompanyVacancies, VacancyDetails, CompanyDetails
urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', CompanyList.as_view()),
    path('companies/<int:pk>/', CompanyDetails.as_view()),
    path('companies/<int:company_id>/vacancies/', CompanyVacancies.as_view()),
    path('vacancies/', VacancyList.as_view()),
    path('vacancies/<int:pk>/', VacancyDetails.as_view())
]


