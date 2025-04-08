from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Todo(models.Model):
    STATE_CHOICES = (
        ('not_started', 'Not Started'),
        ('stopped', 'Stopped'),
        ('active', 'Active'),
        ('paused', 'Paused'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    category = models.CharField(max_length=100, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.CharField(max_length=15, choices=STATE_CHOICES, default='Not Started')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
