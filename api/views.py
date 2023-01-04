from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from base.models import *
from .serializers import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def AboutData(request):
    item = About.objects.all()
    serializer = AboutSerializers(item, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ServicesData(request):
    item = Services.objects.all()
    serializers = ServiceSerializers(item, many=True)
    return Response(serializers.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TestimonialsData(request):
    item = Testimonial.objects.all()
    serializers = TestimonialSerializers(item, many=True)
    return Response(serializers.data)


