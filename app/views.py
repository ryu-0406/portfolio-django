from django.views.generic import View
from django.shortcuts import render
from .models import Work, Skill

# Create your views here.



class IndexView(View):
    def get(self, request, *args, **kwargs):
        skill_data = Skill.objects.all()
        work_data = Work.objects.order_by("-id")
        return render(request, 'app/index.html',{
            "skill_data": skill_data, 
            'work_data': work_data
        })
        # profile_data = Profile.objects.all()
        # if profile_data.exists():
        #     profile_data = profile_data.order_by("-id")[0]
        # work_data = Work.objects.order_by("-id")
        # return render(request, 'app/index.html', {
        #     'profile_data': profile_data,
        #     'work_data': work_data
        # })