from rest_framework import serializers
from .models import (
                    FeatureSmall,
                    FeatureBig,
                    WorkProcess,
                    Testimonial,
                    Pricing,
                    Counter,
                    )


class FeatureSmallSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeatureSmall
        fields = (
            'id',
            'feature_title',
            'feature_desc',
            'created',
            'modified',
            'is_live',
        )


class FeatureBigSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeatureBig
        fields = (
            'id',
            'feature_title',
            'feature_desc',
            'created',
            'modified',
            'is_live',
        )


class WorkProcessSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkProcess
        fields = (
            'id',
            'process_name',
            'process_desc',
            'created',
            'modified',
            'is_live',
        )


class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testimonial
        fields = (
            'id',
            'author',
            'role',
            'opinion',
            'created',
            'modified',
            'is_live',
        )


class PricingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pricing
        fields = (
            'id',
            'name',
            'price',
            'currency',
            'service_duration',
            'benefits',
            'created',
            'modified',
            'is_live',
        )


class CounterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Counter
        fields = (
            'id',
            'name',
            'number',
            'created',
            'modified',
            'is_live',
        )
