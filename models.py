from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Userprofile(models.Model):
    current_user = models.OneToOneField(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.current_user.username


class buy(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    ordered = models.BooleanField(default=False)
    ordered_by = models.ManyToManyField(Userprofile, null=True)
    remain = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('tovar', kwargs={"tovar_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class nomerz(models.Model):
    num = models.FloatField(null=True, blank=True)

class category(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Тип')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title
