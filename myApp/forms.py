
from django import forms

class StudentForm(forms.Form):
    student_name = forms.CharField(
        # must not be blank
        label="Student Name",
        max_length=100,
        widget=forms.TextInput(),
        required=True,
    )
    def clean_student_name(self):
        name = self.cleaned_data['student_name']
        if not name:
            raise forms.ValidationError('This is a required field')
        return name

    student_id = forms.CharField(
        #must not be blank
        label="Student ID",
        max_length=20,
        widget=forms.TextInput(),
        required=True
    )

    def clean_student_id(self):
        student_id = self.cleaned_data['student_id']

        if not student_id:
            raise forms.ValidationError('This is a required field')
        
        return student_id

    major = forms.ChoiceField(
        label="Major",
        choices=[
            ('cs', 'Computer Science'),
            ('it', 'Information Technology'),
            ('engineering', 'Engineering'),
            ('business', 'Business'),
            ('liberal arts', 'Liberal Arts'),
        ],
        widget=forms.Select()
    )

    class_standing = forms.ChoiceField(
        label="Class Standing",
        choices=[
            ('freshman', 'Freshman'),
            ('sophomore', 'Sophomore'),
            ('junior', 'Junior'),
            ('senior', 'Senior'),
            ('graduate', 'Graduate'),
        ],
        widget=forms.RadioSelect()
    )

    programming_languages = forms.MultipleChoiceField(
        label="Programming Languages Known",
        choices=[
            ('python', 'Python'),
            ('rust', 'Rust'),
            ('javascript', 'JavaScript'),
            ('c', 'C'),
            ('golang', 'GoLang')
        ]
    )

    graduation_year = forms.IntegerField(
        label='Expected Graduation Year',
        widget=forms.NumberInput()
    )

    comments = forms.CharField(
        label="Comments",
        required=False,
        widget=forms.Textarea()
    )
