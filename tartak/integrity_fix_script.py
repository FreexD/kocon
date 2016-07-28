from tartak.models import Order, Contractor_shipment

# works best for fully shipped depots
for order in Order.objects.all():
    if order.is_both():
        print('Found {}.'.format(order))
        # convert final shipments to contractor shipments, delete final_shipments
        depot = order.order_items.all()[0].contractor
        for final_shipment in order.final_shipments.all():
            contractor_shipment = Contractor_shipment.objects.create(depot=depot,
                                                                     contractor=final_shipment.contractor,
                                                                     amount=final_shipment.amount,
                                                                     date=final_shipment.date,
                                                                     driver=final_shipment.driver,
                                                                     wood_type=final_shipment.wood_type)
            print('Converting {} to {}.'.format(final_shipment, contractor_shipment))
            final_shipment.delete()
        print('Converted {}.'.format(order))
# check rerun
print('Checking...')
for order in Order.objects.all():
    if order.is_both():
        print('Check failed! Found {}.'.format(order))
        break
print('Check went successfull!')
