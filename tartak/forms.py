from django.forms import ModelForm, HiddenInput

from tartak.models import Order_item, Shipment


class OrderItemForm(ModelForm):
    class Meta:
        model = Order_item
        fields = ('order', 'wood_kind', 'amount', 'detail_price')
        widgets = {
            'order': HiddenInput,
        }


class ShipmentForm(ModelForm):
    class Meta:
        model = Shipment
        fields = ('order', 'contractor', 'wood_kind', 'amount')
        widgets = {
            'order': HiddenInput,
        }


class ContractorForm(ModelForm):
    class Meta:
        model = Shipment
        fields = ('contractor',)

