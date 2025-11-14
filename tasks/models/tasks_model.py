from django.db.models import (
    Model,
    CharField,
    TextField,
    DateTimeField,
    ForeignKey,
    CASCADE
    )
from django.conf import settings


class Task(Model):
    title = CharField(max_length=50, null=False, blank=False)
    content = TextField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    created_by = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
        