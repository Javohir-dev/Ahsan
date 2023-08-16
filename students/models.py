from django.db import models


class ActivedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Studens.Status.Active)
    

# class Category(models.Model):
#     name = models.CharField(max_length=150)

#     def __str__(self):
#         return self.name

 
class Subjects(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Teachers(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Studens(models.Model):

    class Status(models.TextChoices):
        Active = "ACT", "Active"
        Disable = "DIS", "Disable"

    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=3, choices=Status.choices, default=Status.Disable
    )
    objects = models.Manager()  # defauld manager
    active = ActivedManager()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ["-created_at"]

