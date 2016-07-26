from decimal import Decimal

from django import forms

from tartak.models import Order_item, Shipment, Order, Contractor, Final_shipment, Driver


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
    order = forms.ModelChoiceField(queryset=Order.objects.all(), widget=forms.HiddenInput, label='Kwit wywozowy')
    contractor = forms.ModelChoiceField(queryset=Contractor.objects.all(), label='Kontrahent')

    def create_all_shipments_for_order(self):
        for wood_kind, amount in self.cleaned_data['order'].get_differences().items():
            if amount != Decimal(0.0):
                Shipment.objects.create(order=self.cleaned_data['order'],
                                        contractor=self.cleaned_data['contractor'],
                                        wood_kind=wood_kind,
                                        amount=amount)


class ContractorForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ('contractor',)


class FinalShipmentForm(forms.ModelForm):
    class Meta:
        model = Final_shipment
        fields = ('order', 'contractor',  'wood_type', 'amount', 'date', 'driver')
        widgets = {
            'order': forms.HiddenInput,
        }


class AllFinalShipmentForm(forms.Form):
    order = forms.ModelChoiceField(queryset=Order.objects.all(), widget=forms.HiddenInput, label='Kwit wywozowy')
    contractor = forms.ModelChoiceField(queryset=Contractor.objects.all(), label='Kontrahent')
    date = forms.DateField(label='Data')
    driver = forms.ModelChoiceField(queryset=Driver.objects.all(), label='Kierowca')
    wood_type = forms.CharField(max_length=100, label='Rodzaj drewna (po manipulacji)', initial='Brak manipulacji')

    def create_all_final_shipments_for_order(self):
        amount = self.cleaned_data['order'].get_final_difference()
        if amount != Decimal(0.0):
            Final_shipment.objects.create(order=self.cleaned_data['order'],
                                          contractor=self.cleaned_data['contractor'],
                                          date=self.cleaned_data['date'],
                                          driver=self.cleaned_data['driver'],
                                          wood_type=self.cleaned_data['wood_type'],
                                          amount=amount)


class DriverReportForm(forms.Form):
    date_from = forms.DateField(label='Od')
    date_to = forms.DateField(label='Do')
    driver = forms.ModelChoiceField(queryset=Driver.objects.all(), label='Kierowca')

    def get_context_for_driver(self):
        """:returns order_list, final_shipment_list"""
        date_from = self.cleaned_data['date_from']
        date_to = self.cleaned_data['date_to']
        driver = self.cleaned_data['driver']

        order_list = Order.objects.filter(driver=driver, date__gte=date_from, date__lte=date_to)
        final_shipment_list = Final_shipment.objects.filter(driver=driver, date__gte=date_from, date__lte=date_to)

        return order_list, final_shipment_list
