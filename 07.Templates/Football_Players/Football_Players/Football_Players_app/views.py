from django.shortcuts import render
from . import models


def index(response):
    players = models.Player.objects.all()

    context = {
        'players': players
    }

    return render(request=response, template_name='index.html', context=context)


def player_page(response, name):
    players = models.Player.objects.all()

    if name in (player.name for player in players):
        player = models.Player.objects.filter(name=name).get()

        context = {
            'player': player
        }

        return render(request=response, template_name='player-page.html', context=context)
    else:
        return render(request=response, template_name='404.html')