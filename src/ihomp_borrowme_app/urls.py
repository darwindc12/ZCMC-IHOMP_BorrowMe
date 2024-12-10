from django.urls import path
from . import views

# Setting up the URLs for the app's pages and API endpoints
urlpatterns = [
    # Home page route that shows the department, category, and peripheral lists
    path('', views.OverviewPageView.as_view(), name='homepage'),

    # Route for handling the borrowing form submission
    path('borrow/', views.handle_borrow_request, name='borrow_form'),

    # API route to get available peripherals based on selected category
    path('fetch_peripherals/<int:category_id>/', views.fetch_peripherals, name='fetch_peripherals'),

    # API route to get unique numbers for a specific peripheral
    path('unique_numbers/<int:peripheral_id>/', views.get_peripheral_unique_numbers, name='get_unique_numbers'),
]
