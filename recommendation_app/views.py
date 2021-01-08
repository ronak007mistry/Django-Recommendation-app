from django.shortcuts import render
from .models import UserLocation, UserPreference, Users

# Create your views here.



def index(request):
    users = Users.objects.all()
    context = {"users": users,}
# Getting the selected user from the list 

    range_of_preference_user = []
    final_value = set()
    myset = set()

    username = request.GET.get('username', False)
    if username:

        selected_user = Users.objects.get(pk=username)
        print("selected username ",selected_user.name)


        # Getting all the preferred values from the selected user


        userpreference = UserPreference.objects.get(user_id=username)
        preferred_gender = userpreference.gender
        preferred_max_age = userpreference.max_age
        preferred_max_distance = userpreference.max_distance
        preferred_max_distance *= preferred_max_distance
        user_location = UserLocation.objects.get(user_id=username)
        preferred_location = user_location.coordinates
        coordinates = preferred_location.split(',')
        x_coordinate = coordinates[0]
        y_coordinate = coordinates[1]
        x_coordinate.strip()
        y_coordinate.strip()
        x_cor = float(x_coordinate)
        y_cor = float(y_coordinate)
        # print(x_cor, y_cor)

        # Getting the locations of all the users in x and y coordinates

        
        
        for user in users:
            if user.id == selected_user.pk:
                continue

            myuser1 = UserLocation.objects.get(user_id=user.id)
            location1 = myuser1.coordinates
            coordinates1 = location1.split(',')
            x_coordinate1 = coordinates1[0]
            y_coordinate1 = coordinates1[1]
            x_coordinate1.strip()
            y_coordinate1.strip()
            x_corr = float(x_coordinate1)
            y_corr = float(y_coordinate1)
            distance1 = (x_corr - x_cor)**2 + (y_corr - y_cor)**2
            if distance1 <= preferred_max_distance:
                range_of_preference_user.append(user.name)
                myset.add(user)

            # Getting the users from preferred age and preferred gender

            preferred_users = Users.objects.filter(age__lte=preferred_max_age, sex=preferred_gender)
            
            
            # Getting the final list of user having met all the 3 conditions including the preferred distance


            for i in preferred_users:
                if i in myset:
                    final_value.add(i)

        context = {"users": users, "final_value": final_value}
    
    return render(request, 'recommendation_app/index.html', context=context)
        


        

