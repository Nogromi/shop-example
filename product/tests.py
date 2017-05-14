from django.test import TestCase
from .models import Product,Profile
from django.contrib.auth.models import User
import datetime

class ProductTestCase(TestCase):
    def setUp(self):
        # self.user=Profile.objects.create('TestUser','fistnametest','test@user.com', 'mypassmypass', 'mypassmypass',)
        self.p= Product.objects.create(name="Test Product", slug= 'test-product', description="test-description", price=10.90,created=datetime.datetime.now()-datetime.timedelta(days=2), updated=datetime.datetime.now(),)


    def test_products_get_url(self):

        self.assertEqual(self.p.get_absolute_url(), "/test-product/")
        #
        # TestProduct = Product.objects.get(name="Test Product")
        # TestProduct2 = Product.objects.get(name="Test Product2")
        # self.assertEqual(TestProduct.get_absolute_url(), '/test-product')
        # self.assertEqual(TestProduct2.get_absolute_url(), '/test-product2')
