from django.shortcuts import render
from django.http import HttpResponse
from game.models.game import Sessions
from django.http import Http404

from game.models.game import Teams
from game.algs.battle_alg import TeamBattle

# call GET with
# http://127.0.0.1:8000/play/?team_one=2&team_two=3
def play(request):
    team_one_id = request.GET.get('team_one')
    team_two_id = request.GET.get('team_two')

    team_one_obj = Teams.objects.filter(id=team_one_id).first()
    team_two_obj = Teams.objects.filter(id=team_two_id).first()

    winner_team = TeamBattle().compute_result(team_one_obj, team_two_obj)

    return HttpResponse(winner_team)

# Poo teams on the same match
def core(request, session_token):
    session = Sessions.objects.filter(token=session_token)

    if request.method == 'GET':
        if not session.exists():
            raise Http404()

def home(request, session_token):
    session = Sessions.objects.filter(token=session_token)

    if request.method == 'GET':
        if not session.exists():
            raise Http404()

def about(request, session_token):
    session = Sessions.objects.filter(token=session_token)

    if request.method == 'GET':
        if not session.exists():
            raise Http404()

def terms(request):
    return ''

def help(request):
    return ''
