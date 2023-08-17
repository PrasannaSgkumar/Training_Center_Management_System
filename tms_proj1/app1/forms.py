from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.forms import ModelForm
from .models import Students, Courses,Staffs, Subjects,AdminHOD


class AddCourseForm(ModelForm):
    class Meta:
        model=Courses
        fields='__all__'


class AddStaffsForm(ModelForm):
    class Meta:
        model = Staffs
        fields = '__all__'

class AddStudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

class AddSubjectsForm(ModelForm):
    class Meta:
        model=Subjects
        fields='__all__'

class addadminForm(ModelForm):
    class Meta:
        model = AdminHOD
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        models=User
        fields=['username', 'email', 'password1', 'password2']

