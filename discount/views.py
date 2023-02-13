from django.views.generic import CreateView, ListView, DetailView

from .forms import *
from .models import Card


class CardCreateView(CreateView):
    form_class = CardCreateForm
    template_name = 'discount/card_add.html'
    success_url = '/card/add'


class CardListView(ListView):
    model = Card
    template_name = 'discount/card_list.html'
    context_object_name = 'cards'

    def get_queryset(self):
        filters = dict(
            filter(
                lambda x: str(x[1]) > '0' and x[0] != 'csrfmiddlewaretoken',
                self.request.GET.dict().items()
            )
        )
        return Card.objects.filter(**filters)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['form'] = CardFilter()
        return context


class CardDetailView(DetailView):
    model = Card
    pk_url_kwarg = 'card_id'
    context_object_name = 'card'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['orders'] = Order.objects.filter(card__id=context.get('card').id)
        return context
