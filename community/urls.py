from django.urls import path

from .views import UserListView, UserCreateView, UserUpdateView, UserDetailView, UniversityListView, \
    UniversityDetailView, ProgramListView, ProgramDetailView, CorrespondenceCreateView, CorrespondenceCreateDoneView

urlpatterns = [
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("users/update/", UserUpdateView.as_view(), name="user-update"),

    path("universities/", UniversityListView.as_view(), name="university-list"),
    path("universities/<int:pk>/", UniversityDetailView.as_view(), name="university-detail"),
    path("programs/", ProgramListView.as_view(), name="program-list"),
    path("programs/<int:pk>/", ProgramDetailView.as_view(), name="program-detail"),

    path("correspondences/create", CorrespondenceCreateView.as_view(), name="correspondence-create"),
    path("correspondences/create/done", CorrespondenceCreateDoneView.as_view(), name="correspondence-create-done")
]
