from django.db import models

# 1. Баннер (Слайдер)
class Banner(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    subtitle = models.CharField(max_length=200, verbose_name="Подзаголовок")
    image = models.ImageField(upload_to='banners/', verbose_name="Изображение")
    link = models.CharField(max_length=500, verbose_name="Ссылка/WhatsApp")
    button_text = models.CharField(max_length=50, verbose_name="Текст кнопки")

    def __str__(self): return self.title

    class Meta:
        verbose_name = 'баннер'
        verbose_name_plural = 'Баннеры'

# 2. Категории
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    image = models.ImageField(upload_to='categories/')
    url_name = models.CharField(max_length=100, verbose_name="Ссылка (напр. rings.html)")

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'


# 3. Сетка особенностей (Товары в фокусе)
class FeatureProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена", null=True, blank=True)
    image = models.ImageField(upload_to='features/')
    is_large = models.BooleanField(default=False, verbose_name="Большой блок?")

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'особенность'
        verbose_name_plural = 'Особенности'

# 4. Отзывы
class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя клиента")
    text = models.TextField(verbose_name="Текст отзыва")
    stars = models.IntegerField(default=5, verbose_name="Кол-во звезд")

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'

# 5. Блог
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок статьи")
    meta = models.CharField(max_length=200, verbose_name="Краткое описание")
    image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.title

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'Статьи'
