from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    name = models.CharField(verbose_name="Название подкатегории", max_length=150, unique=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория", related_name="categories")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    PRODUCT_TYPES = (
        ('new', "New"),
        ('sale', "Sale"),
        ('sold', "Sold"),
    )

    title = models.CharField(verbose_name='Название товара', max_length=150, unique=True)
    descr = models.TextField(verbose_name='Описание товара')
    price = models.IntegerField(verbose_name='Цена товара')
    quantity = models.IntegerField(verbose_name='Количество Товара', default=10)
    product_type = models.CharField(verbose_name='Тип продукта', choices=PRODUCT_TYPES, max_length=4)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    photo = models.ImageField(verbose_name='Фото', upload_to='products/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

