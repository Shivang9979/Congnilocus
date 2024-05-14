from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, birthdate=None, gender=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          birthdate=birthdate, gender=gender)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, birthdate=None, gender=None):
        user = self.create_user(email, username, password, birthdate, gender)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(max_length=30)
    birthdate = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[(
        "Male", "Male"), ("Female", "Female"), ("Other", "Other")], blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class QuizQuestion(models.Model):
    Q_id = models.CharField(max_length=10)
    Question = models.TextField()
    primaryfact = models.CharField(max_length=1)
    otherfact = models.CharField(max_length=10, blank=True)
   


class MultiFactorQuestion(models.Model):
    Q_id = models.CharField(max_length=10)
    Question = models.TextField()
    primaryfacts = models.CharField(max_length=10)
    otherfacts = models.CharField(max_length=10, blank=True)


class Factor(models.Model):
    code = models.CharField(max_length=1)
    name = models.CharField(max_length=20)


class Job(models.Model):
    interest_code = models.CharField(max_length=3)
    occupation = models.CharField(max_length=50)


# from django.contrib.auth.models import User  # Import Django's User model

# class UserResponse(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
#     choice = models.IntegerField()
#     # You can add fields to store points or any other relevant data
