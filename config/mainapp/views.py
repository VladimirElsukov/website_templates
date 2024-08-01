from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    return render(request, 'index.html', {'greeting': 'Hello, world!'})

def language(request, lang):
    if lang == 'fr':
        return render(request, "index.html", {"greeting": "Bonjour, monde!"})
    elif lang == 'de':
        return render(request, "index.html", {"greeting": "Hallo, Welt!"})
    elif lang == 'es':
        return render(request, "index.html", {"greeting": "¡Hola, mundo!"})
    else:
        return render(request, "index.html", {"greeting": "Hello, world!"})
