from rest_framework import serializers
from .models import Cat, Comment

class CatSerializer(serializers.ModelSerializer):
    view_name='cat_name',
    many=True,
    read_only=True

    class Meta:
        model = Cat
        fields = ('id', 'name', 'favorite_food', 'loves_pets', 'photo_url')

class CommentSerializer(serializers.ModelSerializer):
    view_name='comment_body',
    many=True,
    read_only=True

    class Meta:
        model = Comment
        fields = ('id', 'author', 'body', 'cat')