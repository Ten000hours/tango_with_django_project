from django.test import TestCase
from rango.models import Category, PostAd, Page, UserProfile, User
from django.core.urlresolvers import reverse


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


def add_ad(title, description, image, location, email, phone, likes, price):
    ad = PostAd.objects.get_or_create(title=title)[0]
    ad.description = description
    ad.image = image
    ad.price = price
    ad.location = location
    ad.email = email
    ad.phone = phone
    ad.likes = likes
    ad.save()
    return ad


class CategoryMethodTests(TestCase):

    def test_ensure_views_are_positive(self):
        cat = Category(name='test', views=-1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)

    def test_ensure_likes_are_positive(self):
        cat = Category(name='test', views=0, likes=-1)
        cat.save()
        self.assertEqual((cat.likes >= 0), True)


class PostadMethodTests(TestCase):

    def test_ensure_likes_are_positive(self):
        ad = PostAd(title='test', likes=-1, description='test',image='ad_images/bbig6.jpg', location='g207da',
                       email='xuxiangek@gmail.com', phone=92387429, price=12 )
        ad.save()
        self.assertEqual((ad.likes >= 0), True)

    def test_ensure_price_are_positive(self):
        ad = PostAd(title='test', likes=0, description='test',image='ad_images/bbig6.jpg', location='g207da',
                       email='xuxiangek@gmail.com', phone=92387429, price=-12 )
        ad.save()
        self.assertEqual((ad.price >= 0), True)
    def test_ensure_phone_are_positive(self):
        ad = PostAd(title='test', likes=0, description='test',image='ad_images/bbig6.jpg', location='g207da',
                       email='xuxiangek@gmail.com', phone=-92387429, price=12 )
        ad.save()
        self.assertEqual((ad.phone >= 0), True)


class IndexViewTests(TestCase):

    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['categories'], [])

    def test_index_view_with_categories(self):
        """
        Check to make sure that the index has categories displayed
        """

        add_cat('test', 1, 1)
        add_cat('temp', 1, 1)
        add_cat('tmp', 1, 1)
        add_cat('tmp test temp', 1, 1)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")
        num_cats = len(response.context['categories'])
        self.assertEqual(num_cats, 4)

    def test_showitem_view_with_categories(self):
        add_ad('pc', 'random description', 'ad_images/bbig6.jpg', 'g207bb', "xianslkje@gmail.com", "7983473", 23, 12)
        response = self.client.get(reverse('showitem'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")
        num_cats = len(response.context['ad_list'])
        self.assertEqual(num_cats, 1)
