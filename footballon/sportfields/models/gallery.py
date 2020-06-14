# Django
from django.db import models

# Utils
from footballon.utils.models import FootballonModel

class Gallery(FootballonModel):
  """Gallery model.

  This is the sports fields gallery.
  """
  sport_field = models.ForeignKey('fields.SportField', on_delete=models.CASCADE)

  picture = models.ImageField(
    'Gallery picture',
    upload_to='sportfields/gallery/',
    null=True
  )
  