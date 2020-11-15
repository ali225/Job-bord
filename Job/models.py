from django.db import models

# Create your models here.
JOB_TYPE = (
    ('Full Time', 'Full time'),
    ('Part Time', 'Part Time'),
)


class Job(models.Model):
    title = models.CharField(max_length=100)  # colum
    # location
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class category(models.Model):
    name = models.CharField(max_length=100)