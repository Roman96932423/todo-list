from django.forms import ModelForm

from tasks.models import Task
from utils.bootstrap_form import BootstrapFormMixin


class TaskEditForm(BootstrapFormMixin, ModelForm):
    class Meta:
        model = Task
        fields = ('title', )
