from django.urls import path

from .views import UserListView, UserDetailView, WorkshopListView, WorkshopDetailView, WorkshopCreateView, EnrollmentListView, EnrollmentDetailView

urlpatterns = [
    path('user/', UserListView.as_view()),
    path('user/<pk>', UserDetailView.as_view()),
    path('workshop/', WorkshopListView.as_view()),
    path('workshop/detail/<pk>', WorkshopDetailView.as_view()),
    path('workshop/create', WorkshopCreateView.as_view()),
    path('enrollment/', EnrollmentListView.as_view()),
    path('enrollment/<pk>', EnrollmentDetailView.as_view()),
]
