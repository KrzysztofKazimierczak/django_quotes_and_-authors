from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50, null=False)
    born_date = models.DateField()
    born_location = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    
class Tag(models.Model):
    tag = models.CharField(max_length=20, unique=True, null=False)

    def __str__(self):
        return f"{self.tag}"

class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.content}"