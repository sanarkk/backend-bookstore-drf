from rest_framework import serializers
from .models import book


class book_serial(serializers.ModelSerializer):
    user_name = serializers.CharField(source="author.username")

    class Meta:
        model = book
        fields = (
            "id",
            "book_name",
            "price",
            "user_name",
        )


class bookreate(serializers.Serializer):
    book_name = serializers.CharField()
    price = serializers.IntegerField()

    def create(self, validated_data):
        return book.objects.create(**validated_data)


class update_book(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = "__all__"