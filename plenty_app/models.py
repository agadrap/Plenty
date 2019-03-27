from django.db import models

smell_level = (
    (0, "No smell"),
    (1, "Subtle flowers smell"),
    (2, "Intense flowers smell"),
    (3, "Unpleasant flowers smell"),
    (4, "Intense plant smell")
)

sun_exposure = (
    (5, "Very sunny"),
    (4, "Sunny except noon"),
    (3, "Usually sunny, tolerant, east side"),
    (2, "Sunny except noon"),
    (1, "Sunny but not direct, north side"),
    (0, "In the shadows")
)

difficulty = (
    (1, "Easy"),
    (2, "Moderate"),
    (3, "Intermediate"),
    (4, "Expert")
)

seasons = (
    (1, "winter"),
    (2, "spring"),
    (3, "summer"),
    (4, "autumn")
)
periods = (
    (1, "weekly"),
    (2, "monthly"),
    (3, "quarterly")
)
time_periods = (
    (1, "yearly"),
    (2, "once every 2-3 years"),

)
months = (
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "Novemer"),
    (12, "December")
)

class Plant(models.Model):
    name = models.CharField(max_length=100)
    latin_name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    illustration = models.CharField(max_length=200, null=True) #static/images/file.jpeg

    def __str__(self):
        return 'name: {}, latin: {}'.format(self.name, self.latin_name)

class PlantHumidity(models.Model):
    activity = models.CharField(null=True, max_length=100) #spray everyday // spray once a week // flowerpot on wet stones
    season = models.IntegerField(choices=seasons,null=True)
    watchout = models.TextField(null=True)

class PlantTemperature(models.Model):
    minimum_C = models.IntegerField(null=True)
    maximum_C = models.IntegerField(null=True)
    season = models.IntegerField(choices=seasons,null=True)

class PlantWatering(models.Model):
    occurrence = models.IntegerField(null=True)
    time_period = models.IntegerField(null=True,choices=periods)
    season = models.IntegerField(choices=seasons,null=True)

class Replanting(models.Model):
    occurrence = models.IntegerField(null=True)
    time = models.IntegerField(choices=time_periods,null=True)
    season = models.IntegerField(choices=seasons,null=True)
    month = models.IntegerField(choices=months,null=True)
    description = models.TextField(null=True)

class PlantDetails(models.Model):
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE)
    blooming = models.TextField(null=True)
    smell = models.IntegerField(choices=smell_level)
    light = models.IntegerField(choices=sun_exposure)
    humidity_level = models.ForeignKey(PlantHumidity,null=True,on_delete=models.CASCADE)
    temperature = models.ForeignKey(PlantTemperature,null=True,on_delete=models.CASCADE)

class PlantCare(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    water = models.ForeignKey(PlantWatering,null=True,on_delete=models.CASCADE)
    replanting = models.ForeignKey(Replanting,on_delete=models.CASCADE)
    cutting = models.TextField(null=True)
    care_difficulty = models.IntegerField(choices=difficulty)

