from itertools import count

from django.contrib.auth import get_user_model
from django_tables2.columns import Column, LinkColumn
from django_tables2.tables import Table
from django_tables2.utils import A

from .models import University, Program


class CountedMixin(Table):
    row_number = Column(empty_values=(), verbose_name="#", orderable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = count(1)

    def render_row_number(self):
        return next(self.counter)


class UserTable(CountedMixin, Table):
    username = LinkColumn("user-detail", args=[A("pk")])

    class Meta:
        model = get_user_model()
        fields = ["row_number", "username", "first_name", "last_name"]


class UniversityTable(CountedMixin, Table):
    name = LinkColumn("university-detail", args=[A("pk")])

    class Meta:
        model = University
        fields = ["row_number", "name"]


class ProgramTable(CountedMixin, Table):
    name = LinkColumn("program-detail", args=[A("pk")])
    university = LinkColumn("university-detail", args=[A("pk")])

    class Meta:
        model = Program
        fields = ["row_number", "name", "university"]
