from django.shortcuts import render


def display_message(request):
    message = "Hello, this is the message you want to display!"
    return render(request, 'demo.html', {'message': message})

