from django.contrib import admin
from .models import FeatureSmall, \
    FeatureBig, \
    WorkProcess, \
    Testimonial, \
    Pricing, \
    Counter


@admin.register(FeatureSmall)
class FeatureSmallAdmin(admin.ModelAdmin):
    list_display = ['feature_title', 'created', 'modified', 'is_live']


@admin.register(FeatureBig)
class FeatureBigAdmin(admin.ModelAdmin):
    list_display = ['feature_title', 'created', 'modified', 'is_live']


@admin.register(WorkProcess)
class WorkProcessAdmin(admin.ModelAdmin):
    list_display = ['process_name', 'created', 'modified', 'is_live']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['author', 'created', 'modified', 'is_live']


@admin.register(Counter)
class COunterAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'modified', 'is_live']