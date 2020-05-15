from django.views import generic
from .models import BlogPost


class ArticlesView(generic.ListView):
    model = BlogPost
    template_name = 'html/blog.html'
    queryset = BlogPost.objects.all().order_by('-created_on')
    context_object_name = 'articles'
    paginate_by = 5

class ArticleDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'html/blog-single.html'
