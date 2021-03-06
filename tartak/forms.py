#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import Decimal

from django import forms

from tartak.models import Order_item, Shipment, Order, Contractor, Final_shipment, Driver, Contractor_shipment, Deal, \
    Forest_district, Wood_kind


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
        amount = self.cleaned_data['order'].get_difference()
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
        """:returns order_list, final_shipment_list, contractor_shipment_list"""
        date_from = self.cleaned_data['date_from']
        date_to = self.cleaned_data['date_to']
        driver = self.cleaned_data['driver']

        order_list = Order.objects.filter(driver=driver, date__gte=date_from, date__lte=date_to)
        final_shipment_list = Final_shipment.objects.filter(driver=driver, date__gte=date_from, date__lte=date_to)
        contractor_shipment_list = Contractor_shipment.objects.filter(driver=driver, date__gte=date_from, date__lte=date_to)

        return order_list, final_shipment_list, contractor_shipment_list


class DepotReportForm(forms.Form):
    date_from = forms.DateField(label='Od')
    date_to = forms.DateField(label='Do')
    contractor = forms.ModelChoiceField(queryset=Contractor.objects.filter(is_depot=True), label='Składnica')

    def get_context_for_depot(self):
        """:returns shipment_list, contractor_shipment_list"""
        date_from = self.cleaned_data['date_from']
        date_to = self.cleaned_data['date_to']
        contractor = self.cleaned_data['contractor']

        shipment_list = Shipment.objects.filter(contractor=contractor, order__date__gte=date_from, order__date__lte=date_to)
        contractor_shipment_list = Contractor_shipment.objects.filter(depot=contractor, date__gte=date_from, date__lte=date_to)

        return shipment_list, contractor_shipment_list


class ContractorReportForm(forms.Form):
    date_from = forms.DateField(label='Od')
    date_to = forms.DateField(label='Do')
    contractor = forms.ModelChoiceField(queryset=Contractor.objects.filter(is_depot=False), label='Kontrahent')

    def get_context_for_contractor(self):
        """:returns final_shipment_list, contractor_shipment_list"""
        date_from = self.cleaned_data['date_from']
        date_to = self.cleaned_data['date_to']
        contractor = self.cleaned_data['contractor']

        final_shipment_list = Final_shipment.objects.filter(contractor=contractor, date__gte=date_from, date__lte=date_to)
        contractor_shipment_list = Contractor_shipment.objects.filter(contractor=contractor, date__gte=date_from, date__lte=date_to)

        return final_shipment_list, contractor_shipment_list


class WoodKindReportForm(forms.Form):
    date_from = forms.DateField(label='Od')
    date_to = forms.DateField(label='Do')
    forest_district = forms.ModelChoiceField(queryset=Forest_district.objects.all(), label='Składnica')
    wood_kinds = forms.ModelMultipleChoiceField(queryset=Wood_kind.objects.all(), label='Sortyment')

    def clean_wood_kinds(self):
        wood_kinds = self.cleaned_data['wood_kinds']
        forest_district = self.cleaned_data['forest_district']
        for wood_kind in wood_kinds:
            if not forest_district.wood_kinds.filter(code=wood_kind.code).exists():
                raise forms.ValidationError("Prosze wybrac tylko sortymenty z kodem rozpoczynajacym sie od " + forest_district.code + "!")
        return wood_kinds

    def get_context_for_wood_kinds(self):
        """:returns order_item_list"""
        date_from = self.cleaned_data['date_from']
        date_to = self.cleaned_data['date_to']
        forest_district = self.cleaned_data['forest_district']
        wood_kinds = self.cleaned_data['wood_kinds']

        order_item_list = Order_item.objects.filter(order__date__gte=date_from, order__date__lte=date_to, order__forest_district=forest_district, wood_kind__in=wood_kinds)

        return order_item_list


class DealReportForm(forms.Form):
    deal = forms.ModelChoiceField(queryset=Deal.objects.all(), label='Umowa')

    def get_context_for_deal(self):
        """:returns order_item_list"""
        deal = self.cleaned_data['deal']

        order_item_list = Order_item.objects.filter(order__forest_district=deal.forest_district, order__date__lte=deal.date_to, order__date__gte=deal.date_from)

        return order_item_list


class ContractorShipmentForm(forms.ModelForm):
    class Meta:
        model = Contractor_shipment
        fields = ('depot', 'contractor',  'wood_type', 'amount', 'date', 'driver')
        widgets = {
            'depot': forms.HiddenInput,
        }