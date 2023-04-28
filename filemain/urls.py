from django.urls import path, include
from filemain import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'EmployeeDetails', views.EmployeeViewsets)
urlpatterns = [
    path('',views.index, name='index'),
    path('save_data/', views.Save_data, name='Save_data'),
    path('api/', include(router.urls)),
]