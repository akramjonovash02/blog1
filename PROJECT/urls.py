from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mainApp.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('about/', About.as_view(), name='about'),
    path('talks', TalksView.as_view(), name='talks'),
    path('blog/<int:blog_id>/', MaqolaView.as_view(), name='maqola')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
