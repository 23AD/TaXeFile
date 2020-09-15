import pyautogui
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def form(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        tel = request.POST['tel']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        birthday = request.POST['birthday']
        aadhar = request.POST['aadhar']
        file = request.POST['file']
        pan = request.POST['pan']
        file1 = request.POST['file1']
        account = request.POST['account']
        ifsccode = request.POST['ifsccode']
        x = User.objects.create_user(firstname=firstname, lastname=lastname, email=email, tel=tel, address=address,
                                     city=city, state=state, pincode=pincode, birthday=birthday, aadhar=aadhar,
                                     file=file
                                     , pan=pan, file1=file1, account=account, ifsccode=ifsccode)
        x.Save()
        pyautogui.alert("Detailed is Save")

        return render(request, 'index.html')
    else:
        return render(request, 'form.html')
