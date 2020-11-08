from django.urls import path

from . import views

urlpatterns = [
    path("universities/", views.UniversityListView.as_view(), name="university-list"),
    path("universities/<int:pk>/", views.UniversityDetailView.as_view(), name="university-detail"),
    path("universities/create/", views.UniversityCreateView.as_view(), name="university-create"),
    path("universities/create/done/", views.UniversityCreateDoneView.as_view(), name="university-create-done"),

    path("programs/", views.ProgramListView.as_view(), name="program-list"),
    path("programs/<int:pk>/", views.ProgramDetailView.as_view(), name="program-detail"),
    path("programs/create/", views.ProgramCreateView.as_view(), name="program-create"),
    path("programs/create/done/", views.ProgramCreateDoneView.as_view(), name="program-create-done"),

    path("users/", views.UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),
    path("users/update/", views.UserUpdateView.as_view(), name="user-update"),
    path("users/create/", views.UserCreateView.as_view(), name="user-create"),
    path("users/create/done/", views.UserCreateDoneView.as_view(), name="user-create-done"),

    path("correspondences/create/", views.CorrespondenceCreateView.as_view(), name="correspondence-create"),
    path("correspondences/create/done/", views.CorrespondenceCreateDoneView.as_view(),
         name="correspondence-create-done")
]
