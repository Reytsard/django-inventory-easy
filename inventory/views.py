from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render

from .models import Item, User


# Create your views here.
def index(request):
    return HttpResponse("Hello World!")


def user_details(request, user_id):
    user = User.objects.get(id=int(user_id))
    return HttpResponse("You're looking at user %s." % user.name)


def items(request):
    all_items = Item.objects.all()
    template = loader.get_template("polls/index.html")
    context = {"item_list": all_items}
    # instead of this replace with render()
    # return HttpResponse(template.render(context,request))
    return render(request, "polls/index.html", context)


def item_details(request, item_id):
    # try:
    #     item = Item.objects.get(id=int(item_id))
    # except Item.DoesNotExist:
    #     raise Http404("Item does not exist")

    #can also use
    item = get_object_or_404(Item, pk=item_id)

    return render(request, "polls/details.html", {"item": item})

