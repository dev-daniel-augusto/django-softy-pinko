from django.views.generic import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from rest_framework import viewsets
from .forms import ContactUsForm
from .models import (
                    FeatureSmall,
                    FeatureBig,
                    WorkProcess,
                    Testimonial,
                    Pricing,
                    Counter,
                    )
from.serializers import (
                        FeatureSmallSerializer,
                        FeatureBigSerializer,
                        WorkProcessSerializer,
                        TestimonialSerializer,
                        PricingSerializer,
                        CounterSerializer,
                        )


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['features_small'] = FeatureSmall.objects.all()
        context['features_big'] = FeatureBig.objects.all()
        context['work_process'] = WorkProcess.objects.all()
        context['pricing'] = Pricing.objects.order_by('price').all()
        context['testimonials'] = Testimonial.objects.all()
        context['counter'] = Counter.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, "Your e-mail was successfully sent")
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "It was not possible to send your e-mail, please try again")
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class FeatureSmallViewSet(viewsets.ModelViewSet):
    queryset = FeatureSmall.objects.all()
    serializer_class = FeatureSmallSerializer


class FeatureBigViewSet(viewsets.ModelViewSet):
    queryset = FeatureBig.objects.all()
    serializer_class = FeatureBigSerializer


class WorkProcessViewSet(viewsets.ModelViewSet):
    queryset = WorkProcess.objects.all()
    serializer_class = WorkProcessSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class PricingViewSet(viewsets.ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer


class CounterViewSet(viewsets.ModelViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer
