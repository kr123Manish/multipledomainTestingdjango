from django.contrib.auth.models import AbstractUser
from django.db import models

class OrganizationGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ToolUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('researcher', 'Researcher'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='researcher')
    groups_m2m = models.ManyToManyField(
        OrganizationGroup,
        through='ToolUserGroup',
        related_name='users'
    )

    def __str__(self):
        return f"{self.username} ({self.role})"


class ToolUserGroup(models.Model):
    user = models.ForeignKey(ToolUser, on_delete=models.CASCADE)
    group = models.ForeignKey(OrganizationGroup, on_delete=models.CASCADE)
    date_assigned = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tooluser_org_groups'
        unique_together = ('user', 'group')  # Prevent duplicates

    def __str__(self):
        return f"{self.user.username} -> {self.group.name}"
