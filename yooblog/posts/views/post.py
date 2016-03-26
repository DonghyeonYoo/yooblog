from django.http import HttpResponse
from django.template import loader

from posts.models import Post


def posts(request):
        template = loader.get_template("posts/list.html")
        context = {
            'posts': Post.objects.all()
        }

    return HttpResponse(
        template.render(
                context,
                request,
        )
