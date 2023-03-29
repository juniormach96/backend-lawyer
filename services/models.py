from django.db import models


class Testimonial(models.Model):
    customer_name = models.CharField(max_length=100)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.customer_name}'s testimonial"

    def approve(self):
        self.is_approved = True
        self.save()
