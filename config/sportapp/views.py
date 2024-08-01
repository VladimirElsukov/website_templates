from django.shortcuts import render


# Create your views here.
def sport(request):
    return render(request, "base.html", {"greeting": "Главная-страница о спорте"})

def nav_sport(request, sp):
    if sp == 'football':
        return render(
            request, "base.html", {"greeting": "Футбол"}
        )
    elif sp == 'hockey':
        return render(request, "base.html", {"greeting": "Хоккей"})
    elif sp == 'basketball':
        return render(
            request, "base.html", {"greeting": "Баскетбол"}
        )
    else:
        return render(request, "base.html", {"greeting": "Главная-страница о спорте"})
