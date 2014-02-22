from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
  author = models.Charfield(max_length = 30)
  slug = models.SlugField(unique=True, max_length=255)
  title = models.Charfield(max_length = 100)
  bodytext = models.TextField()
  timestamp = models.DateTimeField()
  description = models.CharField(max_length=255)
  content = models.TextField()
  published = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)

class Meta:
  ordering = ['-created']

  def __unicode__(self):
    return u'%s' % self.title

  def get_absolute_url(self):
    return reverse('blog.views.post', args=[self.slug])