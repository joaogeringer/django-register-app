from django.shortcuts import render
from .models import User

def home(request):
    return render(request, 'users/home.html')

def users(request):
    new_user = User()
    new_user.name = request.POST.get('name')
    new_user.age = request.POST.get('age')
    new_user.save()
    # Shows every created users on a new page
    users = {
    'users': User.objects.all()
}
    # Return datas for the listing users page
    return render(request,'users/users.html',users)