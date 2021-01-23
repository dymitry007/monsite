from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    auteur = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='Images')
    image0 = models.ImageField(upload_to='Images')
    image1 = models.ImageField(upload_to='Images')
    image2 = models.ImageField(upload_to='Images')
    paragraphe0 = models.TextField(blank=True, null=True)
    paragraphe1 = models.TextField(blank=True, null=True)
    paragraphe2 = models.TextField(blank=True, null=True)
    url0 = models.URLField(blank=True, null=True)
    url1 = models.URLField(blank=True, null=True)
    url2 = models.URLField(blank=True, null=True)
    url3 = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        verbose_name_plural = "images"
        verbose_name_plural = "image0"
        verbose_name_plural = "image1"
        verbose_name_plural = "image2"
        verbose_name_plural = "url0"
        verbose_name_plural = "url1"
        verbose_name_plural = "url2"
        verbose_name_plural = "url3"
        verbose_name_plural = "paragraphe0"
        verbose_name_plural = "paragraphe1"
        verbose_name_plural = "paragraphe2"
        verbose_name_plural = "url0"
        verbose_name_plural = "url1"
        verbose_name_plural = "url2"
        verbose_name_plural = "url3"
      

        
