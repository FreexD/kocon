#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from datatableview import helpers
from datatableview.views import DatatableView, XEditableDatatableView
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import django.views.generic as views

from lumberjack.settings import PLAC_ID
from tartak.forms import OrderItemForm, ShipmentForm, ContractorForm
from tartak.models import Order, Wood_kind, Order_item, Shipment, Contractor


class OrderListView(DatatableView):
    model = Order
    template_name = 'tartak/order_list.html'
    datatable_options = {
        'columns': [
            ('WZ', 'code'),
            ('Kierowca', 'driver'),
            ('Nadleśnictwo', 'forest_district'),
            ('Data', 'date'),
            ('Cena [zł]', 'get_price_display'),
            ('Akcja', 'get_action_buttons'),
        ],
        'search_fields': [
            'code',
            'driver__first_name',
            'driver__last_name',
            'forest_district__name',
            'date'
        ]
    }

    def get_queryset(self):
        queryset = Order.objects.all()

        if 'year' in self.kwargs and 'month' in self.kwargs:
            year = self.kwargs.get('year')
            month = self.kwargs.get('month')
            queryset = queryset.filter(date__year=year, date__month=month)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(OrderListView, self).get_context_data(**kwargs)
        if 'year' in self.kwargs and 'month' in self.kwargs:
            context['by_month'] = True
            context['year'] = self.kwargs.get('year')
            context['month'] = self.kwargs.get('month')
            context['report_date'] = context['year'] + '/' + context['month']
        return context

class OrderDetailView(views.DeleteView):
    model = Order
    context_object_name = 'order'
    template_name = 'tartak/order_detail.html'


class OrderCreateView(views.CreateView):
    model = Order
    fields = ['code', 'driver', 'forest_district', 'date', 'pieces']
    template_name = 'tartak/order_create.html'


class OrderDeleteView(views.DeleteView):
    model=Order
    context_object_name = 'order'
    template_name = 'tartak/order_confirm_delete.html'
    success_url = '/'


class PriceListView(XEditableDatatableView):
    model = Wood_kind
    datatable_options = {
        'structure_template': 'datatableview/editable_structure.html',
        'columns': [
            ('Nadleśnictwo', 'forest_district'),
            ('Sortyment', 'code'),
            ('Cena [zł]', 'detail_price', helpers.make_xeditable),
            ('Akcja', 'get_action_buttons')
        ],
        'search_fields': [
            'forest_district__name',
            'code'
        ]
    }


class WoodKindCreateView(views.CreateView):
    model = Wood_kind
    fields = ['code', 'forest_district', 'detail_price']
    template_name = 'tartak/wood_kind_create.html'


class WoodKindDeleteView(views.DeleteView):
    model=Wood_kind
    context_object_name = 'wood_kind'
    template_name = 'tartak/wood_kind_confirm_delete.html'
    success_url = '/price_list/'


class OrderItemListView(XEditableDatatableView):
    model = Order_item
    datatable_options = {
        'structure_template': 'datatableview/editable_structure.html',
        'columns': [
            ('Sortyment', 'wood_kind'),
            ('Masa [m³]', 'amount', helpers.make_xeditable),
            ('Cena [zł]', 'get_price_display'),
            ('Różnica [zł]', 'get_difference_display_for_datatables'),
            ('Akcja', 'get_action_buttons')
        ],
        'search_fields': [
            'wood_kind__code',
            'amount',
        ]
    }

    def get_queryset(self):
        return Order_item.objects.filter(order__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(OrderItemListView, self).get_context_data(**kwargs)
        context['order'] = get_object_or_404(Order, pk=self.kwargs.get('pk'))
        return context


class OrderItemCreateView(views.CreateView):
    model=Order_item
    template_name = 'tartak/order_item_create.html'
    form_class = OrderItemForm

    def get_context_data(self, **kwargs):
        context = super(OrderItemCreateView, self).get_context_data(**kwargs)
        context['order'] = get_object_or_404(Order, pk=self.kwargs.get('pk'))
        return context

    def get_initial(self):
        initial = super(OrderItemCreateView, self).get_initial()
        initial['order'] = get_object_or_404(Order, pk=self.kwargs.get('pk'))
        return initial

    def form_valid(self, form):
        form.instance.order = get_object_or_404(Order, pk=self.kwargs.get('pk'))
        try:
            return super(OrderItemCreateView, self).form_valid(form)
        except IntegrityError as e:
            form.add_error('wood_kind', "Item with this code already exists in this order.")
            return super(OrderItemCreateView, self).form_invalid(form)


class WoodKindPriceRetrieveView(views.DetailView):
    model = Wood_kind
    context_object_name = 'wood_kind'
    template_name = 'tartak/wood_kind_price.html'


class OrderItemDeleteView(views.DeleteView):
    model = Order_item
    context_object_name = 'order_item'
    template_name = 'tartak/order_item_confirm_delete.html'

    def get_success_url(self):
        return '/' + self.object.order.pk.__str__() + '/order_item/list'


class ShipmentListView(XEditableDatatableView):
    model = Shipment
    datatable_options = {
        'structure_template': 'datatableview/editable_structure.html',
        'columns': [
            ('Kontrahent', 'contractor'),
            ('Sortyment', 'wood_kind'),
            ('Masa [m³]', 'amount', helpers.make_xeditable),
            ('Akcja', 'get_action_buttons')
        ],
        'search_fields': [
            'contractor__name',
            'wood_kind__code',
            'amount',
        ]
    }

    def get_queryset(self):
        return Shipment.objects.filter(order__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(ShipmentListView, self).get_context_data(**kwargs)
        context['order'] = get_object_or_404(Order, pk=self.kwargs.get('pk'))
        return context


class ShipmentCreateView(views.CreateView):
    model=Shipment
    template_name = 'tartak/shipment_create.html'
    form_class = ShipmentForm

    def get_context_data(self, **kwargs):
        context = super(ShipmentCreateView, self).get_context_data(**kwargs)
        context['order'] = get_object_or_404(Order, pk=self.kwargs.get('pk'))
        return context

    def get_initial(self):
        initial = super(ShipmentCreateView, self).get_initial()
        initial['order'] = get_object_or_404(Order, pk=self.kwargs.get('pk'))
        return initial

    def form_valid(self, form):
        form.instance.order = get_object_or_404(Order, pk=self.kwargs.get('pk'))
        return super(ShipmentCreateView, self).form_valid(form)


class ShipmentDeleteView(views.DeleteView):
    model = Shipment
    context_object_name = 'shipment'
    template_name = 'tartak/shipment_confirm_delete.html'

    def get_success_url(self):
        return '/' + self.object.order.pk.__str__() + '/shipment/list'


class AllShipmentListView(DatatableView):
    model = Shipment
    template_name = 'tartak/shipment_contractor_list.html'
    datatable_options = {
        'columns': [
            ('Kontrahent', 'contractor'),
            ('WZ', 'order'),
            ('Sortyment', 'wood_kind'),
            ('Masa [m³]', 'amount'),
        ],
        'search_fields': [
            'contractor__name',
            'order__code',
            'wood_kind__code',
            'amount',
        ]
    }

    def get_queryset(self):
        queryset = Shipment.objects.all()
        if 'pk' in self.kwargs:
            queryset = queryset.filter(contractor__pk=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AllShipmentListView, self).get_context_data(**kwargs)
        context['contractor_form'] = ContractorForm()
        if 'pk' in self.kwargs:
            context['by_contractor'] = True
            context['contractor'] = get_object_or_404(Contractor, pk=self.kwargs.get('pk'))
        return context


class ContractorDetailView(views.DetailView):
    model = Contractor
    context_object_name = 'contractor'
    template_name = 'tartak/contractor_detail.html'


class ReportView(views.ListView):
    model = Order
    template_name = 'tartak/report_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return Order.objects.filter(date__year=year, date__month=month)

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        orders = context['orders']
        context['report_date'] = self.kwargs.get('year') + '/' + self.kwargs.get('month')

        not_fully_shipped = []
        for order in orders:
            for order_item in order.order_items.all():
                if not order_item.is_fully_shipped():
                    not_fully_shipped.append(order_item)
        context['not_fully_shipped'] = not_fully_shipped

        plac_shipments = []
        for order in orders:
            for shipment in order.shipments.all():
                if shipment.contractor.id == PLAC_ID:
                    plac_shipments.append(shipment)
        context['plac_shipments'] = plac_shipments

        plac_aggregate_shipments = {}
        for shipment in plac_shipments:
            if shipment.wood_kind in plac_aggregate_shipments.keys():
                plac_aggregate_shipments[shipment.wood_kind] += shipment.amount
            else:
                plac_aggregate_shipments[shipment.wood_kind] = shipment.amount

        for wood_kind in plac_aggregate_shipments.keys():
            plac_aggregate_shipments[wood_kind] = round(plac_aggregate_shipments[wood_kind], 2).__str__()

        context['plac_aggregate_shipments'] = plac_aggregate_shipments

        return context


class BackupView(views.TemplateView):
    template_name = 'tartak/backup_instructions.html'

# BACKUP AND RESTORE DATA
#
# export: pg_dump <dbname> -t <tablename> -f out.sql
#
# import: psql <dbname> -f out.sql