from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):

    def create_user(self, email, name, password):
        if not email:
            raise ValueError("이메일을 다시 확인해 주세요.")
        
        user = self.model(
            email=self.nomalize_email(email),
            name=name,
            team=team
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name=name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):

    email = models.EmailField(verbose_name="email address", unique=True, max_length=255)
    name = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()