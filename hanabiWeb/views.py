from django.shortcuts import render
from django.http import HttpResponse
from hanabiWeb import game

firstplayerarray = []

def start(request):
    stato = game.State()
    for i in stato.playerarray[0].hand:
        firstplayerarray.append(i[1])

    return HttpResponse("Hello world")

def hello(request):

    return render(request,'game.html',{'handcolors': firstplayerarray})