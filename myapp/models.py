from django.db import models
import uuid


class users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Firstname = models.CharField(max_length = 25,unique = True)
    Lastname = models.CharField(max_length = 25,unique = True)
    Email = models.EmailField(max_length = 254,unique = True)
    Date_of_birth = models.DateField()
    Git_address = models.URLField(max_length = 200,unique = True)
    linkedin_address = models.URLField(max_length = 200,unique = True)
    Phone = models.CharField(max_length = 20,unique = True)
    address = models.TextField()
    photo = models.ImageField(upload_to = 'images/',default = 'images/default.jpg')
    def __str__(self):
        return f"{self.Firstname} {self.Lastname}"




class languages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    language_name = models.CharField(max_length = 50,unique = True)
    percentage = models.IntegerField() 
    def __str__(self):
        return self.language_name





class projects(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    user = models.ForeignKey(users, on_delete=models.CASCADE, related_name = 'projects')
    project_name = models.CharField(max_length = 200,unique = True)
    project_language = models.ManyToManyField(languages, through='assign_language')
    project_link = models.URLField(max_length = 200,unique = True)
    description = models.TextField()

    def __str__(self):
        return self.project_name
    




class assign_language(models.Model):
    project = models.ForeignKey(projects, on_delete=models.CASCADE)
    language = models.ForeignKey(languages, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.project} {self.language}"
