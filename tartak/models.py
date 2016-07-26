#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import MinValueValidator
from django.db import models


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
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Nadleśnictwo'
        verbose_name_plural = 'Nadleśnictwa'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


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

        if self.calculate_difference() < 0:
            raise ValidationError({'amount': 'Prosze wprowadzić masę nie powodującą powstania ujemnej różnicy dla dostawy pośredniej.'})

        if self.calculate_final_difference() < 0:
            raise ValidationError({'amount': 'Prosze wprowadzić masę nie powodującą powstania ujemnej różnicy dla dostawy końcowej.'})

    def save(self, **kwargs):
        if self.calculate_difference() < 0 or self.calculate_final_difference() < 0:
            return
        return super(Order_item, self).save(**kwargs)

    def can_delete(self):
        for final_shipment in self.order.final_shipments.all():
            if final_shipment.wood_kind == self.wood_kind:
                return False
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

    def calculate_difference(self):
        difference = self.amount
        for shipment in self.order.final_shipments.all():
            if shipment.wood_kind == self.wood_kind:
                difference -= shipment.amount
        return difference

    def calculate_final_difference(self):
        difference = self.amount
        for final_shipment in self.order.final_shipments.all():
            if final_shipment.wood_kind == self.wood_kind:
                difference -= final_shipment.amount
        return difference

    def get_difference_display(self):
        return round(self.calculate_difference(), 2).__str__()

    def is_fully_shipped(self):
        """:return true if difference between amount and final_shipments amount == 0"""
        return self.calculate_difference() == 0

    def calculate_price(self):
        return self.amount * self.detail_price

    def get_detail_price_display(self):
        return self.detail_price.__str__()

    def get_price_display(self):
        return round(self.calculate_price(), 2).__str__()

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

        max_amount = self.order.get_differences()[self.wood_kind]
        if self.amount > max_amount:
            if max_amount == 0:
                raise ValidationError({'wood_kind': 'Prosze wybrać sortyment nie będący już w pełni dostarczony.'})
            else:
                raise ValidationError({'amount': 'Prosze wybrać mniejszą masę. Tego sortymentu zostało jeszcze {amount} m³.'.format(amount=max_amount)})

    def save(self, **kwargs):
        try:
            former_shipment = Shipment.objects.get(pk=self.pk)
        except Shipment.DoesNotExist:
            former_shipment = None
        amount_delta = Decimal(0)
        if former_shipment:
            amount_delta = former_shipment.amount - self.amount
        if not self.calculate_difference() + amount_delta >= 0:
            return
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

    def calculate_difference(self):
        for order_item in self.order.order_items.all():
            if self.wood_kind == order_item.wood_kind:
                return order_item.calculate_difference()


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

    def get_differences(self):
        """:returns map with differences between order_items and shipments"""
        differences_map = {}
        for order_item in self.order_items.all():
            differences_map[order_item.wood_kind] = order_item.amount
        for shipment in self.shipments.all():
            differences_map[shipment.wood_kind] -= shipment.amount
        return differences_map

    def get_final_differences(self):
        """:returns map with differences between order_items and final_shipments"""
        differences_map = {}
        for order_item in self.order_items.all():
            differences_map[order_item.wood_kind] = order_item.amount
        for final_shipment in self.final_shipments.all():
            differences_map[final_shipment.wood_kind] -= final_shipment.amount
        return differences_map

    def is_fully_shipped(self):
        """:return true if no differences between order_items and final_shipments amounts"""
        for amounts in self.get_final_differences().values():
            if amounts != 0:
                return False
        return True

    def is_fully_shipped_indirect(self):
        """:return true if no differences between order_items and shipments amounts"""
        for amounts in self.get_differences().values():
            if amounts != 0:
                return False
        return True

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

    def calculate_price(self):
        price = Decimal(0)
        for order_item in self.order_items.all():
            price += order_item.calculate_price()
        return price

    def calculate_amount(self):
        amount = Decimal(0)
        for order_item in self.order_items.all():
            amount += order_item.amount
        return amount

    def get_price_display(self):
        return round(self.calculate_price(), 2).__str__()

    def get_amount_display(self):
        return round(self.calculate_amount(), 2).__str__()

    def has_order_items(self):
        return self.order_items.all().exists()

    def has_shipments(self):
        return self.shipments.all().exists()

    def has_final_shipments(self):
        return self.final_shipments.all().exists()

    def get_wood_kinds(self):
        wood_kinds = []
        for order_item in self.order_items.all():
            wood_kinds.append(order_item.wood_kind)
        return wood_kinds

    def get_shipped_wood_kinds(self):
        shipped_wood_kinds = []
        for shipment in self.shipments.all():
            if shipment.wood_kind not in shipped_wood_kinds:
                shipped_wood_kinds.append(shipment.wood_kind)
        return shipped_wood_kinds

    def get_shipped_amount(self):
        shipped_amount = Decimal(0)
        for shipment in self.shipments.all():
            shipped_amount += shipment.amount
        return shipped_amount

    def get_shipped_amount_display(self):
        return round(self.get_shipped_amount(), 2).__str__()


