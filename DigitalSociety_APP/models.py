from django.db import models
#import django.utils.timezone as timezone

class Role(models.Model):
    Name = models.CharField(max_length=20)

    class Meta:
        db_table = 'role'

    def __str__(self):
        return self.Name

class Master(models.Model):
    Role = models.ForeignKey(Role, on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)
    Mobile = models.CharField(max_length=10, default="")
    IsActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'master'

class Society_member(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=20, default="")
    Mobile = models.CharField(max_length=10, default="")
   # Gender = models.CharField(max_length=15, choices=gender_choice)
   # DoB = models.DateField(auto_created=True, default=timezone.now)

    class Meta:
        db_table = 'society_member'

class Society_secretary(models.Model):
    Master = models.ForeignKey(Master, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=20, default="")
    Mobile = models.CharField(max_length=10, default="")
   # Gender = models.CharField(max_length=15, choices=gender_choice)
   # DoB = models.DateField(auto_created=True, default=timezone.now)

    class Meta:
        db_table = 'society_secretary'
