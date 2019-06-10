from django.shortcuts import render

# Create your views here.
def SignUpUser(request):
    return render(request,'SignUp.html')

def SignInUser(request):
    return render(request,'SignIn.html')