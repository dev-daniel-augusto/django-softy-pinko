from django.db import models
from uuid import uuid4
from stdimage import StdImageField
from django.contrib.postgres.fields import ArrayField


def refactor_name(instance, filename):
    ext = filename.split('.')[-1]
    return f'{uuid4()}.{ext}'


class Base(models.Model):
    is_live = models.BooleanField('Is Live?', default=True)
    created = models.DateField('Created', auto_now_add=True)
    modified = models.DateField('Last Time Modified', auto_now=True)

    class Meta:
        abstract = True


class FeatureSmall(Base):
    feature_title = models.CharField('Feature Name', max_length=30)
    feature_desc = models.CharField('Description', max_length=120)
    image = StdImageField('Image',
                          upload_to=refactor_name,
                          variations={'thumbnail': {'width': 56, 'height': 48}})

    class Meta:
        verbose_name = 'Small Feature'
        verbose_name_plural = 'Small Features'

    def __str__(self):
        return self.feature_title


class FeatureBig(Base):
    feature_title = models.CharField('Name', max_length=60)
    feature_desc = models.CharField('Description', max_length=300)
    image = StdImageField('Image',
                          upload_to=refactor_name,
                          variations={'thumbnail': {'width': 280, 'height': 280, 'crop': True}})

    class Meta:
        verbose_name = 'Big Feature'
        verbose_name_plural = 'Big Features'

    def __str__(self):
        return self.feature_title


class WorkProcess(Base):
    process_name = models.CharField('Process', max_length=30)
    process_desc = models.CharField('Description', max_length=50)
    image = StdImageField('Image',
                          upload_to=refactor_name,
                          variations={'thumbnail': {'width': 32, 'height': 32, 'crop': True}})

    class Meta:
        verbose_name = 'Work Process'
        verbose_name_plural = 'Work Processes'

    def __str__(self):
        return self.process_name


class Testimonial(Base):
    author = models.CharField('Author', max_length=50)
    role = models.CharField('Role', max_length=50)
    opinion = models.CharField('Opinion', max_length=300)
    image = StdImageField('Image',
                          upload_to=refactor_name,
                          variations={'thumbnail': {'width': 32, 'height': 32, 'crop': True}})

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.author


class Pricing(Base):
    DURATION_CHOICES = (
        ('Daily', 'Per day'),
        ('Weekly', 'Per week'),
        ('Monthly', 'Per month'),
        ('Yearly', 'Per year')
    )
    name = models.CharField('Name', max_length=50)
    price = models.DecimalField('Price', decimal_places=2, max_digits=10)
    currency = models.CharField('Currency', max_length=4, default='$')
    service_duration = models.CharField('Duration', max_length=7, choices=DURATION_CHOICES)
    benefits = ArrayField(models.CharField(max_length=40, default=list), size=10)

    class Meta:
        verbose_name = 'Pricing'

    def __str__(self):
        return self.name


class Counter(Base):
    name = models.CharField('Name', max_length=100)
    number = models.IntegerField('Number')

    class Meta:
        verbose_name = 'Counter'

    def __str__(self):
        return self.name


