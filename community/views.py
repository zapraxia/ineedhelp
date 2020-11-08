from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.views.generic import TemplateView
from django_tables2.views import SingleTableView, SingleTableMixin
from extra_views import UpdateWithInlinesView, CreateWithInlinesView, InlineFormSet

from .forms import CustomUserCreationForm
from .models import Profile, University, Program, Correspondence
from .tables import UserTable, UniversityTable, ProgramTable


class UniversityListView(SingleTableView):
    model = University
    table_class = UniversityTable


class UniversityDetailView(SingleTableMixin, DetailView):
    model = University

    def get_table(self, **kwargs):
        return ProgramTable(self.object.programs.all())


class UniversityCreateView(CreateView):
    model = University
    fields = ["name", "description"]

    def get_success_url(self):
        return reverse("university-create-done")


class UniversityCreateDoneView(TemplateView):
    template_name = "community/university_create_done.html"


class ProgramListView(SingleTableView):
    model = Program
    table_class = ProgramTable


class ProgramDetailView(SingleTableMixin, DetailView):
    model = Program

    def get_table(self, **kwargs):
        return UserTable(self.object.members.all())

    def post(self, request, *args, **kwargs):
        program = self.get_object()

        if request.user.is_authenticated:
            if request.user in program.members.all():
                program.members.remove(request.user)
            else:
                program.members.add(request.user)

            return HttpResponseRedirect(reverse("program-detail", kwargs={"pk": self.get_object().pk}))
        else:
            return HttpResponseForbidden()


class ProgramCreateView(CreateView):
    model = Program
    fields = ["university", "name", "description"]

    def get_success_url(self):
        return reverse("program-create-done")


class ProgramCreateDoneView(TemplateView):
    template_name = "community/program_create_done.html"


class UserListView(SingleTableView):
    model = get_user_model()
    table_class = UserTable


class ProfileInline(InlineFormSet):
    model = Profile
    fields = ["description", "year", "phone_number", "discord_username", "facebook_link", "skype_username"]
    factory_kwargs = {"can_delete": False}

    def get_object(self):
        return self.request.user.profile


class UserCreateView(CreateWithInlinesView):
    model = get_user_model()
    inlines = [ProfileInline]
    form_class = CustomUserCreationForm

    def get_success_url(self):
        login(self.request, self.object)

        return reverse("user-create-done")


class UserUpdateView(LoginRequiredMixin, UpdateWithInlinesView):
    model = get_user_model()
    fields = ["username", "email"]
    inlines = [ProfileInline]
    template_name = "auth/user_update.html"

    def test_func(self):
        return self.request.user.is_authenticated

    def get_success_url(self):
        return reverse("user-detail", kwargs={"pk": self.object.id})

    def get_object(self, queryset=None):
        return self.request.user


class UserDetailView(SingleTableMixin, DetailView):
    model = get_user_model()
    context_object_name = "_user"

    def get_table(self, **kwargs):
        return ProgramTable(self.object.programs.all())


class UserCreateDoneView(TemplateView):
    template_name = "auth/user_create_done.html"


class CorrespondenceCreateView(CreateView):
    model = Correspondence
    fields = ["name", "email", "subject", "content"]

    def get_success_url(self):
        return reverse("correspondence-create-done")


class CorrespondenceCreateDoneView(TemplateView):
    template_name = "community/correspondence_create_done.html"
