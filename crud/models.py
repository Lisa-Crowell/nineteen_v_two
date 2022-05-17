from django.db import models


class IdeaModel(models.Model):
    idea_title = models.CharField(max_length=75)
    idea_description = models.TextField()
    idea_author = models.CharField(max_length=50)

    def __str__(self):
        return self.idea_title
