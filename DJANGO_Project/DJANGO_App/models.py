from django.db import models



class Title(models.Model):
    title_name = models.CharField("Название", max_length=50)

    def __str__(self):
        return f"{self.title_name}"
    class Meta:
        verbose_name = 'Название Тайтла'
        verbose_name_plural = 'Названия Тайтлов'

class Genre(models.Model):
    genre_name = models.CharField("Жанр", max_length=25)

    def __str__(self):
        return f"{self.genre_name}"
    class Meta:
        verbose_name = 'Наименование Жанра'
        verbose_name_plural = 'Наименования Жанров'

class Category(models.Model):
    category = models.CharField("Категория", max_length=25)

    def __str__(self):
        return f"{self.category}"
    class Meta:
        verbose_name = 'Наименовании Категории'
        verbose_name_plural = 'Наименования Категорий'

class Platform(models.Model):
    platform = models.CharField("Платформа", max_length=15)

    def __str__(self):
        return f"{self.platform}"
    class Meta:
        verbose_name = 'Название Платформы'
        verbose_name_plural = 'Названия Платформ'

class Catalogue(models.Model):
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name= 'название',
        related_name= 'title'
    )

    genre_id = models.ForeignKey(
        Genre,
        on_delete=models.SET_DEFAULT,
        default=1,
        verbose_name= 'жанр',
        related_name= 'genre'
    )
    
    categories = models.ManyToManyField(
        Category,
        verbose_name='категории',
        related_name='categories'
    )

    platforms = models.ManyToManyField(
        Platform,
        verbose_name='платформы',
        related_name='platforms'
    )
    publish_date = models.DateField("Дата выхода", null=True)

    def __str__(self):
        return f"{self.title_name}"
    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'

#


