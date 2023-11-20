# models.py
from django.db import models

class AssociatedContent(models.Model):
    word = models.CharField(max_length=255)
    paragraph = models.TextField()
    figure = models.ImageField(upload_to='figures/')

    class Meta:
        db_table = 'associated_content'

    def __str__(self):
        return f'{self.word} - {self.id}'

class Output(models.Model):
    Concepts = models.TextField()
    Text = models.TextField()
    References = models.TextField()
    Definition = models.TextField()
    Keywords = models.TextField()
    Synonyms = models.TextField()
    Predicate = models.CharField(max_length=255, default='Uncategorized')
    Object_Topic = models.CharField(max_length=255, default='Uncategorized')



    class Meta:
        db_table = 'output'

    def __str__(self):
        return f'{self.Concepts} - {self.id}'
