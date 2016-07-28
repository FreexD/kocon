#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator
from django.db import models

import itertools

class Driver(models.Model):
    """Model definition for DRIVER"""
    code = models.CharField(max_length=30, unique=True, verbose_name='Kod')
    first_name = models.CharField(max_length=50, verbose_name='Imię')
    last_name = models.CharField(max_length=50, verbose_name='Nazwisko')

    class Meta:
        verbose_name='Kierowca'
        verbose_name_plural='Kierowcy'

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __unicode__(self):
        return self.first_name + " " + self.last_name


class Forest_district(models.Model):
    """Model definition for FOREST DISTRICT"""
    code = models.CharField(max_length=30, unique=True, verbose_name='Kod')
    name = models.CharField(max_length=100, verbose_name='Nazwa')

    class Meta:
        verbose_name = 'Nadleśnictwo'
        verbose_name_plural = 'Nadleśnictwa'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_deal_by_date(self, date):
        for deal in self.deals.all():
            if deal.is_date_valid(date):
                return deal
        return None



class Wood_kind(models.Model):
    """Model definition for WOOD KIND"""
    code = models.CharField(max_length=30, unique=True, verbose_name='Kod')
    forest_district = models.ForeignKey('Forest_district', on_delete=models.CASCADE, related_name='wood_kinds', verbose_name='Nadleśnictwo')
    detail_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Cena', validators=[MinValueValidator(Decimal('0.00'))])

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code

    def get_action_buttons(self):
        return '<a href="' \
               + reverse('wood_kind_delete', kwargs={'pk': self.pk}) + \
               '" data-remote="false" data-toggle="modal" data-target="#myModal" class="btn btn-sm btn-danger">' \
               '<span class="glyphicon glyphicon-trash" aria-hidden="true">' \
               '</span>' \
               '</a>'

    def get_absolute_url(self):
        return reverse('price_list')

    def can_delete(self):
        return not self.order_items.all().exists()

    class Meta:
        verbose_name = 'Sortyment'
        verbose_name_plural = 'Sortymenty'


class Order_item(models.Model):
    """Model definition for ORDER ITEM"""
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_items', verbose_name='Kwit wywozowy')
    wood_kind = models.ForeignKey('Wood_kind', on_delete=models.CASCADE, related_name='order_items', verbose_name='Sortyment')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Masa', validators=[MinValueValidator(Decimal('0.01'))])  # in m3
    detail_price = models.DecimalField(default=0, max_digits=12, decimal_places=2, verbose_name='Cena detaliczna', validators=[MinValueValidator(Decimal('0.00'))])

    def clean(self):
        if self.wood_kind not in self.order.forest_district.wood_kinds.all():
            raise ValidationError({'wood_kind':'Prosze wybrać sortyment oferowany przez {fd} (kod {fdk}).'
                                  .format(fd=self.order.forest_district, fdk=self.order.forest_district.code)})

        deal = self.order.forest_district.get_deal_by_date(self.order.date)
        remaining = deal.get_remaining(self.wood_kind)
        if self.amount > remaining:
            raise ValidationError({'amount': 'Prosze wybrać mniej drewna. Na umowie {d} zostało go jeszcze {rm} m3.'
                                  .format(rm=remaining, d=deal)})

    def save(self, **kwargs):
        try:
            former_order_item = Order_item.objects.get(pk=self.pk)
        except Order_item.DoesNotExist:
            former_order_item = None
        amount_delta = Decimal(0)
        deal = self.order.forest_district.get_deal_by_date(self.order.date)
        remaining = deal.get_remaining(self.wood_kind)
        if former_order_item:
            amount_delta = former_order_item.amount - self.amount
        if remaining + amount_delta >= 0:
            return super(Order_item, self).save(**kwargs)
        return

    def can_delete(self):
        for shipment in self.order.shipments.all():
            if shipment.wood_kind == self.wood_kind:
                return False
        return True

    def delete(self, using=None, keep_parents=False):
        if not self.can_delete():
            raise ValidationError({'amount': 'Usuniecie pozycji spowodowaloby powstanie ujemnej roznicy.'})
        return super(Order_item, self).delete(using=None, keep_parents=False)

    def __str__(self):
        return self.order.__str__() + " - " + self.wood_kind.__str__() + " - " + self.amount.__str__()

    def __unicode__(self):
        return self.order.__unicode__() + " - " + self.wood_kind.__unicode__() + " - " + self.amount.__str__()

    # difference

    def get_difference(self):
        difference = self.amount
        if self.order.is_depot():
            for shipment in self.order.shipments.all():
                if shipment.wood_kind == self.wood_kind:
                    difference -= shipment.amount
        return difference

    def has_difference(self):
        return not self.get_difference() <= 0

    def get_difference_display(self):
        difference = self.get_difference()
        if self.has_difference():
            return round(-self.get_difference(), 2).__str__()
        elif difference == 0:
            return round(self.get_difference(), 2).__str__()
        else:
            return '+' + round(abs(self.get_difference()), 2).__str__()

    def is_fully_shipped(self):
        """:return true if difference between amount and final_shipments amount <= 0"""
        return not self.has_difference()

    def get_price(self):
        return self.amount * self.detail_price

    def get_detail_price_display(self):
        return self.detail_price.__str__()

    def get_price_display(self):
        return round(self.get_price(), 2).__str__()

    def get_difference_display_for_datatables(self):
        if self.is_fully_shipped():
            return self.get_difference_display()
        else:
            return self.get_difference_display() + \
                    ' <span ' \
                    'class="glyphicon glyphicon-alert" ' \
                    'aria-hidden="true" ' \
                    'data-toggle="tooltip" ' \
                    'title="Order item not fully shipped!">' \
                    '</span>'

    def get_amount_display(self):
        return self.amount.__str__()

    def get_absolute_url(self):
        return reverse('order_item_list', kwargs={'pk': self.order.pk })

    def get_action_buttons(self):
        return '<a href="' \
               + reverse('order_item_delete', kwargs={'pk': self.pk}) + \
               '" data-remote="false" data-toggle="modal" data-target="#myModal" class="btn btn-sm btn-danger">' \
               '<span class="glyphicon glyphicon-trash" aria-hidden="true">' \
               '</span>' \
               '</a>'

    class Meta:
        verbose_name = 'Pozycja dostawy'
        verbose_name_plural = 'Pozycje dostawy'
        unique_together = ('order', 'wood_kind')


