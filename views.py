from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema
from .models import Product
from .serializers import ProductSerializer


@extend_schema(tags=['product'])
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, parsers
from drf_spectacular.utils import extend_schema, OpenApiTypes     
from .serializers import ProductSerializer


class ProductCreateView(APIView):
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]  # muhim!

    @extend_schema(
        request={
            'multipart/form-data': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'image': {'type': 'string', 'format': 'binary'},  # image uchun
                },
                'required': ['name', 'image'],
            }
        },
        responses={201: ProductSerializer},
    )
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)