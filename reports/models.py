from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('In Progress', 'In Progress'),
    ('Rejected', 'Rejected'),
]

class BugReport(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cvss_score = models.FloatField()
    poc_file = models.FileField(upload_to='pocs/', blank=True, null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    reward = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
