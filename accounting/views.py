from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from accounting.serializers import InternRegisterSerializer
from accounting.permissions import IsAdminOrReadOnly


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RegisterIntern(APIView):
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly)

    def post(self, request):
        ser_data = InternRegisterSerializer(data=request.POST, partial=True)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            return Response({'msg': 'success'}, status=status.HTTP_201_CREATED)

        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
