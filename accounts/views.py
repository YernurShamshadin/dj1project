from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
from accounts.models import CustomUser


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if 'birthdate' in request.POST:
            birthdate = request.POST['birthdate']
        else:
            birthdate = '2001-01-01'

        photo = request.POST['photo']

        if password1 == password2:
            user = CustomUser.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name, birthdate=birthdate, photo=photo)
            user.save()

            email = EmailMessage(
                'Hello',
                'Welcome to my site',
                'ernurshamshadin@gmail.com',
                [user.email],
            )
            email.attach_file('C:/Users/User/Desktop/graduation.jpg')

            new_user = authenticate(username=username,
                                    password=password1,
                                    )
            login(request, new_user)
            print("User created")

            email.send(fail_silently=False)

            return render(request, 'accounts/successfull.html')
        else:
            print("User not created")
            messages.info(request, 'Password not matching')



        return redirect('/')
    else:
        return render(request, 'accounts/register.html')

