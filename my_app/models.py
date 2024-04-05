from django.db import models


class Python(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name  # Corrected to return self.name instead of self.topic

    class Meta:
        ordering = ['name']  # Corrected to use the existing field 'name'
        verbose_name = 'Python'
        db_table = 'python'


class Topic(models.Model):
    topic_name = models.CharField(max_length=250)
    topic_subject = models.CharField(max_length=200)
    topic_content = models.TextField()
    topic_url = models.URLField()
    topic_banner = models.ImageField(upload_to='python/')

    def __str__(self):
        return self.topic_url

    class Meta:
        db_table = 'topic'
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
