from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PartyMember
from .serializers import PartyMemberSerializer
from django.contrib.auth import get_user_model
from rest_framework import status

class PartyMemberViewSet(viewsets.ModelViewSet):
    queryset = PartyMember.objects.all()
    serializer_class = PartyMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Admin sees all; users see all as well but you may restrict later
        return PartyMember.objects.all()

class UnitNameListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        units = PartyMember.objects.order_by('unit').values_list('unit', flat=True).distinct()
        units = list(filter(None, units))
        return Response(units)

User = get_user_model()

class SingleUserSignup(APIView):
    authentication_classes = []  # Allow anyone for signup
    permission_classes = []      # Allow anyone for signup

    def post(self, request):
        if User.objects.exists():
            return Response({"detail": "Signup is disabled after the first user is created."}, status=status.HTTP_403_FORBIDDEN)
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email", "")
        if not username or not password:
            return Response({"detail": "Username and password required."}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password, email=email)
        return Response({"detail": "User created successfully."}, status=status.HTTP_201_CREATED)