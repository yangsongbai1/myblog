from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManage(BaseUserManager):
    def _create_user(self, telephone, username, password, **kwargs):
        if not telephone:
            raise ValueError('必须要传递手机号')
        if not password:
            raise ValueError('必须要输入密码')
        user = self.model(telephone=telephone, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone, username, password, id_superuser=False, **kwargs):
        kwargs['is_superuser'] = id_superuser
        return self._create_user(telephone=telephone, username=username, password=password, **kwargs)


class User(AbstractUser):
    telephone = models.CharField(max_length=11, unique=True)
    profession = models.CharField(max_length=100)

    USERNAME_FIELD = 'telephone'
    objects = UserManage()

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
