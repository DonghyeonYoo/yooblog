from django.template import loader
from django.http import HttpResponse


def home(request):
    template = loader.get_template("home/home.html")
    context={}

    return HttpResponse(
        template.render(
            context,
            request,
        ),
    )
