from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='名前')
    email = forms.EmailField(max_length=100, label='メールアドレス')
    subject = forms.CharField(max_length=100, label='タイトル')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea())

# class PostForm(forms.Form):
#     title = forms.CharField(max_length=30, label='タイトル')
#     content = forms.CharField(label='内容', widget=forms.Textarea())
#     image = forms.ImageField(label='イメージ画像', required=False) # 追加