from django.shortcuts import render
from .models import UserLocation, UserPreference, Users

# Create your views here.


def index(request):
    users = Users.objects.all()

    # username = request.GET['username']
    # print(username)
    context = {"users": users}
    return render(request, 'recommendation_app/index.html', context=context)
    