from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Car(models.Model):
    vin = models.CharField(verbose_name='Vin', max_length=64, db_index=True, unique=True)
    color = models.CharField(verbose_name='Color', max_length=64)
    CAR_TYPES = (
        (1, 'Sedan'),
        (2, 'Unversal'),
        (3, 'Kuper')
    )
    car_type = models.IntegerField(verbose_name='Car_Type', choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
