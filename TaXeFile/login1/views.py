import pyautogui
from django.shortcuts import render
# Create your views here.
def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        from django.contrib import auth
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            pyautogui.alert("Worng Username or Password")
            return render(request, 'login.html')
    else:
        return render(request, 'form.html')
