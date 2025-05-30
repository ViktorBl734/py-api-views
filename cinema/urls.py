from django.urls import path
from rest_framework import routers

from cinema.views import  GenreList, GenreDetail, ActorList, ActorDetail, CinemaHallViewSet, \
    MovieViewSet

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"}
)
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={"get": "retrieve", "put": "update", "patch": "partial_update"}
)
router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
urlpatterns = [
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallViewSet.as_view({"get": "list",
        "post": "create"}), name="cinema-hall-list"),

    path("cinema_halls/<int:pk>/", CinemaHallViewSet.as_view(
        {"get": "retrieve", "put": "update", "patch": "partial_update",
        "delete": "destroy"}), name="cinema-hall-detail"),] +  router.urls

app_name = "cinema"
