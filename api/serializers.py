from rest_framework import serializers

from .models import User, Book

class UserListRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']


class UserCreateSerializer(serializers.ModelSerializer):
    book = BookSerializer(many=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'book']

    def create(self, validated_data):
        books_data = validated_data.pop('book')
        print(validated_data)
        print(books_data)
        user = User.objects.getcreate(**validated_data)
        for book_data in books_data:
            print(book_data)
            Book.objects.create(user=user, **book_data)
        return user
