
fromm django import forms

class StudentFrom(forms.Form):
    student_name = forms.CharField(
        label="Student Name",
        max_length=100,
        widget=forms.TextInput()
    )

    student_id = forms.CharField(
        label="Student ID",
        max_length=20,
        widget=froms.TextInput()
    )

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
            ('sophmore', 'Sophmore'),
            ('junior', 'Junior'),
            ('senior', 'Senior'),
            ('graduate', 'Graduate'),
        ],
        wdiget=froms.RadioSelect()
    )

    programming_langauges = forms.MultipleChoiceField(
        label="Programming Langauges Known",
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
