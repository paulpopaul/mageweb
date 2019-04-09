from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Biografia(models.Model):

    titulo = models.CharField(max_length=255, help_text='Biografía')
    contenido = models.TextField(help_text='Descripcion Biografía')
    titulo_dos = models.CharField(max_length=20, null=True, blank=True, help_text='Influencias')
    contenido_dos = models.CharField(max_length=255, null=True, blank=True, help_text='Géneros Musicales')
    etiqueta_uno = models.CharField(max_length=20, null=True, blank=True, help_text='Influencia Musical Uno')
    etiqueta_dos = models.CharField(max_length=20, null=True, blank=True, help_text='Influencia Musical Dos')
    etiqueta_tres = models.CharField(max_length=20, null=True, blank=True, help_text='Influencia Musical Tres')
    etiqueta_cuatro = models.CharField(max_length=20, null=True, blank=True, help_text='Influencia Musical Cuatro')
    slug = models.SlugField(editable=False)

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)
        super(Biografia, self).save(*args, **kwargs)