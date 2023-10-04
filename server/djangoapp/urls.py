from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # Default homepage view
       path('', views.get_dealerships, name='index'),  # Define an 'index' URL pattern


    # About page view
    path('about/', views.about, name='about'),

    # Contact Us page view
    path('contact/', views.contact, name='contact'),

    # Registration page view
    path('registration/', views.registration_request, name='registration'),

    # Login page view
    path('login/', views.login_request, name='login'),

    # Logout page view
    path('logout/', views.logout_request, name='logout'),

    # Add a Review page view
    path('add_review/', views.add_review, name='add_review'),
        # path for dealer reviews view
    path('dealer/<int:id>/', views.get_dealer_details, name='dealer_details')
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
