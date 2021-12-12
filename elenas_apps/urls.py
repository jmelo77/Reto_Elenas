"""todo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token

from .api import router

# drf_yasg code starts here
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Elenas API",
        default_version='v1',
        description="Welcome to the API of Elenas",
        terms_of_service="https://www.elenas.la",
        contact=openapi.Contact(email="info@elenas.la"),
        license=openapi.License(name="Awesome API"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# ends here

v = settings.API_VERSION

urlpatterns = [
    # docs
    url(r'^doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url('doc/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    url('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),

    url(r'^admin/', admin.site.urls),

    # API
    # Auth endpoints
    url(r'^api/' + v + '/auth/refresh/', refresh_jwt_token, name='refresh_jwt_token'),
    url(r'^api/' + v + '/auth/token/', obtain_jwt_token, name='obtain_jwt_token'),
    # Router endpoints
    url(r'^api/' + v + '/', include((router.urls, 'api'), namespace='api')),

    # only for test purposes
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
