from django.shortcuts import render


def index(request):
    player_1 = 'Алексей'
    player_2 = 'Дмитрий'
    return render(request, 'MainApp/wrapper.html', context={'player_1': player_1,
                                                            'player_2': player_2})
