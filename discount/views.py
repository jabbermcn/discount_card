from django.views.generic import CreateView, ListView, DetailView, TemplateView

from .forms import *
from .models import Card


class ContextMixin:
    context = {
        'site_title': '*****',
        'site_name': 'mikhailouski_n',
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'linkedin': 'https://www.linkedin.com/in/николай-михайловский-612744246/',
        'instagram': 'https://instagram.com',
        'email': 'jabber_mcn@tut.by',
        'Github': 'https://github.com/jabbermcn',
        'phone': '+375 29 5692410',
    }


class HomeTemplateView(ContextMixin, TemplateView):
    template_name = 'discount/base.html'

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data()
        context.update(self.context)
        return context


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
        context['form'] = ChangeStatus()
        context['orders'] = Order.objects.filter(card__id=context.get('card').id)
        return context
