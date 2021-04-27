from rest_framework.routers import SimpleRouter
from django.urls import path
from .views import IndexView
from .views import (
                    FeatureSmallViewSet,
                    FeatureBigViewSet,
                    WorkProcessViewSet,
                    TestimonialViewSet,
                    PricingViewSet,
                    CounterViewSet,
                    )


router = SimpleRouter()

router.register('features-small', FeatureSmallViewSet)
router.register('features-big', FeatureBigViewSet)
router.register('work-processes', WorkProcessViewSet)
router.register('testimonials', TestimonialViewSet)
router.register('prices', PricingViewSet)
router.register('counters', CounterViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