class Contractor(models.Model):
    """Model definition for CONTRACTOR"""
    code = models.CharField(max_length=30, unique=True, verbose_name='Kod')
    name = models.CharField(max_length=100, verbose_name='Nazwa')
    is_depot = models.BooleanField(default=False, verbose_name='Składnica')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def has_shipments(self):
        return self.shipments.all().exists()

    def get_wood_kind_amount_map(self):
        wood_kind_map = {}
        for shipment in self.shipments.all():
            if shipment.wood_kind in wood_kind_map.keys():
                wood_kind_map[shipment.wood_kind] += shipment.amount
            else:
                wood_kind_map[shipment.wood_kind] = shipment.amount
        return wood_kind_map

    def get_wood_kind_amount_display_map(self):
        wood_kind_map = self.get_wood_kind_amount_map()
        for wood_kind in wood_kind_map.keys():
            wood_kind_map[wood_kind] = round(wood_kind_map[wood_kind], 2).__str__()
        return wood_kind_map

    def get_all_amount(self):
        amount = Decimal(0.0)
        for shipment in self.shipments.all():
            amount += shipment.amount
        return amount

    def get_all_amount_display(self):
        return round(self.get_all_amount(), 2).__str__()

    def get_depot_amount_until(self, date):
        depot_amount = Decimal(0)
        if self.is_depot:
            shipments = Shipment.objects.filter(contractor=self, order__date__lt=date)
            contractor_shipments = Contractor_shipment.objects.filter(depot=self, date__lt=date)
            for shipment, contractor_shipment in itertools.izip_longest(shipments, contractor_shipments):
                # print('{} {} {}'.format(shipment, contractor_shipment, depot_amount))
                if shipment:
                    depot_amount += shipment.amount
                if contractor_shipment:
                    depot_amount -= contractor_shipment.amount
        return depot_amount

    def get_depot_amount(self):
        depot_amount = Decimal(0)
        if self.is_depot:
            shipments = Shipment.objects.filter(contractor=self)
            contractor_shipments = Contractor_shipment.objects.filter(depot=self)
            for shipment, contractor_shipment in itertools.izip_longest(shipments, contractor_shipments):
                # print('{} {} {}'.format(shipment, contractor_shipment, depot_amount))
                if shipment:
                    depot_amount += shipment.amount
                if contractor_shipment:
                    depot_amount -= contractor_shipment.amount
        return depot_amount

    def get_depot_amount_display(self):
        return round(self.get_depot_amount(), 2).__str__()

    def get_action_buttons(self):
        buttons = '<a href="' \
                  + reverse('contractor_shipment_list', kwargs={'pk': self.pk}) + \
                  '" class="btn btn-sm btn-info">' \
                  '<span class="glyphicon glyphicon-road" aria-hidden="true">' \
                  '</span>' \
                  '</a>' \
                  '<a href="' \
                  + reverse('shipment_for_depot_list', kwargs={'pk': self.pk}) + \
                  '" class="btn btn-sm btn-success">' \
                  '<span class="glyphicon glyphicon-tree-conifer" aria-hidden="true">' \
                  '</span>' \
                  '</a>' \
                  '<a href="' \
                  + reverse('contractor_shipment_create', kwargs={'pk': self.pk}) + \
                  '" class="btn btn-sm btn-info">' \
                  ' <span class="glyphicon glyphicon-road" aria-hidden="true">' \
                  '</span> Dodaj' \
                  '</a>'
        return buttons

    class Meta:
        verbose_name = 'Kontrahent'
        verbose_name_plural = 'Kontrahenci'


