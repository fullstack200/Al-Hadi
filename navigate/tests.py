from django.test import TestCase
from .models import MosqueAdmin, Mosques, Prayers

class MosqueAdminModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        MosqueAdmin.objects.create( mosqueAdmin_id='testid01', mosqueAdmin_username='testname', mosqueAdmin_password='testpassword')

    def test_title_content(self):
        ma = MosqueAdmin.objects.get(mosqueAdmin_id='testid01')
        expected_object_name = f'{ma.mosqueAdmin_username}'
        self.assertEqual(expected_object_name, 'testname')
        
    def test_body_content(self):
        ma = MosqueAdmin.objects.get(mosqueAdmin_id='testid01')       
        expected_object_name = f'{ma.mosqueAdmin_password}'
        self.assertEqual(expected_object_name, 'testpassword')

class MosqueModelTest(TestCase):

    def setUp(self):
        # Create a MosqueAdmin instance
        self.admin = MosqueAdmin.objects.create(
            mosqueAdmin_id = 'admin01',
            mosqueAdmin_username='fahd',
            mosqueAdmin_password='securepassword'  # Use hashed passwords in production
        )

        # Create a Mosque instance
        self.mosque = Mosques.objects.create(
            mosque_id='mosque01',
            mosque_name='Masjid E Noor',
            mosque_address='123 Noor Street, Cityville',
            mosque_google_map_url='https://www.google.com/maps/place/123+Noor+Street,+Cityville',
            mosqueAdmin_id=self.admin  # Foreign key to the MosqueAdmin
        )

    def test_mosque_creation(self):
        # Test if the mosque was created successfully
        self.assertEqual(self.mosque.mosque_id, 'mosque01')
        self.assertEqual(self.mosque.mosque_name, 'Masjid E Noor')
        self.assertEqual(self.mosque.mosque_address, '123 Noor Street, Cityville')
        self.assertEqual(self.mosque.mosque_google_map_url, 'https://www.google.com/maps/place/123+Noor+Street,+Cityville')
        self.assertEqual(self.mosque.mosqueAdmin_id, self.admin)

    def test_mosque_str(self):
        # Test the string representation of the Mosque
        self.assertEqual(str(self.mosque), 'Masjid E Noor')  # Assuming you have defined __str__ method in the model

    def tearDown(self):
        # Clean up after each test
        self.mosque.delete()
        self.admin.delete()
        
class PrayerModelTest(TestCase):

    def setUp(self):
        # Create a MosqueAdmin instance
        self.admin = MosqueAdmin.objects.create(
            mosqueAdmin_id = 'admin01',
            mosqueAdmin_username='fahd',
            mosqueAdmin_password='securepassword'  # Use hashed passwords in production
        )

        # Create a Mosque instance
        self.mosque = Mosques.objects.create(
            mosque_id='mosque01',
            mosque_name='Masjid E Noor',
            mosque_address='123 Noor Street, Cityville',
            mosque_google_map_url='https://www.google.com/maps/place/123+Noor+Street,+Cityville',
            mosqueAdmin_id=self.admin  # Foreign key to the MosqueAdmin
        )

        # Create a Prayer instance
        self.prayer = Prayers.objects.create(
            prayer_id='prayer01',
            prayer_name='Fajr',
            prayer_rakat=2,
            azaan_time='05:00:00',
            prayer_time='05:15:00',
            prayer_valid_till='06:30:00',
            mosque_id=self.mosque  # Foreign key to the Mosque
        )

    def test_prayer_creation(self):
        # Test if the prayer was created successfully
        self.assertEqual(self.prayer.prayer_id, 'prayer01')
        self.assertEqual(self.prayer.prayer_name, 'Fajr')
        self.assertEqual(self.prayer.prayer_rakat, 2)
        self.assertEqual(self.prayer.azaan_time, '05:00:00')
        self.assertEqual(self.prayer.prayer_time, '05:15:00')
        self.assertEqual(self.prayer.prayer_valid_till, '06:30:00')
        self.assertEqual(self.prayer.mosque_id, self.mosque)

    def test_prayer_str(self):
        # Test the string representation of the Prayer
        self.assertEqual(str(self.prayer), 'Fajr')  # Assuming you have defined __str__ method in the model

    def tearDown(self):
        # Clean up after each test
        self.prayer.delete()
        self.mosque.delete()
        self.admin.delete()