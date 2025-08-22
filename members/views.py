from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PartyMember
from .serializers import PartyMemberSerializer

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

