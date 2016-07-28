from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.OrderListView.as_view(), name='order_list'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)$', views.OrderListView.as_view(), name='order_list'),
    url(r'^(?P<pk>\d+)/detail$', views.OrderDetailView.as_view(), name='order_detail'),
    url(r'^(?P<pk>\d+)/delete$', views.OrderDeleteView.as_view(), name='order_delete'),
    url(r'^(?P<pk>\d+)/order_item/list$', views.OrderItemListView.as_view(), name='order_item_list'),
    url(r'^(?P<pk>\d+)/order_item/create$', views.OrderItemCreateView.as_view(), name='order_item_create'),
    url(r'^(?P<pk>\d+)/order_item/delete$', views.OrderItemDeleteView.as_view(), name='order_item_delete'),
    url(r'^(?P<pk>\d+)/shipment/list$', views.ShipmentListView.as_view(), name='shipment_list'),
    url(r'^(?P<pk>\d+)/shipment/depot_list$', views.ShipmentForDepotListView.as_view(), name='shipment_for_depot_list'),
    url(r'^(?P<pk>\d+)/shipment/create$', views.ShipmentCreateView.as_view(), name='shipment_create'),
    url(r'^(?P<pk>\d+)/shipment/create_all$', views.AllShipmentCreateView.as_view(), name='shipment_create_all'),
    url(r'^(?P<pk>\d+)/shipment/delete$', views.ShipmentDeleteView.as_view(), name='shipment_delete'),
    url(r'^shipment$', views.AllShipmentListView.as_view(), name='shipment_list_bi'),
    url(r'^(?P<pk>\d+)/shipment$', views.AllShipmentListView.as_view(), name='shipment_list_bi'),
    url(r'^create$', views.OrderCreateView.as_view(), name='order_create'),
    url(r'^price_list$', views.PriceListView.as_view(), name='price_list'),
    url(r'^price_list/create$', views.WoodKindCreateView.as_view(), name='wood_kind_create'),
    url(r'^price_list/delete/(?P<pk>\d+)$', views.WoodKindDeleteView.as_view(), name='wood_kind_delete'),
    url(r'^backup$', views.BackupView.as_view(), name='backup_details'),
    url(r'^(?P<pk>\d+)/price$', views.WoodKindPriceRetrieveView.as_view(), name='wood_kind_price'),
    # final shipments
    url(r'^(?P<pk>\d+)/final_shipment/list$', views.FinalShipmentListView.as_view(), name='final_shipment_list'),
    url(r'^(?P<pk>\d+)/final_shipment/create$', views.FinalShipmentCreateView.as_view(), name='final_shipment_create'),
    url(r'^(?P<pk>\d+)/final_shipment/create_all$', views.AllFinalShipmentCreateView.as_view(), name='final_shipment_create_all'),
    url(r'^(?P<pk>\d+)/final_shipment/delete$', views.FinalShipmentDeleteView.as_view(), name='final_shipment_delete'),
    # reports
    url(r'^reports$', views.ReportListView.as_view(), name='reports'),
    url(r'^reports/drivers$', views.DriverReportView.as_view(), name='driver_report'),
    url(r'^reports/contractors$', views.ContractorReportView.as_view(), name='contractor_report'),
    # contractor shipments
    url(r'^(?P<pk>\d+)/contractor_shipment/list$', views.ContractorShipmentListView.as_view(), name='contractor_shipment_list'),
    url(r'^(?P<pk>\d+)/contractor_shipment/create$', views.ContractorShipmentCreateView.as_view(), name='contractor_shipment_create'),
    url(r'^(?P<pk>\d+)/contractor_shipment/delete$', views.ContractorShipmentDeleteView.as_view(), name='contractor_shipment_delete'),
    # contractors
    url(r'^contractor/(?P<pk>\d+)$', views.ContractorDetailView.as_view(), name='contractor_detail'),
    url(r'^depot_list$', views.DepotListView.as_view(), name='depot_list'),
]
