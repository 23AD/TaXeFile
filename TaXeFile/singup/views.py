import pyautogui
from django.contrib.auth.models import User
from django.shortcuts import render
# Create your views here.
def singup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['password']

        x = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                     password=password)
        x.save()
        pyautogui.alert("User is Created")

        return render(request, 'login.html')

    else:
        return render(request, 'singup.html')
