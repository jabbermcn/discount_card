from django.forms import *

from .models import *


class CardCreateForm(ModelForm):
    class Meta:
        model = Card
        fields = ['card_number', 'status', 'series', 'date_created', 'expire_date']


def get_status_choices():
    statuses = CardStatus.objects.filter()
    return [[0, '...']] + [[status.id, status.name] for status in statuses]


def get_series_choices():
    series = CardSeries.objects.filter()
    return [[0, '...']] + [[series.id, series.name] for series in series]


class CardFilter(Form):
    id = IntegerField(label='number', required=False)
    status = ChoiceField(
        choices=get_status_choices(),
        required=False,
    )
    series = ChoiceField(
        choices=get_series_choices(),
        required=False,
    )
