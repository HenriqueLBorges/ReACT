from django.conf.urls import url, include
from django.contrib import admin
from ReACT_API.api import AtletaResource
from django.http.request import (
    HttpRequest, QueryDict, RawPostDataException, UnreadablePostError,
)

atleta_resource = AtletaResource()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(atleta_resource.urls)),
    '''url(HttpResponse.GET, include(atleta_resource.urls)),
    if request.method == "GET":
        include(atleta_resource.urls)'''
]
