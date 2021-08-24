from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def home(request):
    ctx = {
        "welcome": _("text_welcome")
    }
    return render(request, "index.html", ctx)
