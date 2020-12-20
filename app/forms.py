from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='名前')
    email = forms.EmailField(max_length=100, label='メールアドレス')
    subject = forms.CharField(max_length=100, label='タイトル')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea())