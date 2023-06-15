from django.db import models


# Create your models here.
class Place(models.Model):
    number = models.IntegerField(unique=True, verbose_name="Номер места")
    side = models.CharField(max_length=5, blank=True, verbose_name="Часть (верхняя или нижняя)")
    location = models.CharField(max_length=7, blank=True, verbose_name="Место")

    class Meta:
        constraints = (models.CheckConstraint(check=models.Q(number__gt=0), name="больше 0"),
                       models.CheckConstraint(check=models.Q(number__lte=54), name="меньше или равно 54"))
        ordering = ("number",)
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return "Место " + str(self.number)

