from django import forms
from .models import Profile, Car


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']


class ProfileCreateForm(BaseProfileForm):
    BaseProfileForm.Meta.widgets = {
        'password': forms.PasswordInput
    }


class ProfileEditForm(BaseProfileForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_type', 'model', 'year', 'image_url', 'price']


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def __set_disabled_fields(self):
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance