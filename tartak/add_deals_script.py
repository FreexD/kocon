#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import date
from decimal import Decimal

from tartak.models import Forest_district, Deal, Deal_item

print('Creating K deals...')

print('Creating K deal for Andrychów...')
district = Forest_district.objects.get(code='AND', name='Andrychów K')
deal = Deal.objects.create(forest_district=district, code='AND/2016', name='Andrychów K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_BRZ', amount=Decimal(200))

print('Creating K deal for Bielsko...')
district = Forest_district.objects.get(code='BIE', name='Bielsko K')
deal = Deal.objects.create(forest_district=district, code='BIE/2016', name='Bielsko K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_BRZ', amount=Decimal(290))
Deal_item.objects.create(deal=deal, code='S_S2A_SW', amount=Decimal(295))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SW', amount=Decimal(975))
Deal_item.objects.create(deal=deal, code='W_WBCK_23_SW', amount=Decimal(601))
Deal_item.objects.create(deal=deal, code='W_WCDK_12_SW', amount=Decimal(2428))

print('Creating K deal for Brynek...')
district = Forest_district.objects.get(code='BRY', name='Brynek K')
deal = Deal.objects.create(forest_district=district, code='BRY/2016', name='Brynek K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(183))
Deal_item.objects.create(deal=deal, code='S_S2B_GD_SO', amount=Decimal(278))

print('Creating K deal for Jeleśnia...')
district = Forest_district.objects.get(code='JEL', name='Jeleśnia K')
deal = Deal.objects.create(forest_district=district, code='JEL/2016', name='Jeleśnia K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_BRZ', amount=Decimal(40))
Deal_item.objects.create(deal=deal, code='S_S2A_SW', amount=Decimal(461))
Deal_item.objects.create(deal=deal, code='S_S2A_ENER_IGLASTE', amount=Decimal(107))
Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(492))
Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(700))
Deal_item.objects.create(deal=deal, code='W_STANDARD_JD', amount=Decimal(1494))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SO', amount=Decimal(358))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SW', amount=Decimal(1267))

print('Creating K deal for Katowice...')
district = Forest_district.objects.get(code='KAT', name='Katowice K')
deal = Deal.objects.create(forest_district=district, code='KAT/2016', name='Katowice K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_BRZ', amount=Decimal(294))
Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(140))
Deal_item.objects.create(deal=deal, code='S_S2B_GD_SO', amount=Decimal(170))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SO', amount=Decimal(638))

print('Creating K deal for Kobiór...')
district = Forest_district.objects.get(code='KOB', name='Kobiór K')
deal = Deal.objects.create(forest_district=district, code='KOB/2016', name='Kobiór K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_ENER_LISCIASTE', amount=Decimal(1666))
Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_MD', amount=Decimal(47))

print('Creating K deal for Koszęcin...')
district = Forest_district.objects.get(code='KOS', name='Koszęcin K')
deal = Deal.objects.create(forest_district=district, code='KOS/2016', name='Koszęcin K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(312))

print('Creating K deal for Opole...')
district = Forest_district.objects.get(code='OPO', name='Opole K')
deal = Deal.objects.create(forest_district=district, code='OPO/2016', name='Opole K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(119))

print('Creating K deal for Olesno...')
district = Forest_district.objects.get(code='OLE', name='Olesno K')
deal = Deal.objects.create(forest_district=district, code='OLE/2016', name='Olesno K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_SW', amount=Decimal(23))

print('Creating K deal for Oława...')
district = Forest_district.objects.get(code='OŁA', name='Oława K')
deal = Deal.objects.create(forest_district=district, code='OŁA/2016', name='Oława K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='W_WD_SO', amount=Decimal(304))

print('Creating K deal for Prudnik...')
district = Forest_district.objects.get(code='PRU', name='Prudnik K')
deal = Deal.objects.create(forest_district=district, code='PRU/2016', name='Prudnik K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_ENER_LISCIASTE', amount=Decimal(1306))
Deal_item.objects.create(deal=deal, code='S_S2A_SW', amount=Decimal(1530))
Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(4261))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SW', amount=Decimal(1667))

print('Creating K deal for Prószków...')
district = Forest_district.objects.get(code='PRÓ', name='Prószków K')
deal = Deal.objects.create(forest_district=district, code='PRÓ/2016', name='Prószków K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_ENER_LISCIASTE', amount=Decimal(762))
Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(516))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SO', amount=Decimal(1744))

print('Creating K deal for Rudy Raciborskie...')
district = Forest_district.objects.get(code='RAC', name='Rudy Raciborskie K')
deal = Deal.objects.create(forest_district=district, code='RAC/2016', name='Rudy Raciborskie K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='W_STANDARD_SO', amount=Decimal(350))

print('Creating K deal for Rudziniec...')
district = Forest_district.objects.get(code='RUD', name='Rudziniec K')
deal = Deal.objects.create(forest_district=district, code='RUD/2016', name='Rudziniec K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_BRZ', amount=Decimal(362))
Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(67))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SO', amount=Decimal(1231))

print('Creating K deal for Siewierz...')
district = Forest_district.objects.get(code='SIE', name='Siewierz K')
deal = Deal.objects.create(forest_district=district, code='SIE/2016', name='Siewierz K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_SW', amount=Decimal(51))
Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_BRZ', amount=Decimal(334))
Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(106))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SO', amount=Decimal(250))

print('Creating K deal for Świerklaniec...')
district = Forest_district.objects.get(code='ŚWI', name='Świerklaniec K')
deal = Deal.objects.create(forest_district=district, code='ŚWI/2016', name='Świerklaniec K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(164))
Deal_item.objects.create(deal=deal, code='S_S2B_GD_SO', amount=Decimal(225))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SO', amount=Decimal(832))

print('Creating K deal for Tułowice...')
district = Forest_district.objects.get(code='TUŁ', name='Tułowice K')
deal = Deal.objects.create(forest_district=district, code='TUŁ/2016', name='Tułowice K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_BRZ', amount=Decimal(84))
Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(29))

print('Creating K deal for Ujsoły...')
district = Forest_district.objects.get(code='UJS', name='Ujsoły K')
deal = Deal.objects.create(forest_district=district, code='UJS/2016', name='Ujsoły K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_BK', amount=Decimal(29))
Deal_item.objects.create(deal=deal, code='S_S2A_SW', amount=Decimal(493))
Deal_item.objects.create(deal=deal, code='W_STANDARD_BK', amount=Decimal(47))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SW', amount=Decimal(4088))

print('Creating K deal for Ustroń...')
district = Forest_district.objects.get(code='UST', name='Ustroń K')
deal = Deal.objects.create(forest_district=district, code='UST/2016', name='Ustroń K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_SO', amount=Decimal(209))
Deal_item.objects.create(deal=deal, code='S_S2A_SW', amount=Decimal(143))
Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(1323))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SO', amount=Decimal(1461))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SW', amount=Decimal(5112))
Deal_item.objects.create(deal=deal, code='W_WD_SW', amount=Decimal(299))

print('Creating K deal for Węgierska Górka...')
district = Forest_district.objects.get(code='WĘG', name='Węgierska Górka K')
deal = Deal.objects.create(forest_district=district, code='WĘG/2016', name='Węgierska Górka K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_SW', amount=Decimal(511))

print('Creating K deal for Wisła...')
district = Forest_district.objects.get(code='WIS', name='Wisła K')
deal = Deal.objects.create(forest_district=district, code='WIS/2016', name='Wisła K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_SW', amount=Decimal(397))
Deal_item.objects.create(deal=deal, code='W_STANDARD_JD', amount=Decimal(150))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SW', amount=Decimal(19828))

print('Creating K deal for Zawadzkie...')
district = Forest_district.objects.get(code='ZAW', name='Zawadzkie K')
deal = Deal.objects.create(forest_district=district, code='ZAW/2016', name='Zawadzkie K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2B_GD_SO', amount=Decimal(300))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SO', amount=Decimal(399))

print('Creating K deal for Bardo Śląskie...')
district = Forest_district.objects.get(code='BAR', name='Bardo Śląskie K')
deal = Deal.objects.create(forest_district=district, code='BAR/2016', name='Bardo Śląskie K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(42))

print('Creating K deal for Bystrzyca Kłodzka...')
district = Forest_district.objects.get(code='BYS', name='Bystrzyca Kłodzka K')
deal = Deal.objects.create(forest_district=district, code='BYS/2016', name='Bystrzyca Kłodzka K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(4588))

print('Creating K deal for Jawor...')
district = Forest_district.objects.get(code='JAW', name='Jawor K')
deal = Deal.objects.create(forest_district=district, code='JAW/2016', name='Jawor K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(697))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SW', amount=Decimal(400))

print('Creating K deal for Jugów...')
district = Forest_district.objects.get(code='JUG', name='Jugów K')
deal = Deal.objects.create(forest_district=district, code='JUG/2016', name='Jugów K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(956))

print('Creating K deal for Kamienna Góra...')
district = Forest_district.objects.get(code='KAM', name='Kamienna Góra K')
deal = Deal.objects.create(forest_district=district, code='KAM/2016', name='Kamienna Góra K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(3807))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SW', amount=Decimal(1343))

print('Creating K deal for Lądek Zdrój...')
district = Forest_district.objects.get(code='LĄD', name='Lądek Zdrój K')
deal = Deal.objects.create(forest_district=district, code='LĄD/2016', name='Lądek Zdrój K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(4789))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SW', amount=Decimal(500))

print('Creating K deal for Lwówek Śląski...')
district = Forest_district.objects.get(code='LWÓ', name='Lwówek Śląski K')
deal = Deal.objects.create(forest_district=district, code='LWÓ/2016', name='Lwówek Śląski K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(1865))

print('Creating K deal for Międzylesie...')
district = Forest_district.objects.get(code='MIĘ', name='Międzylesie K')
deal = Deal.objects.create(forest_district=district, code='MIĘ/2016', name='Międzylesie K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_ENER_LISCIASTE', amount=Decimal(50))
Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(348))
Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(1270))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SW', amount=Decimal(799))

print('Creating K deal for Szklarska Poręba...')
district = Forest_district.objects.get(code='SZK', name='Szklarska Poręba K')
deal = Deal.objects.create(forest_district=district, code='SZK/2016', name='Szklarska Poręba K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(40))

print('Creating K deal for Śnieżka...')
district = Forest_district.objects.get(code='ŚNI', name='Śnieżka K')
deal = Deal.objects.create(forest_district=district, code='ŚNI/2016', name='Śnieżka K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_BC_SW', amount=Decimal(300))
Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(835))

print('Creating K deal for Świdnica...')
district = Forest_district.objects.get(code='ŚWD', name='Świdnica K')
deal = Deal.objects.create(forest_district=district, code='ŚWD/2016', name='Świdnica K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='W_STANDARD_SW', amount=Decimal(1400))

print('Creating K deal for Zdroje...')
district = Forest_district.objects.get(code='ZDR', name='Zdroje K')
deal = Deal.objects.create(forest_district=district, code='ZDR/2016', name='Zdroje K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(4550))
Deal_item.objects.create(deal=deal, code='W_STANDARD_SW', amount=Decimal(400))

print('Creating K deal for Złotoryja...')
district = Forest_district.objects.get(code='ZŁO', name='Złotoryja K')
deal = Deal.objects.create(forest_district=district, code='ZŁO/2016', name='Złotoryja K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(519))

print('Creating K deal for Dojlidy...')
district = Forest_district.objects.get(code='DOJ', name='Dojlidy K')
deal = Deal.objects.create(forest_district=district, code='DOJ/2016', name='Dojlidy K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(460))

print('Creating K deal for Drygały...')
district = Forest_district.objects.get(code='DRY', name='Drygały K')
deal = Deal.objects.create(forest_district=district, code='DRY/2016', name='Drygały K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(400))

print('Creating K deal for Górowo Iławeckie...')
district = Forest_district.objects.get(code='GÓR', name='Górowo Iławieckie K')
deal = Deal.objects.create(forest_district=district, code='GÓR/2016', name='Górowo Iławeckie K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(497))

print('Creating K deal for Olsztyn...')
district = Forest_district.objects.get(code='OLS', name='Olsztyn K')
deal = Deal.objects.create(forest_district=district, code='OLS/2016', name='Olsztyn K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(2000))

print('Creating K deal for Orneta...')
district = Forest_district.objects.get(code='ORN', name='Orneta K')
deal = Deal.objects.create(forest_district=district, code='ORN/2016', name='Orneta K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(773))

print('Creating K deal for Płaska...')
district = Forest_district.objects.get(code='PŁA', name='Płaska K')
deal = Deal.objects.create(forest_district=district, code='PŁA/2016', name='Płaska K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='S_S2A_OPAL_SW', amount=Decimal(400))
Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(874))

print('Creating K deal for Suwałki...')
district = Forest_district.objects.get(code='SUW', name='Suwałki K')
deal = Deal.objects.create(forest_district=district, code='SUW/2016', name='Suwałki K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(1623))

print('Creating K deal for Nowe Ramuki...')
district = Forest_district.objects.get(code='NOW', name='Nowe Ramuki K')
deal = Deal.objects.create(forest_district=district, code='NOW/2016', name='Nowe Ramuki K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(500))

print('Creating K deal for Żednia...')
district = Forest_district.objects.get(code='ŻED', name='Żednia K')
deal = Deal.objects.create(forest_district=district, code='ŻED/2016', name='Żednia K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(651))

print('Creating K deal for Wichrowo...')
district = Forest_district.objects.get(code='WIC', name='Wichrowo K')
deal = Deal.objects.create(forest_district=district, code='WIC/2016', name='Wichrowo K 2016', date_from=date(year=2016, month=1, day=1), date_to=date(year=2016, month=12, day=31))

Deal_item.objects.create(deal=deal, code='WK_STANDARD_SW', amount=Decimal(1500))