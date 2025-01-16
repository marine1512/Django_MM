from django.db import models
from enum import Enum

class StatusEnum(Enum):
    DEFAULT = '?', '?'
    IN_STOCK = 'ok', 'In stock'
    OUT_OF_STOCK = 'no', 'Out of stock'


class Media(models.Model):
    nom = models.fields.CharField(max_length=150)
    type_media = models.fields.CharField( max_length=2,
        choices=[(tag.value[0], tag.value[1]) for tag in StatusEnum],
        default=StatusEnum.DEFAULT.value[0])
