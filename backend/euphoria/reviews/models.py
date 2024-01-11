from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from users.models import User
from fragnances.models import Fragnance

class FragnanceReview(models.Model):
    fragnance = models.ForeignKey(
        Fragnance,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Духи'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='Рейтинг',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )
    video_url = models.URLField(
        blank=True, null=True, verbose_name="URL видео"
    )
    image = models.ImageField(
        upload_to='review_images/',
        blank=True, null=True, verbose_name="Изображение"
    )

    class Meta:
        verbose_name = 'Отзыв о духах'
        verbose_name_plural = 'Отзывы о духах'

    def __str__(self):
        return f"{self.user.username} оценил {self.fragnance.title} - {self.rating}"

class ReviewComment(models.Model):
    review = models.ForeignKey(
        FragnanceReview, related_name="comments", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(
        FragnanceReview,
        related_name="likes",
        on_delete=models.CASCADE, null=True, blank=True
    )
    comment = models.ForeignKey(
        ReviewComment,
        related_name="likes",
        on_delete=models.CASCADE,
        null=True, blank=True
    )





class Order(models.Model):
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending'
    )

    def __str__(self):
        return f"Order {self.id} by {self.user}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    fragnance = models.ForeignKey(Fragnance, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.fragnance.title}"
    
class Rating(models.Model):
    fragnance = models.ForeignKey(
        Fragnance, on_delete=models.CASCADE, related_name='ratings'
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rating {self.score}/5 by {self.user} for {self.fragnance}"