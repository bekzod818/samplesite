from django.db import models

class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Nomi')

    class Meta:
        verbose_name_plural = 'Bo\'limlar'
        verbose_name = 'Bo\'lim'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Bb(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey(Rubric, null=True, on_delete=models.PROTECT, verbose_name='Reklamalar')

    class Meta:
        verbose_name_plural = 'Reklamalar'
        verbose_name = 'Reklama'
        ordering = ['-published']

    def __str__(self):
        return self.title
        