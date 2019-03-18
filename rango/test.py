from django.test import TestCase
from rango.models import Category, PostAd, Page, UserProfile, User
from django.core.urlresolvers import reverse


# class CategoryMethodTests(TestCase):
#
#     def test_ensure_views_are_positive(self):
#         cat = Category(name='test', views=-1, likes=0)
#         cat.save()
#         self.assertEqual((cat.views >= 0), True)
#
#     def test_ensure_likes_are_posi(self):
#         ad = PostAd(title='test', likes=-1, description='asdfasfads', price=34, location="g207da", eamil)
#         ad.save()
#         self.assertEqual((ad.likes >= 0))
#
#
# class IndexViewTests(TestCase):
#
#
#     def test_index_view_with_no_categories(self):
#
#
#         response = self.client.get(reverse('index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "There are no categories present.")
#         self.assertQuerysetEqual(response.context['categories'], [])
