from http import HTTPStatus

from django.db.models import Count, Avg, Sum
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .filters import FragnanceFilter
from .models import Fragnance, Favourite, ShoppingList, FragnanceComment
from .serializers import (
    FragnanceSerializer,
    FavouriteSerializer,
    ShoppingListSerializer,
    FragnanceCommentSerializer
)


class FragnanceViewSet(ReadOnlyModelViewSet):
    """Вьюсет духов."""

    queryset = Fragnance.objects.all()
    pagination_class = LimitOffsetPagination
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FragnanceFilter
    filterset_fields = ('title', 'brand')
    serializer_class = FragnanceSerializer

    @method_decorator(cache_page(60 * 15))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 15))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


    @action(
        detail=True,
        methods=("post",),
        url_path="add_favourites",
        url_name="add_favourites",
        permission_classes=(IsAuthenticated,)
    )
    def add_favourites(self, request, pk):
        fragnance = self.get_object()
        serializer = FavouriteSerializer(
            data={"user": request.user.id, "fragnance": pk}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTPStatus.CREATED)

    @action(
        detail=True,
        methods=("delete",),
        url_path="delete_favourites",
        url_name="delete_favourites",
        permission_classes=(IsAuthenticated,)
    )
    def delete_favourites(self, request, pk):
        user = request.user
        fragnance = Fragnance.objects.get(pk=pk)
        favourites = Favourite.objects.filter(
            user=user, fragnance=fragnance
        )
        if favourites.exists():
            favourites.delete()
            return Response(status=HTTPStatus.NO_CONTENT)
        return Response(status=HTTPStatus.BAD_REQUEST)


    @action(
        detail=False,
        methods=("get",),
        url_path="favourites",
        url_name="favourites",
        permission_classes=(IsAuthenticated,)
    )
    def favourites_list(self, request):
        user = request.user
        favourites = Favourite.objects.filter(user=user)
        serializer = FavouriteSerializer(favourites, many=True)
        return Response(serializer.data, status=HTTPStatus.OK)

    @action(
        detail=True,
        methods=("post",),
        url_path="add_shopping_list",
        url_name="add_shopping_list",
        permission_classes=(IsAuthenticated,)
    )
    def add_to_shopping_list(self, request, pk):
        fragnance = self.get_object()
        if fragnance.available:
            serializer = ShoppingListSerializer(
                data={"user": request.user.id, "fragnance": pk}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTPStatus.CREATED)
        return Response(
            {"detail": "Нет в наличии."},
            status=HTTPStatus.BAD_REQUEST
        )

    @action(
        detail=True,
        methods=("delete",),
        url_path="delete_shopping_list",
        url_name="delete_shopping_list",
        permission_classes=(IsAuthenticated,)
    )
    def remove_from_shopping_list(self, request, pk):
        shopping_list_item = ShoppingList.objects.filter(
            user=request.user, fragnance_id=pk
        )
        if shopping_list_item.exists():
            shopping_list_item.delete()
            return Response(status=HTTPStatus.NO_CONTENT)
        return Response(status=HTTPStatus.BAD_REQUEST)


    @action(
        detail=False,
        methods=("get",),
        url_path="shopping_list",
        url_name="shopping_list",
        permission_classes=(IsAuthenticated,)
    )
    def shopping_list(self, request):
        user = request.user
        shopping_list = ShoppingList.objects.filter(user=user)
        serializer = ShoppingListSerializer(shopping_list, many=True)
        return Response(serializer.data, status=HTTPStatus.OK)
#  Отзывы
    @action(
        detail=True,
        methods=("post",),
        url_path="add_comment",
        url_name="add_comment",
        permission_classes=(IsAuthenticated,)
    )
    def add_comment(self, request, pk):
        fragnance = self.get_object()
        serializer = FragnanceCommentSerializer(
            data=request.data,
            context={"request": request, "fragnance": fragnance}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, fragnance=fragnance)
        return Response(serializer.data, status=HTTPStatus.CREATED)

    @action(
        detail=True,
        methods=("delete",),
        url_path="delete_comment",
        url_name="delete_comment",
        permission_classes=(IsAuthenticated,)
    )
    def delete_comment(self, request, pk):
        comment = FragnanceComment.objects.get(pk=pk)
        comment.delete()
        return Response(status=HTTPStatus.NO_CONTENT)


    @action(
        detail=True,
        methods=("get",),
        url_path="comments_list",
        url_name="comments_list",
        permission_classes=(IsAuthenticated,)
    )
    def comments_list(self, request, pk):
        fragnance = self.get_object()
        comments = FragnanceComment.objects.filter(fragnance=fragnance)
        serializer = FragnanceCommentSerializer(comments, many=True)
        return Response(serializer.data, status=HTTPStatus.OK)