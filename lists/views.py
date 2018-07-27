from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item


def home_page(request):

    new_item_text = request.POST.get("item_text")
    if new_item_text:
        Item.objects.create(text=new_item_text)
        #item = Item()
        #item.text = item_text
        # item.save()
        return redirect('/')

    items = Item.objects.all()
    return render(request, "home.html", {
        "items": items
    })
