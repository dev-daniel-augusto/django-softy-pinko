from django.test import TestCase
from model_bakery import baker
from core.models import refactor_name
from uuid import uuid4


class RefactorNameTestCase(TestCase):

    def setUp(self):
        self.name_1 = f'{uuid4()}.png'
        self.name_2 = f'{uuid4()}.jpeg'
        self.name_3 = f'{uuid4()}.psd'
        self.name_4 = f'{uuid4()}.raw'
        self.name_5 = f'{uuid4()}.indd'
        self.name_6 = f'{uuid4()}.ai'
        self.name_7 = f'{uuid4()}.tiff'
        self.name_8 = f'{uuid4()}.bmp'
        self.name_9 = f'{uuid4()}.gif'
        self.name_10 = f'{uuid4()}.eps'

    def test_refactor_name(self):
        file_1 = refactor_name(None, 'str.png')
        file_2 = refactor_name(None, 'str.jpeg')
        file_3 = refactor_name(None, 'str.psd')
        file_4 = refactor_name(None, 'str.raw')
        file_5 = refactor_name(None, 'str.indd')
        file_6 = refactor_name(None, 'str.ai')
        file_7 = refactor_name(None, 'str.tiff')
        file_8 = refactor_name(None, 'str.bmp')
        file_9 = refactor_name(None, 'str.gif')
        file_10 = refactor_name(None, 'str.eps')

        self.assertEquals(len(self.name_1), len(file_1))
        self.assertEquals(len(self.name_2), len(file_2))
        self.assertEquals(len(self.name_3), len(file_3))
        self.assertEquals(len(self.name_4), len(file_4))
        self.assertEquals(len(self.name_5), len(file_5))
        self.assertEquals(len(self.name_6), len(file_6))
        self.assertEquals(len(self.name_7), len(file_7))
        self.assertEquals(len(self.name_8), len(file_8))
        self.assertEquals(len(self.name_9), len(file_9))
        self.assertEquals(len(self.name_10), len(file_10))


class FeatureSmallTestCase(TestCase):

    def setUp(self):
        self.object_1 = baker.make('FeatureSmall')
        self.object_2 = baker.make('FeatureSmall')
        self.object_3 = baker.make('FeatureSmall')
        self.object_4 = baker.make('FeatureSmall')
        self.object_5 = baker.make('FeatureSmall')

    def test_str_feature_small(self):
        self.assertEquals(str(self.object_1), self.object_1.feature_title)
        self.assertEquals(str(self.object_2), self.object_2.feature_title)
        self.assertEquals(str(self.object_3), self.object_3.feature_title)
        self.assertEquals(str(self.object_4), self.object_4.feature_title)
        self.assertEquals(str(self.object_5), self.object_5.feature_title)


class FeatureBigTestCase(TestCase):

    def setUp(self):
        self.object_1 = baker.make('FeatureBig')
        self.object_2 = baker.make('FeatureBig')
        self.object_3 = baker.make('FeatureBig')
        self.object_4 = baker.make('FeatureBig')
        self.object_5 = baker.make('FeatureBig')

    def test_str_feature_big(self):
        self.assertEquals(str(self.object_1), self.object_1.feature_title)
        self.assertEquals(str(self.object_2), self.object_2.feature_title)
        self.assertEquals(str(self.object_3), self.object_3.feature_title)
        self.assertEquals(str(self.object_4), self.object_4.feature_title)
        self.assertEquals(str(self.object_5), self.object_5.feature_title)


class WorkProcessTestCase(TestCase):

    def setUp(self):
        self.object_1 = baker.make('WorkProcess')
        self.object_2 = baker.make('WorkProcess')
        self.object_3 = baker.make('WorkProcess')
        self.object_4 = baker.make('WorkProcess')
        self.object_5 = baker.make('WorkProcess')

    def test_str_work_process(self):
        self.assertEquals(str(self.object_1), self.object_1.process_name)
        self.assertEquals(str(self.object_2), self.object_2.process_name)
        self.assertEquals(str(self.object_3), self.object_3.process_name)
        self.assertEquals(str(self.object_4), self.object_4.process_name)
        self.assertEquals(str(self.object_5), self.object_5.process_name)


class TestimonialTestCase(TestCase):

    def setUp(self):
        self.object_1 = baker.make('Testimonial')
        self.object_2 = baker.make('Testimonial')
        self.object_3 = baker.make('Testimonial')
        self.object_4 = baker.make('Testimonial')
        self.object_5 = baker.make('Testimonial')

    def test_str_testimonial(self):
        self.assertEquals(str(self.object_1), self.object_1.author)
        self.assertEquals(str(self.object_2), self.object_2.author)
        self.assertEquals(str(self.object_3), self.object_3.author)
        self.assertEquals(str(self.object_4), self.object_4.author)
        self.assertEquals(str(self.object_5), self.object_5.author)


class PricingTestCase(TestCase):

    def setUp(self):
        self.object_1 = baker.make('Pricing')
        self.object_2 = baker.make('Pricing')
        self.object_3 = baker.make('Pricing')
        self.object_4 = baker.make('Pricing')
        self.object_5 = baker.make('Pricing')

    def test_str_pricing(self):
        self.assertEquals(str(self.object_1), self.object_1.name)
        self.assertEquals(str(self.object_2), self.object_2.name)
        self.assertEquals(str(self.object_3), self.object_3.name)
        self.assertEquals(str(self.object_4), self.object_4.name)
        self.assertEquals(str(self.object_5), self.object_5.name)


class CounterTestCase(TestCase):

    def setUp(self):
        self.object_1 = baker.make('Counter')
        self.object_2 = baker.make('Counter')
        self.object_3 = baker.make('Counter')
        self.object_4 = baker.make('Counter')
        self.object_5 = baker.make('Counter')

    def test_str_counter(self):
        self.assertEquals(str(self.object_1), self.object_1.name)
        self.assertEquals(str(self.object_2), self.object_2.name)
        self.assertEquals(str(self.object_3), self.object_3.name)
        self.assertEquals(str(self.object_4), self.object_4.name)
        self.assertEquals(str(self.object_5), self.object_5.name)
