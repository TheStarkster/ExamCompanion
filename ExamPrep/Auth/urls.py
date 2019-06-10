from django.urls import path

urlpatterns = [
    path('SignUp/',views.SignUpUser),
    path('SIgnIn/',views.SignInUser)
]