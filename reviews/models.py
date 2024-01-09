from django.db import models
from users.models import User
from fragnances.models import Fragnance

class FragnanceReview(models.Model):
    fragnance = models.ForeignKey(
        Fragnance,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Духи',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.IntegerField(
        default=5,
        validators=[models.Min(1), models.Max(5)],
        verbose_name='Рейтинг',
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Отзыв о духах'
        verbose_name_plural = 'Отзывы о духах'

    def __str__(self):
        return f"{self.user.username} оценил {self.fragnance.title} - {self.rating}"