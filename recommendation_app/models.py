from django.db import models

# Create your models here.



class Users(models.Model):
    name = models.CharField(max_length=100)
    sex = models.TextField()
    age = models.IntegerField()

    def __str__(self):
         return str(self.name)

    class Meta:
        verbose_name_plural = "Users"



class UserLocation(models.Model):
    coordinates = models.CharField(max_length=100)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user_id) +" " + str(self.coordinates)


class UserPreference(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    gender = models.TextField()
    max_age = models.IntegerField()
    max_distance = models.IntegerField()

    def __str__(self):
        return str(self.user_id)





    