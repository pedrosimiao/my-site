from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=160)  # Coluna para o título do post
    content = models.TextField()  # Coluna para o conteúdo do post
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação

    def __str__(self):
        return self.title  # Exibe o título do post como representação
