from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework.exceptions import ValidationError

from users.models import User


class Fragnance(models.Model):
    title = models.CharField(max_length=40)
    brand = models.CharField(max_length=35)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, default='Товар')
    sex = models.CharField(max_length=8, default='Унисекс')
    image = models.ImageField(
        "Изображение духов", upload_to="fragnances/"
    )
    size = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    rating = models.IntegerField(
        validators=(MinValueValidator(0), MaxValueValidator(5))
    )
    description = models.CharField(max_length=450)
    class Meta:
        verbose_name = "Духи"
        verbose_name_plural = "Духи"

class FragnanceComment(models.Model):
    fragnance = models.ForeignKey(
        Fragnance, on_delete=models.CASCADE, related_name='comments'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.FloatField(
        validators=(MinValueValidator(0), MaxValueValidator(5))
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    class Meta:
        verbose_name = "Отзывы про духи"
        verbose_name_plural = "Отзывы про духи"

class FavouriteShoppingFragnance(models.Model):
    """Абстрактный класс для покупок и избранного."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",

    )
    fragnance = models.ForeignKey(
        Fragnance,
        on_delete=models.CASCADE,
        verbose_name="Духи",
    )

    class Meta:
        abstract = True

    def clean(self):
        if self.__class__.objects.filter(
                user=self.user, fragnance=self.fragnance
        ).exists():
            raise ValidationError(
                "Пользователь уже добавил эти духи."
            )
        if self.__class__.objects.filter(
                user=self.user, name=self.fragnance
        ).exists():
            raise ValidationError(
                "Пользователь уже имеет список с таким именем."
            )
        return super().save(self)

    def __str__(self):
        return "{} В {} у {}".format(
            self.fragnance, self.__str__(), self.user
        )


class Favourite(FavouriteShoppingFragnance):
    """Наследник абстрактного класса для избранного."""
    class Meta(FavouriteShoppingFragnance.Meta):
        default_related_name = "favourites_fragnances"
        verbose_name = "Избранные духи"
        verbose_name_plural = "Избранные духи"


class ShoppingList(FavouriteShoppingFragnance):
    """Наследник абстрактного класса для покупок."""
    class Meta(FavouriteShoppingFragnance.Meta):
        default_related_name = "shopping_list"
        verbose_name = "Список для покупок"
        verbose_name_plural = "Списки для покупок"