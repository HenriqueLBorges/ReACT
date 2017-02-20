from django.conf.urls import url, include
from django.contrib import admin

from ReACT_API.api import AtletaResource

atleta_resource = AtletaResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(atleta_resource.urls)),
]
