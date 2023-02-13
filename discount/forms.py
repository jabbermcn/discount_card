from django.forms import *

from .models import *


class CardCreateForm(ModelForm):
    class Meta:
        model = Card
        fields = ['id', 'status', 'seria', 'date_created', 'expire_date']


def get_status_choices():
    statuses = CardStatus.objects.filter()
    return [[0, '...']] + [[status.id, status.name] for status in statuses]


def get_series_choices():
    statuses = CardSeries.objects.filter()
    return [[0, '...']] + [[status.id, status.name] for status in statuses]


class CardFilter(Form):
    id = IntegerField(label='number', required=False)
    status = ChoiceField(
        choices=get_status_choices(),
        required=False,
    )
    seria = ChoiceField(
        choices=get_series_choices(),
        required=False,
    )
