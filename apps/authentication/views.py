from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.views import APIView


'''
    Login IN  Using SimpleJwt
'''
class LoginAPIView(ObtainAuthToken):
    permission_classes =[AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user  =serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key
        })
        

'''
    Logout Out 
'''

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # delete token
        token = Token.objects.get(user = request.user)
        token.delete()
        return Response(
            {'detail': 'Logout Successfully'}
        )