from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from cinema.models import Movie, Genre
from cinema.serializers import MovieSerializer


class GenreList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serialize(


