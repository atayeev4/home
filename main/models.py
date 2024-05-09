from django.db import models


class City(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    
class Image(models.Model):
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='apartment_images')

    def __str__(self):
        return f'{self.apartment} - image'

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Apartment(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField()
    type = models.ForeignKey('Type', on_delete=models.CASCADE, related_name='type', blank=True, null=True)
    rooms = models.PositiveSmallIntegerField()
    metres = models.PositiveSmallIntegerField()
    price = models.PositiveSmallIntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='apartments')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Апартамент'
        verbose_name_plural = 'Апартаменты'


class UserApplication(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.phone}'
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'



class Type(models.Model):
    title = models.CharField(max_length=100, db_index=True, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип недвижимости'
        verbose_name_plural = 'Типы недвижимости'