class Final_shipment(models.Model):
    """Model definition for FINAL SHIPMENT"""
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='final_shipments', verbose_name='Kwit wywozowy')
    contractor = models.ForeignKey('Contractor', on_delete=models.CASCADE, related_name='final_shipments', verbose_name='Kontrahent')
    wood_kind = models.ForeignKey('Wood_kind', on_delete=models.CASCADE, related_name='final_shipments', verbose_name='Sortyment')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Masa', validators=[MinValueValidator(Decimal('0.01'))])  # in m3
    date = models.DateField(verbose_name='Data')
    driver = models.ForeignKey('Driver', on_delete=models.CASCADE, related_name='final_shipments', verbose_name='Kierowca')
    wood_type = models.CharField(max_length=100, verbose_name='Rodzaj drewna (po manipulacji)', default='Brak manipulacji')

    class Meta:
        verbose_name = 'Dostawa końcowa'
        verbose_name_plural = 'Dostawy końcowe'

    def clean(self):
        if self.wood_kind not in self.order.get_wood_kinds():
            raise ValidationError({'wood_kind': 'Prosze wybrać sortyment będący w pozycjach dostawy kwitu wywozowego.'})

        max_amount = self.order.get_final_differences()[self.wood_kind]
        if self.amount > max_amount:
            if max_amount == 0:
                raise ValidationError({'wood_kind': 'Prosze wybrać sortyment nie będący już w pełni dostarczony.'})
            else:
                raise ValidationError({'amount': 'Prosze wybrać mniejszą masę. Tego sortymentu zostało jeszcze {amount} m³.'.format(amount=max_amount)})

        # amount_delta = get_object_or_404(Shipment, pk=self.pk).amount - self.amount
        # if not self.calculate_difference() + amount_delta >= 0:
        #     raise ValidationError({'amount': 'Prosze wprowadzić masę nie powodującą powstania ujemnej różnicy.'})

    def save(self, **kwargs):
        try:
            former_shipment = Final_shipment.objects.get(pk=self.pk)
        except Final_shipment.DoesNotExist:
            former_shipment = None
        amount_delta = Decimal(0)
        if former_shipment:
            amount_delta = former_shipment.amount - self.amount
        if not self.calculate_difference() + amount_delta >= 0:
            return
        return super(Final_shipment, self).save(**kwargs)

    def __str__(self):
        return self.order.__str__() + " - " + self.wood_kind.__str__() + " - " + self.amount.__str__()

    def __unicode__(self):
        return self.order.__unicode__() + " - " + self.wood_kind.__unicode__() + " - " + self.amount.__str__()

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

    def calculate_difference(self):
        for order_item in self.order.order_items.all():
            if self.wood_kind == order_item.wood_kind:
                return order_item.calculate_final_difference()
