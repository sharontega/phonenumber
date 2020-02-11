from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView
from . models import add
class addcontact(CreateView):
    model= add
    template_name='add.html'
    fields='__all__'
class listcontact(ListView):
    model=add
    template_name='list.html'
class detailcontact(DetailView):
    model=add
    template_name='detail.html'