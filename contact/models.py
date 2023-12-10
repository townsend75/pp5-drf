from django.db import models;
from django.contrib.auth.models import User;


QUESTIONS = (
    ('LOGIN', 'Trouble logging in'),
    ('PASSWORD', 'Forgotten password'),
    ('REPORT', 'Report inappropriate site content'),
    ('OTHER', 'Other reason')
)


class Contact(models.Model):

    """
    Contact model, related to User
    """


    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=50, choices=QUESTIONS)
    content = models.TextField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(null=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner} : {self.question}"


