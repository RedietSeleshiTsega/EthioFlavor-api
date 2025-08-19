from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, CategoryViewSet, IngredientViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'ingredients', IngredientViewSet)

urlpatterns = router.urls