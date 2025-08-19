from rest_framework import serializers
from .models import Recipe, Category, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ingredient.objects.all()
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'instructions',
            'ingredients', 'category', 'prep_time',
            'cook_time', 'servings', 'created_at', 'owner'
        ]
        read_only_fields = ['owner', 'created_at']

    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError("Title is required.")
        if not data.get('ingredients'):
            raise serializers.ValidationError("At least one ingredient is required.")
        if not data.get('instructions'):
            raise serializers.ValidationError("Instructions are required.")
        return data