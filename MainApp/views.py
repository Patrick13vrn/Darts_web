from django.shortcuts import render
from django.views.generic import View
from .forms import PostScore


# from MainApp.darts import functions, game, player, start


def index(request):
    player_1 = 'Алексей'
    player_2 = 'Дмитрий'

    return render(request, 'MainApp/main.html', context={'player_1': player_1,
                                                         'player_2': player_2
                                                         })


def player_throw(request):
    pass


class MainPage(View):
    template = 'MaiApp/base_main.html'

    def get(self, request):
        form = PostScore()
        return render(request, self.template, {'form': form})
