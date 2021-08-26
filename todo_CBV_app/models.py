from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
# Create your models here.


class Task(models.Model):
    """docstring for Todo."""
    title = models.CharField(verbose_name=_('title'), max_length=100)
    is_complete = models.BooleanField(default=False, verbose_name=_('is complete'))
    created_data = models.DateTimeField(default=timezone.now)

    description = models.TextField(null=True, blank=True, verbose_name=_('description'))
    image = models.ImageField(default='todo/default.jpg',
                              null=True, blank=True, upload_to='todo/%Y/%m/%d', verbose_name=_('image'))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_data', )
