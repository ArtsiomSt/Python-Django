from django.db import models

class TelegramQA(models.Model):
    tguser = models.CharField(null=True,blank = True,max_length=50, verbose_name='Пользователь')
    question = models.TextField(null=True, blank=True, verbose_name='Вопрос')
    answer = models.TextField(null=True, blank=True, verbose_name='Ответ')
    is_answered = models.BooleanField(default=False, blank=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.tguser