class Shipment(models.Model):
    """Model definition for SHIPMENT"""
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='shipments', verbose_name='Kwit wywozowy')
    contractor = models.ForeignKey('Contractor', on_delete=models.CASCADE, related_name='shipments', verbose_name='Kontrahent')
    wood_kind = models.ForeignKey('Wood_kind', on_delete=models.CASCADE, related_name='shipments', verbose_name='Sortyment')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Masa', validators=[MinValueValidator(Decimal('0.01'))])  # in m3

    class Meta:
        verbose_name = 'Dostawa pośrednia'
        verbose_name_plural = 'Dostawy pośrednie'

    def clean(self):
        if self.wood_kind not in self.order.get_wood_kinds():
            raise ValidationError({'wood_kind': 'Prosze wybrać sortyment będący w pozycjach dostawy kwitu wywozowego.'})

    def save(self, **kwargs):
        return super(Shipment, self).save(**kwargs)

    def __str__(self):
        return self.order.__str__() + " - " + self.wood_kind.__str__() + " - " + self.amount.__str__()

    def __unicode__(self):
        return self.order.__unicode__() + " - " + self.wood_kind.__unicode__() + " - " + self.amount.__str__()

    def get_amount_display(self):
        return self.amount.__str__()

    def get_absolute_url(self):
        return reverse('shipment_list', kwargs={'pk': self.order.pk})

    def get_action_buttons(self):
        return '<a href="' \
               + reverse('shipment_delete', kwargs={'pk': self.pk}) + \
               '" data-remote="false" data-toggle="modal" data-target="#myModal" class="btn btn-sm btn-danger">' \
               '<span class="glyphicon glyphicon-trash" aria-hidden="true">' \
               '</span>' \
               '</a>'


