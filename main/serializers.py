from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Recruit


class BulkUpdateListSerializer(serializers.ListSerializer):

    def update(self, instances, validated_data):

        instance_hash = {index: instance for index, instance in enumerate(instances)}

        result = [
            self.child.update(instance_hash[index], attrs)
            for index, attrs in enumerate(validated_data)
        ]

        writable_fields = [
            x
            for x in self.child.fields
            if x not in self.child.Meta.read_only_fields
        ]


        try:
            self.child.Meta.model.objects.bulk_update(result, writable_fields)
        except IntegrityError as e:
            raise ValidationError(e)



        return result


class RecruitSerializer(serializers.ModelSerializer):
    #renamed_id = serializers.IntegerField(source='id')
    class Meta:
        model = Recruit
        fields = "__all__"
        read_only_fields = ("id",)
        list_serializer_class = BulkUpdateListSerializer
        order_by = (
            ('order_id',)
        )

class RecruiterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recruit
        fields = '__all__'
        read_only_fields = ("id","order_id",)
