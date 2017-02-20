from tastypie.resources import ModelResource
from tastypie.constants import ALL

from ReACT_API.models import Atleta


class AtletaResource(ModelResource):
    class Meta:
        queryset = Atleta.objects.all()
        resource_name = 'ReACT_API'
