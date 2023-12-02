from django.test import TestCase
from .models import Music

class MusicTestCase(TestCase):
    def test_model_name(self):
        music1 = Music.objects.create(name="Dora", artist="dura")
        self.assertEqual(music1.name, "Dora")

    def test_model_url(self):
        music1 = Music.objects.create(name="Dora", artist="dura")
        self.assertEqual(music1.artist, "dura")