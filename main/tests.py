from django.test import TestCase, Client
from main.models import Item
# Create your tests here.

class mainTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Item.objects.create(name='Buku', amount=2, description="test")
    
    def test_buku_label(self):
        buku = Item.objects.get(id=1)
        field_label = buku._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_amount_label(self):
        buku = Item.objects.get(id=1)
        field_label = buku._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')

    def test_buku_label(self):
        buku = Item.objects.get(id=1)
        field_label = buku._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_object_name_is_last_name_comma_first_name(self):
        buku = Item.objects.get(id=1)
        expected_object_string = f'{buku.name}, {buku.amount}, {buku.description}'
        self.assertEqual("Buku, 2, test", expected_object_string)

    def test_landing_url_is_exist(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200) 
    
    def test_main_using_main_template(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'landingpage.html')
    
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    