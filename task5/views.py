from django.shortcuts import render
from .forms import UserRegister


users = ['user1', 'user2', 'user3']

def sign_up_by_django(request):
    info = {}
    form = UserRegister(request.POST or None)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))

        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            users.append(username)
            info['message'] = f'Приветствуем, {username}! Вы успешно зарегистрированы.'

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', context=info)

def sign_up_by_html(request):
    info = {}
    form = UserRegister(request.POST or None)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))

        if username in users:
            info['error'] = 'Пользователь уже существует'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            users.append(username)
            info['message'] = f'Приветствуем, {username}! Вы успешно зарегистрированы.'

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', context=info)
