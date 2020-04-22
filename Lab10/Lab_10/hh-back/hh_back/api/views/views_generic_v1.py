from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from api.models import Company, Vacancy
from api.serializers import CompanySerializer2


class CompanyListAPIView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         generics.GenericAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CompanyDetailAPIView(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.GenericAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2
    lookup_url_kwarg = 'category_id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
