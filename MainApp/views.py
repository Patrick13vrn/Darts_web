from django.shortcuts import render
# from MainApp.darts import functions, game, player, start


def index(request):
    player_1 = 'Алексей'
    player_2 = 'Дмитрий'
    return render(request, 'MainApp/main.html', context={'player_1': player_1,
                                                         'player_2': player_2})
