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

class Category(models.Model):
    category = models.CharField("Категория", max_length=25)

class Platform(models.Model):
    platform = models.CharField("Платформа", max_length=15)

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


