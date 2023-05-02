from django.db import models


class ClassifierAlgorithm(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'classifier_algorithm'
