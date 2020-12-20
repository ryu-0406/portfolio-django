from django.views.generic import View
from django.shortcuts import render,redirect
from .models import Work, Skill
from .forms import ContactForm
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap


# Create your views here.



class IndexView(View):
    def get(self, request, *args, **kwargs):
        skill_data = Skill.objects.all()
        work_data = Work.objects.order_by("-id")
        form = ContactForm(request.POST or None)
        return render(request, 'app/index.html',{
            "skill_data": skill_data, 
            'work_data': work_data,
            'form': form
        })
        
    def post(self, request, *args, **kwargs):
        print('テスト')
        form = ContactForm(request.POST or None)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject2 = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            subject = 'お問い合わせありがとうございます。'
            content = textwrap.dedent('''
                ※このメールはシステムからの自動返信です。
                
                {name} 様
                
                お問い合わせありがとうございました。
                以下の内容でお問い合わせを受け付けいたしました。
                内容を確認させていただき、ご返信させて頂きますので、少々お待ちください。
                
                --------------------
                ■お名前
                {name}
                
                ■メールアドレス
                {email}

                ■タイトル
                {subject2}
                
                ■メッセージ
                {message}
                --------------------
                ''').format(
                    name=name,
                    email=email,
                    subject2=subject2,
                    message=message
                )

            to_list = [email]
            bcc_list = [settings.EMAIL_HOST_USER]

            try:
                message = EmailMessage(subject=subject, body=content, to=to_list, bcc=bcc_list)
                message.send()
            except BadHeaderError:
                return HttpResponse("無効なヘッダが検出されました。")

        return redirect('index') # 後で変更

        