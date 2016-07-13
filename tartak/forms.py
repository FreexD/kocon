from django import forms

from tartak.models import Order_item, Shipment, Order, Contractor


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = Order_item
        fields = ('order', 'wood_kind', 'amount', 'detail_price')
        widgets = {
            'order': forms.HiddenInput,
        }


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ('order', 'contractor', 'wood_kind', 'amount')
        widgets = {
            'order': forms.HiddenInput,
        }


class AllShipmentForm(forms.Form):
    order = forms.ModelChoiceField(queryset=Order.objects.all(), widget=forms.HiddenInput)
    contractor = forms.ModelChoiceField(queryset=Contractor.objects.all())

    def create_all_shipments_for_order(self):
        for order_item in self.cleaned_data['order'].order_items.all():
            Shipment.objects.create(order=self.cleaned_data['order'],
                                    contractor=self.cleaned_data['contractor'],
                                    wood_kind=order_item.wood_kind,
                                    amount=order_item.amount)


class ContractorForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ('contractor',)

