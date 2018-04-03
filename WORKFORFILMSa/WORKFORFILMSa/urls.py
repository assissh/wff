"""WORKFORFILMSa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user.views import home


urlpatterns = [
    path('page/', include('pages.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls')),
    path('help_center/', include('help_center.urls'),name = 'help_center'),
    path('help_category/', include('help_category.urls')),
    path('help_Qna/', include('help_Qna.urls')),
    path('help_subcategory/', include('help_subcategory.urls')),
    path('Letter_pdf/', include('Letter_pdf.urls')),
    path('Location/', include('Location.urls')),
    path('Location_Amenitie/', include('Location_Amenitie.urls')),
    path('Location_Authoritie/', include('Location_Authorities.urls')),
    path('Location_Category/', include('Location_Category.urls')),
    path('prop/', include('Prop.urls')),
    path('quick_requirments/', include('Quick_Requirements.urls')),
    path('rating/', include('Ratings.urls')),
    path('review/', include('Review.urls')),
    path('search/', include('Search.urls')),
    path('', home,name='home'),





]
