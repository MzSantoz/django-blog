import uuid
from django.db import models
from django.urls import reverse

class Categories(models.TextChoices):
      TECH = 'TC', 'Technology'
      BUGS = 'BG', "Bugs"
      MONEY = 'MN', "Money"
      NONE = "NA", 'Select one category'
class Post(models.Model):

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  title = models.CharField(max_length=100)
  sub_title = models.CharField(max_length=200)
  content = models.TextField()
  categories = models.CharField(
    max_length=2,
    choices=Categories.choices,
    default=Categories.TECH,
  )
  deleted = models.BooleanField(default=False)
  slug = models.SlugField(null=True, unique=True)
  image = models.ImageField(upload_to='posts', null=True, blank=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post_detail', kwargs={'slug': self.slug})
  
  def get_category_label(self):
    return self.get_categories_display()