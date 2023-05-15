from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from news.views import news_feed
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('booking/', include('booking.urls')),
    path('profiles/', include('profiles.urls')),
    path('scheduling/', include('scheduling.urls')),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name="contact"),
    path('services/', TemplateView.as_view(template_name="services.html"), name="services"),
    path('aboutus/', TemplateView.as_view(template_name="aboutus.html"), name="aboutus"),
    path('news/', include('news.urls', namespace='news')),
    path('login/', LoginView.as_view(), name='login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)