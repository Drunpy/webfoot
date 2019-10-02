from django.shortcuts import render
from core.models import Sessions
from django.http import Http404

# Poo teams on the same match
def core(request, session_token):
    session = Sessions.objects.filter(token=session_token)

    if not sesion.exists():
        raise Http404()