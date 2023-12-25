from django.db import models

class Message(models.Model):
    #contenu du message
    content = models.TextField()
    #temps de creation du message 
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.timestamp} - {self.content}"