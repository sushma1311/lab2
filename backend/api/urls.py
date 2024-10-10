from django.urls import path
from .views import CustomerSignupView, RestaurantSignupView  # Import your view classes

urlpatterns = [
    path('customer-signup/', CustomerSignupView.as_view(), name='customer-signup'),
    path('restaurant-signup/', RestaurantSignupView.as_view(), name='restaurant-signup'),
    # Add other API endpoints here
]