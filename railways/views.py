from django.shortcuts import render

# Create your views here.

from django.contrib.auth import authenticate, login, logout


def login_user(request):
    template_name = 'railways/login.html'

    if request.method == 'GET':
        return render(request, template_name, {})

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return render(request, template_name, {'user': user})
        else:
            # Return an 'invalid login' error message.
            return


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, 'railways/login.html', {})
