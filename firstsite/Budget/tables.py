import django_tables2 as tables
from .models import UserInput

class UserInputTable(tables.Table):
    class Meta:
        model = UserInput
        template_name = 'django_tables2/bootstrap.html'
        exclude = ('objects', 'user', 'pdobjects', 'id') 