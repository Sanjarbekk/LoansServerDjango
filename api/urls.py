from django.urls import path, include
from .views import LoanAPIView, LoanDetails,LoanAPIAdd
urlpatterns = [

    path('loans', LoanAPIView.as_view()),
    path('loan', LoanAPIAdd.as_view()),
    path('deleteLoan/<str:uid>', LoanDetails.as_view())

]
