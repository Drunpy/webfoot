from django.shortcuts import render



def new_math_or_continue(request):
    return render(
        request,
        template_name="core/pre_game/index.html"
    )