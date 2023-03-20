from django import forms

# creating a form
class InputForm(forms.Form):
    # first_name = forms.CharField(label="First Name",max_length=200)
    # last_name = forms.CharField(label="Last Name",max_length=200,required=False)
    # roll_number = forms.IntegerField(label="Roll No",help_text="Enter 6 digit roll number")
    # password = forms.CharField(label="Password",widget=forms.PasswordInput())
    file = forms.FileField(label="Browse File to upload")