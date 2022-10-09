from django.test import TestCase


class SampleTest(TestCase):
    def test_true(self):
        self.assertTrue(True, 'is true')

# 运行测试
#  python manage.py test hello
