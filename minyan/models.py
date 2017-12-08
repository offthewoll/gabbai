from django.db import models

class MinyanInfo(models.Model):
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE)
    public = models.BooleanField()

class Tefilla(models.Model):
    minyan = models.ForeignKey(MinyanInfo, on_delete=models.CASCADE)
    date = models.DateField()
    tefilla_type = models.ForeignKey('TefillaType', on_delete=models.CASCADE)

class MinyanSignup(models.Model):
    tefilla = models.ForeignKey(Tefilla, on_delete=models.CASCADE)
    userID = None #TODO create user table
    response = models.ForeignKey('MinyanResponse', on_delete=models.CASCADE)

class MinyanResponse(models.Model):
    '''Whether the user is coming to the minyan'''
    name = models.CharField(max_length=20)

class Venue(models.Model):
    '''Shiva minyan or regular'''
    name = models.CharField(max_length=10)

class TefillaType(models.Model):
    name = models.CharField(max_length=9)

class MinyanSchedule(models.Model):
    minyan = models.ForeignKey(MinyanInfo, on_delete=models.CASCADE)
    tefilla = models.ForeignKey(TefillaType, on_delete=models.CASCADE)
    time = models.TimeField()

class LainingStart(models.Model):
    '''How early should the minyan start on Monday and Thursday'''
    minyan = models.ForeignKey(MinyanInfo, on_delete=models.CASCADE)
    minutes_early = models.SmallIntegerField()

class MinchaMaariv(models.Model):
    '''Whether the Mincha minyan has Ma'ariv following'''
    minyan = models.ForeignKey(MinyanInfo, on_delete=models.CASCADE)
    minchamaariv = models.BooleanField()

class Shiva(models.Model):
    niftar_english = models.CharField(max_length=30)
    niftar_hebrew = models.CharField(max_length=60)
    mishnayos_url = models.URLField()