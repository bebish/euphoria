from django.db import models
from django.db.models import CheckConstraint, UniqueConstraint

from users.models import User

class Subscribe(models.Model):
    """Модель подписки."""

    user = models.ForeignKey(
        User,
        related_name="follower",
        on_delete=models.CASCADE,
        null=True,
        help_text="Подписчик автора",
    )
    author = models.ForeignKey(
        User,
        related_name="author",
        on_delete=models.CASCADE,
        null=True,
        help_text="Автор",
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        constraints = [
            UniqueConstraint(
                fields=["author", "user"],
                name="re-subscription"
            ),
            CheckConstraint(
                name="prevent_self_subscription",
                check=~models.Q(user=models.F("author")),
            )]

    def __str__(self):
        return "{} подписан на {}".format(self.user, self.author)