from django.http import HttpResponse
from .models import Post

def home(request):
    # Busca todos os posts do banco de dados
    posts = Post.objects.all()
    # Cria uma resposta simples
    output = "<h1>Blog Posts:</h1>"
    for post in posts:
        output += f"<h2><em>{post.title}</em>: {post.content}</h2>"
    return HttpResponse(output)

