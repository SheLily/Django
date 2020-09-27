from django.db import models
from django.conf import settings


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField()
    tag = models.ForeignKey(to='Tag', on_delete=models.CASCADE, related_name='products', null=True)

    def __str__(self):
        return self.name

    class Meta:
        pass
        # verbose_name = ''
        # verbose_name_plura = ''


class Tag(models.Model):
    name = models.CharField(max_length=256, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        pass
        # verbose_name = ''
        # verbose_name_plura = ''


class Cart(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField(to='Product', related_name='carts')

    def __str__(self):
        return self.user

    class Meta:
        pass
        # verbose_name = ''
        # verbose_name_plura = ''


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE, related_name='reviews', null=True)
    author = models.CharField(max_length=128)
    body = models.TextField()
    rating = models.PositiveIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.author

    class Meta:
        pass
        # verbose_name = ''
        # verbose_name_plura = ''


class Order(models.Model):
    owner = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    products = models.ManyToManyField(to='Product', related_name='orders')

    @property
    def price(self):
        return sum([product for product in self.products])

    def __str__(self):
        return self.owner

    class Meta:
        pass
        # verbose_name = ''
        # verbose_name_plura = ''
