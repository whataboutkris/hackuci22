from django.db import models
from django.db.models.deletion import CASCADE
import uuid


# Create your models here.
class Laptop(models.Model):
    brand = models.CharField(max_length=200)
    main_url = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)

    def __str__(self):
        return self.brand