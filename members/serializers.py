
from rest_framework import serializers
from .models import PartyMember

class PartyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyMember
        fields = '__all__'

    def validate(self, data):
        qs = PartyMember.objects.filter(
            name=data['name'], contact_number=data['contact_number']
        )
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError(
                "Member with this name and phone number already exists."
            )
        return data
