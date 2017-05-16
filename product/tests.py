from django.test import TestCase
from .models import Product, Profile, Comment
import datetime
from django.urls import reverse

class ProductTestCase(TestCase):
    def setUp(self):
        self.p = Product.objects.create(name="Test Product", slug='test-product', description="test-description",
                                        price=10.90, created=datetime.datetime.now() - datetime.timedelta(days=2),
                                        updated=datetime.datetime.now() )



    def test_products_get_url(self):
        """
            Test that product has absolute url
        """
        self.assertEqual(self.p.get_absolute_url(), "/test-product/")

    def test_product_list_view(self):
        """
            Test that list page  exists
        """
        response = self.client.get(reverse('product_list'))
        self.assertEqual(response.status_code, 200)


    def test_product_detail_view(self):
        """
            Test that detail page exists
        """
        response = self.client.get(reverse('product_detail', args=[self.p.slug]))
        self.assertEqual(response.status_code, 200)
