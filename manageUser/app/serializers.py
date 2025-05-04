from rest_framework import serializers
from .models import ToolUser, OrganizationGroup, ToolUserGroup
from django.contrib.auth.hashers import make_password


class OrganizationGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationGroup
        fields = ['id', 'name', 'code']


class ToolUserGroupSerializer(serializers.ModelSerializer):
    group = OrganizationGroupSerializer(read_only=True)
    group_id = serializers.PrimaryKeyRelatedField(
        queryset=OrganizationGroup.objects.all(), source='group', write_only=True
    )

    class Meta:
        model = ToolUserGroup
        fields = ['id', 'user', 'group', 'group_id', 'date_assigned']
        read_only_fields = ['id', 'user', 'group', 'date_assigned']


class ToolUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    groups_m2m = serializers.PrimaryKeyRelatedField(
        queryset=OrganizationGroup.objects.all(),
        many=True,
        write_only=True,
        required=False
    )
    assigned_groups = OrganizationGroupSerializer(many=True, read_only=True, source='groups_m2m')

    class Meta:
        model = ToolUser
        fields = ['id', 'username', 'email', 'password', 'role', 'groups_m2m', 'assigned_groups']

    def create(self, validated_data):
        groups = validated_data.pop('groups_m2m', [])
        password = validated_data.pop('password')
        user = ToolUser(**validated_data)
        user.password = make_password(password)
        user.save()

        for group in groups:
            ToolUserGroup.objects.create(user=user, group=group)

        return user
