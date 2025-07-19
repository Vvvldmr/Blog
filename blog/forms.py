from django import forms


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        strip=True,
        required=True,
        label='Заголовок поста',
        widget=forms.TextInput(attrs={
            'placeholder': 'максимальная длинна 200 символов',
            })
    )
    text = forms.CharField(
        label='Содержание поста', 
        widget=forms.Textarea(attrs={ 'rows': 3})
        )
    
def clean_title(self):
    title = self.cleaned_data['title'].strip()

    if len(title) < 5:
        raise forms.ValidationError("Заголовок не может быть меньше 5 символов")
    
    return title