class Order(models.Model):
    """Model definition for ORDER"""
    code = models.CharField(max_length=30, unique=True, verbose_name='WZ')  # WZ
    forest_district = models.ForeignKey('Forest_district', on_delete=models.CASCADE, related_name='orders', verbose_name='Nadleśnictwo')
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='orders', verbose_name='Kierowca')
    date = models.DateField(verbose_name='Data')
    pieces = models.IntegerField(default=0, verbose_name='Liczba sztuk', validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Kwit wywozowy'
        verbose_name_plural = 'Kwity wywozowe'

    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code

    def is_depot(self):
        """:return true if shipments and no final shipments in the order, false otherwise"""
        return self.has_shipments() and not self.has_final_shipments()

    def is_empty(self):
        """:return true if has no shipments and final shipments"""
        return not self.has_shipments() and not self.has_final_shipments()

    def is_both(self):
        """:return true if has shipments and final shipments"""
        return self.has_shipments() and self.has_final_shipments()

    def is_fully_shipped(self):
        """:return true if no differences between order_items and final_shipments amounts"""
        return not self.has_difference()

    def get_action_buttons(self):
        buttons = '<a href="'\
               + reverse('order_detail', kwargs={'pk': self.pk}) + \
               '" data-remote="false" data-toggle="modal" data-target="#myModal" class="btn btn-sm btn-primary">' \
               '<span class="glyphicon glyphicon-info-sign" aria-hidden="true">' \
               '</span>' \
               '</a>' \
               '<a href="' \
               + reverse('order_delete', kwargs={'pk': self.pk}) + \
               '" data-remote="false" data-toggle="modal" data-target="#myModal" class="btn btn-sm btn-danger">' \
               '<span class="glyphicon glyphicon-trash" aria-hidden="true">' \
               '</span>' \
               '</a>'
        if not self.is_fully_shipped():
            buttons += ' <span ' \
                    'class="glyphicon glyphicon-alert" style="float:right" ' \
                    'aria-hidden="true" ' \
                    'data-toggle="tooltip" ' \
                    'title="Kwit wywozowy nie w pełni dostarczony!">' \
                    '</span>'
        return buttons

    def get_absolute_url(self):
        return reverse('order_list')

    # Price and Amount

    def get_price(self):
        """:returns order's price"""
        price = Decimal(0)
        for order_item in self.order_items.all():
            price += order_item.get_price()
        return price

    def get_amount(self):
        """:returns order's amount"""
        amount = Decimal(0)
        for order_item in self.order_items.all():
            amount += order_item.amount
        return amount

    def get_price_display(self):
        return round(self.get_price(), 2).__str__()

    def get_amount_display(self):
        return round(self.get_amount(), 2).__str__()

    # has functions

    def has_order_items(self):
        return self.order_items.all().exists()

    def has_shipments(self):
        return self.shipments.all().exists()

    def has_final_shipments(self):
        return self.final_shipments.all().exists()

    # wood kinds

    def get_wood_kinds(self):
        """:returns list of ordered wood kinds"""
        wood_kinds = []
        for order_item in self.order_items.all():
            wood_kinds.append(order_item.wood_kind)
        return wood_kinds

    def get_shipped_wood_kinds(self):
        """:returns list of shipped wood kinds if is_depot"""
        shipped_wood_kinds = []
        if self.is_depot():
            for shipment in self.shipments.all():
                if shipment.wood_kind not in shipped_wood_kinds:
                    shipped_wood_kinds.append(shipment.wood_kind)
        return shipped_wood_kinds

    # shipped amount

    def get_shipped_amount(self):
        """:returns shipped or finally shipped amount"""
        shipped_amount = Decimal(0)
        if self.is_depot():
            for shipment in self.shipments.all():
                shipped_amount += shipment.amount
        else:
            for final_shipment in self.final_shipments.all():
                shipped_amount += final_shipment.amount
        return shipped_amount

    def get_shipped_amount_display(self):
        return round(self.get_shipped_amount(), 2).__str__()

    # differences

    def get_differences(self):
        """:returns map with differences between order_items and shipments if is_depot"""
        differences_map = {}
        if self.is_depot() or self.is_empty():
            for order_item in self.order_items.all():
                differences_map[order_item.wood_kind] = order_item.amount
            for shipment in self.shipments.all():
                differences_map[shipment.wood_kind] -= shipment.amount
        return differences_map

    def get_difference(self):
        """:returns differences between order_items and shipments if is_depot, final_shipments otherwise"""
        difference = Decimal(0)
        for order_item in self.order_items.all():
            difference += order_item.amount
        if self.is_depot():
            for shipment in self.shipments.all():
                difference -= shipment.amount
        else:
            for final_shipment in self.final_shipments.all():
                difference -= final_shipment.amount
        return difference

    def get_difference_display(self):
        difference = self.get_difference()
        if self.has_difference():
            return round(-self.get_difference(), 2).__str__()
        elif difference == 0:
            return round(self.get_difference(), 2).__str__()
        else:
            return '+'+round(abs(self.get_difference()), 2).__str__()

    def has_difference(self):
        return not self.get_difference() <= 0


class Final_shipment(models.Model):
    """Model definition for FINAL SHIPMENT"""
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='final_shipments', verbose_name='Kwit wywozowy')
    contractor = models.ForeignKey('Contractor', on_delete=models.CASCADE, related_name='final_shipments', verbose_name='Kontrahent')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Masa', validators=[MinValueValidator(Decimal('0.01'))])  # in m3
    date = models.DateField(verbose_name='Data')
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='final_shipments', verbose_name='Kierowca')
    wood_type = models.CharField(max_length=100, verbose_name='Rodzaj drewna (po manipulacji)', default='Brak manipulacji')

    class Meta:
        verbose_name = 'Dostawa końcowa'
        verbose_name_plural = 'Dostawy końcowe'

    def save(self, **kwargs):
        return super(Final_shipment, self).save(**kwargs)

    def __str__(self):
        return self.order.__str__() + " - " + self.wood_type.__str__() + " - " + self.amount.__str__()

    def __unicode__(self):
        return self.order.__unicode__() + " - " + self.wood_type.__str__() + " - " + self.amount.__str__()

    def get_amount_display(self):
        return self.amount.__str__()

    def get_absolute_url(self):
        return reverse('final_shipment_list', kwargs={'pk': self.order.pk})

    def get_action_buttons(self):
        return '<a href="' \
               + reverse('final_shipment_delete', kwargs={'pk': self.pk}) + \
               '" data-remote="false" data-toggle="modal" data-target="#myModal" class="btn btn-sm btn-danger">' \
               '<span class="glyphicon glyphicon-trash" aria-hidden="true">' \
               '</span>' \
               '</a>'


