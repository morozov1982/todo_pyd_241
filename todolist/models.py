from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Категория',
                            unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class TodoList(models.Model):
    title = models.CharField(max_length=250,
                             verbose_name='Задача')
    content = models.TextField(blank=True,
                               verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True)
    category = models.ForeignKey(Category,
                                 # default='general',
                                 on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created']
