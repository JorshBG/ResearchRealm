"""
URL configuration for ResearchRealm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from django.views.decorators.cache import cache_page
from django.conf.urls.static import static
from django.conf import settings
# from pwa import views as pwa_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login),
    path('register', views.register),
    path('profile', views.profile),
    path('thesis/create', views.create_thesis),
    path('thesis/all', views.index_thesis),
    path('thesis/<int:id>', views.get_thesis),
    path('thesis/update/<int:id>', views.update_thesis),
    path('', include('pwa.urls')),
    path('', include('ScholarStack.urls')),
]


# handler404 = 'ResearchRealm.views.handler404'
# handler500 = 'ResearchRealm.views.handler500'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