class Contractor_shipment(models.Model):
    """Model definition for CONTRACTOR SHIPMENT"""
    depot = models.ForeignKey('Contractor', on_delete=models.CASCADE, related_name='contractor_shipments_from', verbose_name='Składnica')
    contractor = models.ForeignKey('Contractor', on_delete=models.CASCADE, related_name='contractor_shipments_to', verbose_name='Kontrahent')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Masa', validators=[MinValueValidator(Decimal('0.01'))])  # in m3
    date = models.DateField(verbose_name='Data')
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='contractor_shipments', verbose_name='Kierowca')
    wood_type = models.CharField(max_length=100, verbose_name='Rodzaj drewna (po manipulacji)', default='Brak manipulacji')

    class Meta:
        verbose_name = 'Dostawa końcowa ze składnicy'
        verbose_name_plural = 'Dostawy końcowe ze składnicy'

    def save(self, **kwargs):
        return super(Contractor_shipment, self).save(**kwargs)

    def __str__(self):
        return self.depot.__str__() + " - " + self.wood_type.__str__() + " - " + self.amount.__str__()

    def __unicode__(self):
        return self.depot.__unicode__() + " - " + self.wood_type.__str__() + " - " + self.amount.__str__()

    def get_amount_display(self):
        return self.amount.__str__()

    def get_absolute_url(self):
        return reverse('contractor_shipment_list', kwargs={'pk': self.order.pk})

    def get_action_buttons(self):
        return '<a href="' \
               + reverse('contractor_shipment_delete', kwargs={'pk': self.pk}) + \
               '" data-remote="false" data-toggle="modal" data-target="#myModal" class="btn btn-sm btn-danger">' \
               '<span class="glyphicon glyphicon-trash" aria-hidden="true">' \
               '</span>' \
               '</a>'


class Deal(models.Model):
    """Model definition for Deal"""
    forest_district = models.ForeignKey('Forest_district', on_delete=models.CASCADE, related_name='deals', verbose_name='Nadleśnictwo')
    code = models.CharField(max_length=30, unique=True, verbose_name='Kod')
    name = models.CharField(max_length=100, verbose_name='Nazwa')
    date_from = models.DateField(verbose_name='Obowiązuje od')
    date_to = models.DateField(verbose_name='Obowiązuje do')

    class Meta:
        verbose_name = 'Umowa'
        verbose_name_plural = 'Umowy'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def is_date_valid(self, date):
        return self.date_from <= date <= self.date_to

    def get_remaining(self, wood_kind):
        for deal_item in self.deal_items.all():
            if deal_item.code in wood_kind.code:
                return deal_item.get_remaining()


class Deal_item(models.Model):
    """Model definition for Deal item"""
    deal = models.ForeignKey('Deal', on_delete=models.CASCADE, related_name='deal_items', verbose_name='Umowa')
    code = models.CharField(max_length=30, verbose_name='Kod sortymentu', help_text='np. W_STANDARD_SW')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Masa',
                                 validators=[MinValueValidator(Decimal('0.01'))])  # in m3

    class Meta:
        verbose_name = 'Pozycja umowy'
        verbose_name_plural = 'Pozycje umowy'

    def __str__(self):
        return self.deal.name + ' - ' + self.code

    def __unicode__(self):
        return self.deal.name + ' - ' + self.code

    def get_remaining(self):
        remaining = self.amount
        order_item_list = Order_item.objects.filter(wood_kind__code__icontains=self.code, order__date__gte=self.deal.date_from, order__date__lte=self.deal.date_to)
        for order_item in order_item_list:
            remaining -= order_item.amount
        return remaining

    def get_amount_display(self):
        return self.amount.__str__()

    def get_remaining_display(self):
        return round(self.get_remaining(), 2).__str__()
