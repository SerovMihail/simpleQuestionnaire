from django.shortcuts import render
from .forms import SubscriberForm


def landing(request):
    name = "yahooly"
    form = SubscriberForm(request.POST or None)

    if request.method == 'POST':
        print(form)
        form.save()

    return render(request, 'landing/index.html', locals())
