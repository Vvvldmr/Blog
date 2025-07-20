from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "Максимальная длинна 200 символов"
            })
        }
        labels = {
            'title': 'Заголовок поста:',
            'content': 'Текст поста'
        }

def clean_title(self):
    title = self.cleaned_data["title"].strip()

    if len(title) < 5:
        raise forms.ValidationError('Должен быть более 5 символов')

    return title
            
            