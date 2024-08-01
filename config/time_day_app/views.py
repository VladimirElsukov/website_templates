from django.shortcuts import render
from datetime import datetime


def time_view(request):
    current_hour = datetime.now().hour  # Получаем текущий час
    
    if 6 <= current_hour < 9:
        greeting = "Доброе утро!"
    elif 9 <= current_hour < 15:
        greeting = "Добрый день!"
    elif 15 <= current_hour < 21:
        greeting = "Добрый вечер!"
    else:
        greeting = "Ночь!"

    return render(request, "time.html", {"greeting": greeting})
