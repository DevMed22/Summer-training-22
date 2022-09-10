from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta(UserCreationForm):
        model = User
        exclude = ('last_login', 'is_superuser', 'groups',
                   'user_permissions', 'is_staff', 'password', 'date_joined', 'is_active')
        fields = '__all__'
