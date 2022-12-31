from django.shortcuts import render


def skills(request):
    context={'skill':'active'}
    return render(request,'skills/skills.html',context)
