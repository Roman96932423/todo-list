def get_bootstrap_classes(form):
    for visible_field in form.visible_fields():
        existing_classes = visible_field.field.widget.attrs.get('class', '')
        visible_field.field.widget.attrs['class'] = f'{existing_classes} form-control'.strip()
        

class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        get_bootstrap_classes(self)
    