from django.shortcuts import render

# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
    return render(request,'login.html')

def createaccounts(request):
    return render(request,'createaccounts.html')    