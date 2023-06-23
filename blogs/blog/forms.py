from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post    #Post 객체 생성
        fields = ['title', 'content', 'photo', 'category']
        labels = {  #글쓰기 폼에 영어를 한글로 변경
            'title': '제목',
            'content': '내용',
            'photo': '사진',
            'category': '분류'
        }