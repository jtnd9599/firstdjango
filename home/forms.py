from django import forms

class customForms(forms.Form):
    username=forms.CharField(
        label='username',
        widget=forms.TextInput(
            attrs={'placeholder':'yourname',
            'class':'form-control','max':'20'}
        )
    )
    email=forms.EmailField(
        label='your email',
        widget=forms.EmailInput(
            attrs={'placeholder':'ac@mail.com',
            'class':'forms-control',
            }
        )
    )
                        