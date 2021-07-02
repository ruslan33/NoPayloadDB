# from django.contrib.auth.models import User
from rest_framework import serializers
from cdb.models import GlobalTag, GlobalTagStatus, GlobalTagType, PayloadType, PayloadList, PayloadIOV


class GlobalTagStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = GlobalTagStatus
        fields = ("id","name","created")


class GlobalTagTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = GlobalTagType
        fields = ("id", "name", "created")

class GlobalTagCreateSerializer(serializers.ModelSerializer):

    #type = serializers.SlugRelatedField(slug_field="name", queryset=GlobalTagType.objects.all())

    class Meta:
        model = GlobalTag
        fields = ("id", "name", "status", "type", "created", "updated")
        #depth = 1

class GlobalTagReadSerializer(serializers.ModelSerializer):

    #type = serializers.SlugRelatedField(slug_field="name", queryset=GlobalTagType.objects.all())

    class Meta:
        model = GlobalTag
        fields = ("id", "name", "status", "type", "created", "updated")
        depth = 1

class PayloadTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PayloadType
        fields = ("id", "name", "created")

class PayloadIOVSerializer(serializers.ModelSerializer):

    class Meta:
        model = PayloadIOV
        fields = ("id", "payload_url", "major_iov", "minor_iov", "created")

class PayloadListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PayloadList
        fields = ("id", "name", "payload_type", "payload_iov", "created")
