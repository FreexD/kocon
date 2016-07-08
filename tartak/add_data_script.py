#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import Decimal

from lumberjack import settings
from tartak.models import Driver, Contractor, Forest_district, Wood_kind

print('Creating drivers...')

Driver.objects.create(code='BEDNARZ', last_name='Bednarz', first_name='Tadeusz')
Driver.objects.create(code='BIERNAT', last_name='Biernat', first_name='Czesław')
Driver.objects.create(code='BRYS', last_name='Brys', first_name='Krzysztof')
Driver.objects.create(code='BYRSKI', last_name='Byrski', first_name='Jan')
Driver.objects.create(code='DUDYS_M', last_name='Dudys', first_name='Mariusz')

Driver.objects.create(code='DUDYS_SZ', last_name='Dudys', first_name='Szymon')
Driver.objects.create(code='DZIERGAS', last_name='Dziergas', first_name='Tomasz')
Driver.objects.create(code='FRYCZKOWSKI', last_name='Fryczkowski', first_name='Sławomir')
Driver.objects.create(code='HABICIAK', last_name='Habiciak', first_name='Tomasz')
Driver.objects.create(code='HANKUS', last_name='Hankus', first_name='Sławomir')

Driver.objects.create(code='HULBÓJ', last_name='Hulbój', first_name='Adam')
Driver.objects.create(code='JANOTA', last_name='Janota', first_name='Leszek')
Driver.objects.create(code='JASZCZUROWSKI', last_name='Jaszczurowski', first_name='Andrzej')
Driver.objects.create(code='KLIMCZAK', last_name='Klimczak', first_name='Łukasz')
Driver.objects.create(code='KLIŚ_P', last_name='Kliś', first_name='Piotr')

Driver.objects.create(code='KLIŚ_S', last_name='Kliś', first_name='Stanisław')
Driver.objects.create(code='KOCOŃ', last_name='Kocoń', first_name='Jarosław')
Driver.objects.create(code='KOLARCZYK', last_name='Kolarczyk', first_name='Jerzy')
Driver.objects.create(code='KOTRYS', last_name='Kotrys', first_name='Andrzej')
Driver.objects.create(code='KUŚNIERZ', last_name='Kuśnierz', first_name='Robert')

Driver.objects.create(code='LEŚNIAK', last_name='Leśniak', first_name='Tomasz')
Driver.objects.create(code='LINK_D', last_name='Link', first_name='Dariusz')
Driver.objects.create(code='LINK_M', last_name='Link', first_name='Maciej')
Driver.objects.create(code='LINK_R', last_name='Link', first_name='Roman')
Driver.objects.create(code='MICHAŁEK', last_name='Michałek', first_name='Janusz')

Driver.objects.create(code='MORZY', last_name='Morzy', first_name='Krzysztof')
Driver.objects.create(code='PACIOREK', last_name='Paciorek', first_name='Czesław')
Driver.objects.create(code='PIĘTKA', last_name='Piętka', first_name='Andrzej')
Driver.objects.create(code='PIWOWARCZYK', last_name='Piwowarczyk', first_name='Janusz')
Driver.objects.create(code='PŁOSKONKA', last_name='Płoskonka', first_name='Mateusz')

Driver.objects.create(code='PYDYCH', last_name='Pydych', first_name='Wiesław')
Driver.objects.create(code='PYTEL', last_name='Pytel', first_name='Stanisław')
Driver.objects.create(code='SUCHOŃSKI', last_name='Suchoński', first_name='Mariusz')
Driver.objects.create(code='SZCZOTKA', last_name='Szczotka', first_name='Konrad')
Driver.objects.create(code='ŚLEZIAK', last_name='Śleziak', first_name='Andrzej')

Driver.objects.create(code='TANISTRA', last_name='Tanistra', first_name='Grzegorz')
Driver.objects.create(code='TOMALA', last_name='Tomala', first_name='Witold')
Driver.objects.create(code='WEJCHENIG', last_name='Wejchenig', first_name='Arkadiusz')
Driver.objects.create(code='WESOŁOWSKI', last_name='Wesołowski', first_name='Jarosław')
Driver.objects.create(code='WŁOCH', last_name='Włoch', first_name='Stanisław')

Driver.objects.create(code='WOREK', last_name='Worek', first_name='Wiesław')
Driver.objects.create(code='WYDRA', last_name='Wydra', first_name='Kazimierz')
Driver.objects.create(code='ZAWADA', last_name='Zawada', first_name='Mateusz')
Driver.objects.create(code='ZIOBRO', last_name='Ziobro', first_name='Aleksander')

print('Creating K price lists...')

# Andrychów
print('Creating K price lists for Andrychów...')
district = Forest_district.objects.create(code='AND', name='Andrychów K')
Wood_kind.objects.create(forest_district=district, code='AND/S_S2A_BRZ/S2A', detail_price=Decimal(145.78))

# Bielsko
print('Creating K price lists for Bielsko...')
district = Forest_district.objects.create(code='BIE', name='Bielsko K')
Wood_kind.objects.create(forest_district=district, code='BIE/S_S2A_BRZ/S2A', detail_price=Decimal(132.97))

Wood_kind.objects.create(forest_district=district, code='BIE/S_S2A_SW/S2A', detail_price=Decimal(170.92))

Wood_kind.objects.create(forest_district=district, code='BIE/W_STANDARD_SW/WA0_2', detail_price=Decimal(382.92))
Wood_kind.objects.create(forest_district=district, code='BIE/W_STANDARD_SW/WA0_3', detail_price=Decimal(463.20))
Wood_kind.objects.create(forest_district=district, code='BIE/W_STANDARD_SW/WB0_1', detail_price=Decimal(296.73))
Wood_kind.objects.create(forest_district=district, code='BIE/W_STANDARD_SW/WB0_2', detail_price=Decimal(332.93))
Wood_kind.objects.create(forest_district=district, code='BIE/W_STANDARD_SW/WB0_3', detail_price=Decimal(364.20))
Wood_kind.objects.create(forest_district=district, code='BIE/W_STANDARD_SW/WC0_1', detail_price=Decimal(246.25))
Wood_kind.objects.create(forest_district=district, code='BIE/W_STANDARD_SW/WC0_2', detail_price=Decimal(286.63))
Wood_kind.objects.create(forest_district=district, code='BIE/W_STANDARD_SW/WC0_3', detail_price=Decimal(323.08))
Wood_kind.objects.create(forest_district=district, code='BIE/W_STANDARD_SW/WD_1', detail_price=Decimal(192.32))
Wood_kind.objects.create(forest_district=district, code='BIE/W_STANDARD_SW/WD_2', detail_price=Decimal(212.76))
Wood_kind.objects.create(forest_district=district, code='BIE/W_STANDARD_SW/WD_3', detail_price=Decimal(245.75))

Wood_kind.objects.create(forest_district=district, code='BIE/W_WBCK_23_SW/WBK_2', detail_price=Decimal(354.81))
Wood_kind.objects.create(forest_district=district, code='BIE/W_WBCK_23_SW/WBK_3', detail_price=Decimal(388.10))
Wood_kind.objects.create(forest_district=district, code='BIE/W_WBCK_23_SW/WCK_2', detail_price=Decimal(305.35))
Wood_kind.objects.create(forest_district=district, code='BIE/W_WBCK_23_SW/WCK_3', detail_price=Decimal(344.13))

Wood_kind.objects.create(forest_district=district, code='BIE/W_WCDK_12_SW/WCK_1', detail_price=Decimal(256.44))
Wood_kind.objects.create(forest_district=district, code='BIE/W_WCDK_12_SW/WCK_2', detail_price=Decimal(298.50))
Wood_kind.objects.create(forest_district=district, code='BIE/W_WCDK_12_SW/WDK_1', detail_price=Decimal(200.29))
Wood_kind.objects.create(forest_district=district, code='BIE/W_WCDK_12_SW/WDK_2', detail_price=Decimal(221.57))

# Brynek
print('Creating K price lists for Brynek...')
district = Forest_district.objects.create(code='BRY', name='Brynek K')
Wood_kind.objects.create(forest_district=district, code='BRY/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(153.66))

Wood_kind.objects.create(forest_district=district, code='BRY/S_S2B_GD_SO/S2B_D', detail_price=Decimal(178.28))

# Jeleśnia
print('Creating K price lists for Jeleśnia...')
district = Forest_district.objects.create(code='JEL', name='Jeleśnia K')
Wood_kind.objects.create(forest_district=district, code='JEL/S_S2A_BRZ/S2A', detail_price=Decimal(145.78))

Wood_kind.objects.create(forest_district=district, code='JEL/S_S2A_SW/S2A', detail_price=Decimal(191.09))

Wood_kind.objects.create(forest_district=district, code='JEL/S_S2A_ENER_IGLASTE/S2AC', detail_price=Decimal(131.00))

Wood_kind.objects.create(forest_district=district, code='JEL/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(153.66))

Wood_kind.objects.create(forest_district=district, code='JEL/WK_STANDARD_SW/WAK_2', detail_price=Decimal(423.40))
Wood_kind.objects.create(forest_district=district, code='JEL/WK_STANDARD_SW/WAK_3', detail_price=Decimal(512.16))
Wood_kind.objects.create(forest_district=district, code='JEL/WK_STANDARD_SW/WBK_2', detail_price=Decimal(368.12))
Wood_kind.objects.create(forest_district=district, code='JEL/WK_STANDARD_SW/WBK_3', detail_price=Decimal(402.70))
Wood_kind.objects.create(forest_district=district, code='JEL/WK_STANDARD_SW/WCK_1', detail_price=Decimal(272.28))
Wood_kind.objects.create(forest_district=district, code='JEL/WK_STANDARD_SW/WCK_2', detail_price=Decimal(316.93))
Wood_kind.objects.create(forest_district=district, code='JEL/WK_STANDARD_SW/WCK_3', detail_price=Decimal(357.23))
Wood_kind.objects.create(forest_district=district, code='JEL/WK_STANDARD_SW/WDK_1', detail_price=Decimal(212.65))
Wood_kind.objects.create(forest_district=district, code='JEL/WK_STANDARD_SW/WDK_2', detail_price=Decimal(235.24))
Wood_kind.objects.create(forest_district=district, code='JEL/WK_STANDARD_SW/WDK_3', detail_price=Decimal(271.74))

Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_JD/WA0_2', detail_price=Decimal(421.20))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_JD/WA0_3', detail_price=Decimal(519.84))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_JD/WB0_1', detail_price=Decimal(312.48))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_JD/WB0_2', detail_price=Decimal(341.28))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_JD/WB0_3', detail_price=Decimal(393.37))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_JD/WC0_1', detail_price=Decimal(240.00))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_JD/WC0_2', detail_price=Decimal(283.92))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_JD/WC0_3', detail_price=Decimal(309.36))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_JD/WD_1', detail_price=Decimal(170.64))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_JD/WD_2', detail_price=Decimal(182.88))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_JD/WD_3', detail_price=Decimal(192.96))

Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SO/WA0_2', detail_price=Decimal(349.26))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SO/WA0_3', detail_price=Decimal(427.70))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SO/WB0_1', detail_price=Decimal(235.11))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SO/WB0_2', detail_price=Decimal(289.41))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SO/WB0_3', detail_price=Decimal(330.44))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SO/WC0_1', detail_price=Decimal(213.74))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SO/WC0_2', detail_price=Decimal(249.86))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SO/WC0_3', detail_price=Decimal(284.70))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SO/WD_1', detail_price=Decimal(163.52))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SO/WD_2', detail_price=Decimal(177.83))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SO/WD_3', detail_price=Decimal(193.01))

Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SW/WA0_2', detail_price=Decimal(429.46))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SW/WA0_3', detail_price=Decimal(519.49))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SW/WB0_1', detail_price=Decimal(332.80))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SW/WB0_2', detail_price=Decimal(373.39))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SW/WB0_3', detail_price=Decimal(408.47))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SW/WC0_1', detail_price=Decimal(276.18))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SW/WC0_2', detail_price=Decimal(321.47))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SW/WC0_3', detail_price=Decimal(362.35))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SW/WD_1', detail_price=Decimal(215.69))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SW/WD_2', detail_price=Decimal(238.61))
Wood_kind.objects.create(forest_district=district, code='JEL/W_STANDARD_SW/WD_3', detail_price=Decimal(275.63))

# Katowice
print('Creating K price lists for Katowice...')
district = Forest_district.objects.create(code='KAT', name='Katowice K')
Wood_kind.objects.create(forest_district=district, code='KAT/S_S2A_OPAL_BRZ/S2AP', detail_price=Decimal(131.00))

Wood_kind.objects.create(forest_district=district, code='KAT/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(153.66))

Wood_kind.objects.create(forest_district=district, code='KAT/S_S2B_GD_SO/S2B_D', detail_price=Decimal(181.24))

Wood_kind.objects.create(forest_district=district, code='KAT/W_STANDARD_SO/WA0_2', detail_price=Decimal(321.89))
Wood_kind.objects.create(forest_district=district, code='KAT/W_STANDARD_SO/WA0_3', detail_price=Decimal(394.19))
Wood_kind.objects.create(forest_district=district, code='KAT/W_STANDARD_SO/WB0_1', detail_price=Decimal(216.70))
Wood_kind.objects.create(forest_district=district, code='KAT/W_STANDARD_SO/WB0_2', detail_price=Decimal(266.73))
Wood_kind.objects.create(forest_district=district, code='KAT/W_STANDARD_SO/WB0_3', detail_price=Decimal(304.56))
Wood_kind.objects.create(forest_district=district, code='KAT/W_STANDARD_SO/WC0_1', detail_price=Decimal(197.00))
Wood_kind.objects.create(forest_district=district, code='KAT/W_STANDARD_SO/WC0_2', detail_price=Decimal(230.29))
Wood_kind.objects.create(forest_district=district, code='KAT/W_STANDARD_SO/WC0_3', detail_price=Decimal(262.40))
Wood_kind.objects.create(forest_district=district, code='KAT/W_STANDARD_SO/WD_1', detail_price=Decimal(150.70))
Wood_kind.objects.create(forest_district=district, code='KAT/W_STANDARD_SO/WD_2', detail_price=Decimal(163.90))
Wood_kind.objects.create(forest_district=district, code='KAT/W_STANDARD_SO/WD_3', detail_price=Decimal(177.89))

# Kobiór
print('Creating K price lists for Kobiór...')
district = Forest_district.objects.create(code='KOB', name='Kobiór K')
Wood_kind.objects.create(forest_district=district, code='KOB/S_S2A_ENER_LISCIASTE/S2AC', detail_price=Decimal(140.10))

Wood_kind.objects.create(forest_district=district, code='KOB/S_S2A_OPAL_MD/S2AP', detail_price=Decimal(128.05))

# Koszęcin
print('Creating K price lists for Koszęcin...')
district = Forest_district.objects.create(code='KOS', name='Koszęcin K')
Wood_kind.objects.create(forest_district=district, code='KOS/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(153.66))

# Opole
print('Creating K price lists for Opole...')
district = Forest_district.objects.create(code='OPO', name='Opole K')
Wood_kind.objects.create(forest_district=district, code='OPO/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(153.66))

# Olesno
print('Creating K price lists for Olesno...')
district = Forest_district.objects.create(code='OLE', name='Olesno K')
Wood_kind.objects.create(forest_district=district, code='OLE/S_S2A_SW/S2A', detail_price=Decimal(179.27))

# Oława
print('Creating K price lists for Oława...')
district = Forest_district.objects.create(code='OŁA', name='Oława K')
Wood_kind.objects.create(forest_district=district, code='OŁA/W_WD_SO/WD_1', detail_price=Decimal(165.48))
Wood_kind.objects.create(forest_district=district, code='OŁA/W_WD_SO/WD_2', detail_price=Decimal(179.88))
Wood_kind.objects.create(forest_district=district, code='OŁA/W_WD_SO/WD_3', detail_price=Decimal(195.26))

# Prudnik
print('Creating K price lists for Prudnik...')
district = Forest_district.objects.create(code='PRU', name='Prudnik K')
Wood_kind.objects.create(forest_district=district, code='PRU/S_S2A_ENER_LISCIASTE/S2A', detail_price=Decimal(131.00))

Wood_kind.objects.create(forest_district=district, code='PRU/S_S2A_SW/S2A', detail_price=Decimal(144.79))

Wood_kind.objects.create(forest_district=district, code='PRU/WK_STANDARD_SW/WAKP_2', detail_price=Decimal(408.91))
Wood_kind.objects.create(forest_district=district, code='PRU/WK_STANDARD_SW/WAKP_3', detail_price=Decimal(494.63))
Wood_kind.objects.create(forest_district=district, code='PRU/WK_STANDARD_SW/WBKP_2', detail_price=Decimal(355.52))
Wood_kind.objects.create(forest_district=district, code='PRU/WK_STANDARD_SW/WBKP_3', detail_price=Decimal(388.92))
Wood_kind.objects.create(forest_district=district, code='PRU/WK_STANDARD_SW/WCKP_1', detail_price=Decimal(262.96))
Wood_kind.objects.create(forest_district=district, code='PRU/WK_STANDARD_SW/WCKP_2', detail_price=Decimal(306.08))
Wood_kind.objects.create(forest_district=district, code='PRU/WK_STANDARD_SW/WCKP_3', detail_price=Decimal(345.00))
Wood_kind.objects.create(forest_district=district, code='PRU/WK_STANDARD_SW/WDKP_1', detail_price=Decimal(205.37))
Wood_kind.objects.create(forest_district=district, code='PRU/WK_STANDARD_SW/WDKP_2', detail_price=Decimal(227.20))
Wood_kind.objects.create(forest_district=district, code='PRU/WK_STANDARD_SW/WDKP_3', detail_price=Decimal(262.44))

Wood_kind.objects.create(forest_district=district, code='PRU/W_STANDARD_SW/WA0_2', detail_price=Decimal(382.91))
Wood_kind.objects.create(forest_district=district, code='PRU/W_STANDARD_SW/WA0_3', detail_price=Decimal(463.19))
Wood_kind.objects.create(forest_district=district, code='PRU/W_STANDARD_SW/WB0_1', detail_price=Decimal(296.73))
Wood_kind.objects.create(forest_district=district, code='PRU/W_STANDARD_SW/WB0_2', detail_price=Decimal(332.93))
Wood_kind.objects.create(forest_district=district, code='PRU/W_STANDARD_SW/WB0_3', detail_price=Decimal(364.20))
Wood_kind.objects.create(forest_district=district, code='PRU/W_STANDARD_SW/WC0_1', detail_price=Decimal(246.25))
Wood_kind.objects.create(forest_district=district, code='PRU/W_STANDARD_SW/WC0_2', detail_price=Decimal(286.63))
Wood_kind.objects.create(forest_district=district, code='PRU/W_STANDARD_SW/WC0_3', detail_price=Decimal(323.08))
Wood_kind.objects.create(forest_district=district, code='PRU/W_STANDARD_SW/WD_1', detail_price=Decimal(192.32))
Wood_kind.objects.create(forest_district=district, code='PRU/W_STANDARD_SW/WD_2', detail_price=Decimal(212.76))
Wood_kind.objects.create(forest_district=district, code='PRU/W_STANDARD_SW/WD_3', detail_price=Decimal(245.75))

# Prószków
print('Creating K price lists for Prószków...')
district = Forest_district.objects.create(code='PRÓ', name='Prószków K')
Wood_kind.objects.create(forest_district=district, code='PRÓ/S_S2A_ENER_LISCIASTE/S2AC', detail_price=Decimal(131.00))

Wood_kind.objects.create(forest_district=district, code='PRÓ/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(153.66))

Wood_kind.objects.create(forest_district=district, code='PRÓ/W_STANDARD_SO/WA0_2', detail_price=Decimal(329.94))
Wood_kind.objects.create(forest_district=district, code='PRÓ/W_STANDARD_SO/WA0_3', detail_price=Decimal(404.05))
Wood_kind.objects.create(forest_district=district, code='PRÓ/W_STANDARD_SO/WB0_1', detail_price=Decimal(222.11))
Wood_kind.objects.create(forest_district=district, code='PRÓ/W_STANDARD_SO/WB0_2', detail_price=Decimal(273.40))
Wood_kind.objects.create(forest_district=district, code='PRÓ/W_STANDARD_SO/WB0_3', detail_price=Decimal(312.17))
Wood_kind.objects.create(forest_district=district, code='PRÓ/W_STANDARD_SO/WC0_1', detail_price=Decimal(201.92))
Wood_kind.objects.create(forest_district=district, code='PRÓ/W_STANDARD_SO/WC0_2', detail_price=Decimal(236.05))
Wood_kind.objects.create(forest_district=district, code='PRÓ/W_STANDARD_SO/WC0_3', detail_price=Decimal(268.96))
Wood_kind.objects.create(forest_district=district, code='PRÓ/W_STANDARD_SO/WD_1', detail_price=Decimal(154.47))
Wood_kind.objects.create(forest_district=district, code='PRÓ/W_STANDARD_SO/WD_2', detail_price=Decimal(168.00))
Wood_kind.objects.create(forest_district=district, code='PRÓ/W_STANDARD_SO/WD_3', detail_price=Decimal(182.34))

# Rudy Raciborskie
print('Creating K price lists for Rudy Raciborskie...')
district = Forest_district.objects.create(code='RAC', name='Rudy Raciborskie K')

Wood_kind.objects.create(forest_district=district, code='RAC/W_STANDARD_SO/WA0_2', detail_price=Decimal(426.51))
Wood_kind.objects.create(forest_district=district, code='RAC/W_STANDARD_SO/WA0_3', detail_price=Decimal(522.31))
Wood_kind.objects.create(forest_district=district, code='RAC/W_STANDARD_SO/WB0_1', detail_price=Decimal(287.12))
Wood_kind.objects.create(forest_district=district, code='RAC/W_STANDARD_SO/WB0_2', detail_price=Decimal(353.42))
Wood_kind.objects.create(forest_district=district, code='RAC/W_STANDARD_SO/WB0_3', detail_price=Decimal(403.54))
Wood_kind.objects.create(forest_district=district, code='RAC/W_STANDARD_SO/WC0_1', detail_price=Decimal(261.02))
Wood_kind.objects.create(forest_district=district, code='RAC/W_STANDARD_SO/WC0_2', detail_price=Decimal(305.14))
Wood_kind.objects.create(forest_district=district, code='RAC/W_STANDARD_SO/WC0_3', detail_price=Decimal(347.68))
Wood_kind.objects.create(forest_district=district, code='RAC/W_STANDARD_SO/WD_1', detail_price=Decimal(199.68))
Wood_kind.objects.create(forest_district=district, code='RAC/W_STANDARD_SO/WD_2', detail_price=Decimal(217.17))
Wood_kind.objects.create(forest_district=district, code='RAC/W_STANDARD_SO/WD_3', detail_price=Decimal(235.71))

# Ruziniec
print('Creating K price lists for Rudziniec...')
district = Forest_district.objects.create(code='RUD', name='Rudziniec K')
Wood_kind.objects.create(forest_district=district, code='RUD/S_S2A_OPAL_BRZ/S2AP', detail_price=Decimal(131.00))

Wood_kind.objects.create(forest_district=district, code='RUD/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(153.66))

Wood_kind.objects.create(forest_district=district, code='RUD/W_STANDARD_SO/WA0_2', detail_price=Decimal(364.26))
Wood_kind.objects.create(forest_district=district, code='RUD/W_STANDARD_SO/WA0_3', detail_price=Decimal(446.07))
Wood_kind.objects.create(forest_district=district, code='RUD/W_STANDARD_SO/WB0_1', detail_price=Decimal(245.22))
Wood_kind.objects.create(forest_district=district, code='RUD/W_STANDARD_SO/WB0_2', detail_price=Decimal(301.84))
Wood_kind.objects.create(forest_district=district, code='RUD/W_STANDARD_SO/WB0_3', detail_price=Decimal(344.65))
Wood_kind.objects.create(forest_district=district, code='RUD/W_STANDARD_SO/WC0_1', detail_price=Decimal(222.92))
Wood_kind.objects.create(forest_district=district, code='RUD/W_STANDARD_SO/WC0_2', detail_price=Decimal(260.60))
Wood_kind.objects.create(forest_district=district, code='RUD/W_STANDARD_SO/WC0_3', detail_price=Decimal(296.93))
Wood_kind.objects.create(forest_district=district, code='RUD/W_STANDARD_SO/WD_1', detail_price=Decimal(170.54))
Wood_kind.objects.create(forest_district=district, code='RUD/W_STANDARD_SO/WD_2', detail_price=Decimal(185.47))
Wood_kind.objects.create(forest_district=district, code='RUD/W_STANDARD_SO/WD_3', detail_price=Decimal(201.30))

# Siewierz
print('Creating K price lists for Siewierz...')
district = Forest_district.objects.create(code='SIE', name='Siewierz K')
Wood_kind.objects.create(forest_district=district, code='SIE/S_S2A_SW/S2A', detail_price=Decimal(142.82))

Wood_kind.objects.create(forest_district=district, code='SIE/S_S2A_OPAL_BRZ/S2AP', detail_price=Decimal(131.00))

Wood_kind.objects.create(forest_district=district, code='SIE/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(153.66))


Wood_kind.objects.create(forest_district=district, code='SIE/W_STANDARD_SO/WA0_2', detail_price=Decimal(450.65))
Wood_kind.objects.create(forest_district=district, code='SIE/W_STANDARD_SO/WA0_3', detail_price=Decimal(551.87))
Wood_kind.objects.create(forest_district=district, code='SIE/W_STANDARD_SO/WB0_1', detail_price=Decimal(303.38))
Wood_kind.objects.create(forest_district=district, code='SIE/W_STANDARD_SO/WB0_2', detail_price=Decimal(373.43))
Wood_kind.objects.create(forest_district=district, code='SIE/W_STANDARD_SO/WB0_3', detail_price=Decimal(426.38))
Wood_kind.objects.create(forest_district=district, code='SIE/W_STANDARD_SO/WC0_1', detail_price=Decimal(275.80))
Wood_kind.objects.create(forest_district=district, code='SIE/W_STANDARD_SO/WC0_2', detail_price=Decimal(322.41))
Wood_kind.objects.create(forest_district=district, code='SIE/W_STANDARD_SO/WC0_3', detail_price=Decimal(367.36))
Wood_kind.objects.create(forest_district=district, code='SIE/W_STANDARD_SO/WD_1', detail_price=Decimal(210.98))
Wood_kind.objects.create(forest_district=district, code='SIE/W_STANDARD_SO/WD_2', detail_price=Decimal(229.46))
Wood_kind.objects.create(forest_district=district, code='SIE/W_STANDARD_SO/WD_3', detail_price=Decimal(249.04))

# Świerklaniec
print('Creating K price lists for Świerklaniec...')
district = Forest_district.objects.create(code='ŚWI', name='Świerklaniec K')
Wood_kind.objects.create(forest_district=district, code='ŚWI/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(153.66))

Wood_kind.objects.create(forest_district=district, code='ŚWI/S_S2B_GD_SO/S2B_D', detail_price=Decimal(178.28))

Wood_kind.objects.create(forest_district=district, code='ŚWI/W_STANDARD_SO/WA0_2', detail_price=Decimal(366.69))
Wood_kind.objects.create(forest_district=district, code='ŚWI/W_STANDARD_SO/WA0_3', detail_price=Decimal(449.06))
Wood_kind.objects.create(forest_district=district, code='ŚWI/W_STANDARD_SO/WB0_1', detail_price=Decimal(246.86))
Wood_kind.objects.create(forest_district=district, code='ŚWI/W_STANDARD_SO/WB0_2', detail_price=Decimal(303.86))
Wood_kind.objects.create(forest_district=district, code='ŚWI/W_STANDARD_SO/WB0_3', detail_price=Decimal(346.95))
Wood_kind.objects.create(forest_district=district, code='ŚWI/W_STANDARD_SO/WC0_1', detail_price=Decimal(224.42))
Wood_kind.objects.create(forest_district=district, code='ŚWI/W_STANDARD_SO/WC0_2', detail_price=Decimal(262.34))
Wood_kind.objects.create(forest_district=district, code='ŚWI/W_STANDARD_SO/WC0_3', detail_price=Decimal(298.92))
Wood_kind.objects.create(forest_district=district, code='ŚWI/W_STANDARD_SO/WD_1', detail_price=Decimal(171.67))
Wood_kind.objects.create(forest_district=district, code='ŚWI/W_STANDARD_SO/WD_2', detail_price=Decimal(186.71))
Wood_kind.objects.create(forest_district=district, code='ŚWI/W_STANDARD_SO/WD_3', detail_price=Decimal(202.65))

# Tułowice
print('Creating K price lists for Tułowice...')
district = Forest_district.objects.create(code='TUŁ', name='Tułowice K')
Wood_kind.objects.create(forest_district=district, code='TUŁ/S_S2A_OPAL_BRZ/S2AP', detail_price=Decimal(131.00))

Wood_kind.objects.create(forest_district=district, code='TUŁ/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(153.66))

# Ujsoły
print('Creating K price lists for Ujsoły...')
district = Forest_district.objects.create(code='UJS', name='Ujsoły K')
Wood_kind.objects.create(forest_district=district, code='UJS/S_S2A_BK/S2A', detail_price=Decimal(145.78))

Wood_kind.objects.create(forest_district=district, code='UJS/S_S2A_SW/S2A', detail_price=Decimal(186.16))

Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_BK/WA0_2', detail_price=Decimal(356.96))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_BK/WA0_3', detail_price=Decimal(452.11))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_BK/WB0_1', detail_price=Decimal(184.68))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_BK/WB0_2', detail_price=Decimal(236.40))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_BK/WB0_3', detail_price=Decimal(310.27))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_BK/WC0_1', detail_price=Decimal(147.75))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_BK/WC0_2', detail_price=Decimal(184.68))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_BK/WC0_3', detail_price=Decimal(236.40))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_BK/WD_1', detail_price=Decimal(132.97))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_BK/WD_2', detail_price=Decimal(147.75))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_BK/WD_3', detail_price=Decimal(162.52))

Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_SW/WA0_2', detail_price=Decimal(382.91))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_SW/WA0_3', detail_price=Decimal(463.19))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_SW/WB0_1', detail_price=Decimal(296.73))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_SW/WB0_2', detail_price=Decimal(332.93))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_SW/WB0_3', detail_price=Decimal(364.20))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_SW/WC0_1', detail_price=Decimal(246.25))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_SW/WC0_2', detail_price=Decimal(286.63))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_SW/WC0_3', detail_price=Decimal(323.08))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_SW/WD_1', detail_price=Decimal(192.32))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_SW/WD_2', detail_price=Decimal(212.76))
Wood_kind.objects.create(forest_district=district, code='UJS/W_STANDARD_SW/WD_3', detail_price=Decimal(245.75))

# Ustroń
print('Creating K price lists for Ustroń...')
district = Forest_district.objects.create(code='UST', name='Ustroń K')
Wood_kind.objects.create(forest_district=district, code='UST/S_S2A_SO/S2A', detail_price=Decimal(134.94))

Wood_kind.objects.create(forest_district=district, code='UST/S_S2A_SW/S2A', detail_price=Decimal(175.33))

Wood_kind.objects.create(forest_district=district, code='UST/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(153.66))

Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SO/WA0_2', detail_price=Decimal(341.21))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SO/WA0_3', detail_price=Decimal(417.84))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SO/WB0_1', detail_price=Decimal(229.70))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SO/WB0_2', detail_price=Decimal(282.74))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SO/WB0_3', detail_price=Decimal(322.83))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SO/WC0_1', detail_price=Decimal(208.82))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SO/WC0_2', detail_price=Decimal(244.11))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SO/WC0_3', detail_price=Decimal(278.14))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SO/WD_1', detail_price=Decimal(159.74))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SO/WD_2', detail_price=Decimal(173.73))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SO/WD_3', detail_price=Decimal(188.56))

Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SW/WA0_2', detail_price=Decimal(431.45))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SW/WA0_3', detail_price=Decimal(521.91))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SW/WB0_1', detail_price=Decimal(334.34))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SW/WB0_2', detail_price=Decimal(375.13))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SW/WB0_3', detail_price=Decimal(410.37))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SW/WC0_1', detail_price=Decimal(277.46))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SW/WC0_2', detail_price=Decimal(322.97))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SW/WC0_3', detail_price=Decimal(364.03))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SW/WD_1', detail_price=Decimal(216.70))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SW/WD_2', detail_price=Decimal(239.72))
Wood_kind.objects.create(forest_district=district, code='UST/W_STANDARD_SW/WD_3', detail_price=Decimal(276.91))

Wood_kind.objects.create(forest_district=district, code='UST/W_WD_SO/WD_1', detail_price=Decimal(181.24))
Wood_kind.objects.create(forest_district=district, code='UST/W_WD_SO/WD_2', detail_price=Decimal(200.63))
Wood_kind.objects.create(forest_district=district, code='UST/W_WD_SO/WD_3', detail_price=Decimal(231.62))

# Węgierska Górka
print('Creating K price lists for Węgierska Górka...')
district = Forest_district.objects.create(code='WĘG', name='Węgierska Górka K')
Wood_kind.objects.create(forest_district=district, code='WĘG/S_S2A_SW/S2A', detail_price=Decimal(161.54))

# Wisła
print('Creating K price lists for Wisła...')
district = Forest_district.objects.create(code='WIS', name='Wisła K')
Wood_kind.objects.create(forest_district=district, code='WIS/S_S2A_SW/S2A', detail_price=Decimal(176.31))

Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_JD/WA0_2', detail_price=Decimal(520.33))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_JD/WA0_3', detail_price=Decimal(642.19))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_JD/WB0_1', detail_price=Decimal(386.02))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_JD/WB0_2', detail_price=Decimal(421.60))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_JD/WB0_3', detail_price=Decimal(485.93))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_JD/WC0_1', detail_price=Decimal(296.48))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_JD/WC0_2', detail_price=Decimal(350.73))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_JD/WC0_3', detail_price=Decimal(382.17))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_JD/WD_1', detail_price=Decimal(210.79))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_JD/WD_2', detail_price=Decimal(225.91))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_JD/WD_3', detail_price=Decimal(238.37))

Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_SW/WA0_2', detail_price=Decimal(415.36))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_SW/WA0_3', detail_price=Decimal(502.43))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_SW/WB0_1', detail_price=Decimal(321.86))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_SW/WB0_2', detail_price=Decimal(361.14))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_SW/WB0_3', detail_price=Decimal(395.06))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_SW/WC0_1', detail_price=Decimal(267.11))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_SW/WC0_2', detail_price=Decimal(310.92))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_SW/WC0_3', detail_price=Decimal(350.45))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_SW/WD_1', detail_price=Decimal(208.61))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_SW/WD_2', detail_price=Decimal(230.78))
Wood_kind.objects.create(forest_district=district, code='WIS/W_STANDARD_SW/WD_3', detail_price=Decimal(266.58))

# Zawadzkie
print('Creating K price lists for Zawadzkie...')
district = Forest_district.objects.create(code='ZAW', name='Zawadzkie K')
Wood_kind.objects.create(forest_district=district, code='ZAW/S_S2B_GD_SO/S2B_D', detail_price=Decimal(178.28))

Wood_kind.objects.create(forest_district=district, code='ZAW/W_STANDARD_SO/WA0_2', detail_price=Decimal(329.94))
Wood_kind.objects.create(forest_district=district, code='ZAW/W_STANDARD_SO/WA0_3', detail_price=Decimal(404.05))
Wood_kind.objects.create(forest_district=district, code='ZAW/W_STANDARD_SO/WB0_1', detail_price=Decimal(222.11))
Wood_kind.objects.create(forest_district=district, code='ZAW/W_STANDARD_SO/WB0_2', detail_price=Decimal(273.40))
Wood_kind.objects.create(forest_district=district, code='ZAW/W_STANDARD_SO/WB0_3', detail_price=Decimal(312.17))
Wood_kind.objects.create(forest_district=district, code='ZAW/W_STANDARD_SO/WC0_1', detail_price=Decimal(201.92))
Wood_kind.objects.create(forest_district=district, code='ZAW/W_STANDARD_SO/WC0_2', detail_price=Decimal(236.05))
Wood_kind.objects.create(forest_district=district, code='ZAW/W_STANDARD_SO/WC0_3', detail_price=Decimal(268.96))
Wood_kind.objects.create(forest_district=district, code='ZAW/W_STANDARD_SO/WD_1', detail_price=Decimal(154.47))
Wood_kind.objects.create(forest_district=district, code='ZAW/W_STANDARD_SO/WD_2', detail_price=Decimal(168.00))
Wood_kind.objects.create(forest_district=district, code='ZAW/W_STANDARD_SO/WD_3', detail_price=Decimal(182.34))

# Bardo Śląskie
print('Creating K price lists for Bardo Śląskie...')
district = Forest_district.objects.create(code='BAR', name='Bardo Śląskie K')
Wood_kind.objects.create(forest_district=district, code='BAR/WK_STANDARD_SW/WAK_2', detail_price=Decimal(490.13))
Wood_kind.objects.create(forest_district=district, code='BAR/WK_STANDARD_SW/WAK_3', detail_price=Decimal(592.89))
Wood_kind.objects.create(forest_district=district, code='BAR/WK_STANDARD_SW/WBK_2', detail_price=Decimal(426.15))
Wood_kind.objects.create(forest_district=district, code='BAR/WK_STANDARD_SW/WBK_3', detail_price=Decimal(466.18))
Wood_kind.objects.create(forest_district=district, code='BAR/WK_STANDARD_SW/WCK_1', detail_price=Decimal(315.20))
Wood_kind.objects.create(forest_district=district, code='BAR/WK_STANDARD_SW/WCK_2', detail_price=Decimal(366.89))
Wood_kind.objects.create(forest_district=district, code='BAR/WK_STANDARD_SW/WCK_3', detail_price=Decimal(413.54))
Wood_kind.objects.create(forest_district=district, code='BAR/WK_STANDARD_SW/WDK_1', detail_price=Decimal(246.17))
Wood_kind.objects.create(forest_district=district, code='BAR/WK_STANDARD_SW/WDK_2', detail_price=Decimal(272.33))
Wood_kind.objects.create(forest_district=district, code='BAR/WK_STANDARD_SW/WDK_3', detail_price=Decimal(314.56))

# Bystrzyca Kłodzka
print('Creating K price lists for Bystrzyca Kłodzka...')
district = Forest_district.objects.create(code='BYS', name='Bystrzyca Kłodzka K')
Wood_kind.objects.create(forest_district=district, code='BYS/WK_STANDARD_SW/WAKP_2', detail_price=Decimal(417.67))
Wood_kind.objects.create(forest_district=district, code='BYS/WK_STANDARD_SW/WAKP_3', detail_price=Decimal(505.24))
Wood_kind.objects.create(forest_district=district, code='BYS/WK_STANDARD_SW/WBKP_2', detail_price=Decimal(363.14))
Wood_kind.objects.create(forest_district=district, code='BYS/WK_STANDARD_SW/WBKP_3', detail_price=Decimal(397.26))
Wood_kind.objects.create(forest_district=district, code='BYS/WK_STANDARD_SW/WCKP_1', detail_price=Decimal(268.60))
Wood_kind.objects.create(forest_district=district, code='BYS/WK_STANDARD_SW/WCKP_2', detail_price=Decimal(312.65))
Wood_kind.objects.create(forest_district=district, code='BYS/WK_STANDARD_SW/WCKP_3', detail_price=Decimal(352.40))
Wood_kind.objects.create(forest_district=district, code='BYS/WK_STANDARD_SW/WDKP_1', detail_price=Decimal(209.77))
Wood_kind.objects.create(forest_district=district, code='BYS/WK_STANDARD_SW/WDKP_2', detail_price=Decimal(232.07))
Wood_kind.objects.create(forest_district=district, code='BYS/WK_STANDARD_SW/WDKP_3', detail_price=Decimal(268.06))

# Jawor
print('Creating K price lists for Jawor...')
district = Forest_district.objects.create(code='JAW', name='Jawor K')
Wood_kind.objects.create(forest_district=district, code='JAW/WK_STANDARD_SW/WAK_2', detail_price=Decimal(436.39))
Wood_kind.objects.create(forest_district=district, code='JAW/WK_STANDARD_SW/WAK_3', detail_price=Decimal(527.88))
Wood_kind.objects.create(forest_district=district, code='JAW/WK_STANDARD_SW/WBK_2', detail_price=Decimal(379.42))
Wood_kind.objects.create(forest_district=district, code='JAW/WK_STANDARD_SW/WBK_3', detail_price=Decimal(415.05))
Wood_kind.objects.create(forest_district=district, code='JAW/WK_STANDARD_SW/WCK_1', detail_price=Decimal(280.63))
Wood_kind.objects.create(forest_district=district, code='JAW/WK_STANDARD_SW/WCK_2', detail_price=Decimal(326.66))
Wood_kind.objects.create(forest_district=district, code='JAW/WK_STANDARD_SW/WCK_3', detail_price=Decimal(368.19))
Wood_kind.objects.create(forest_district=district, code='JAW/WK_STANDARD_SW/WDK_1', detail_price=Decimal(219.18))
Wood_kind.objects.create(forest_district=district, code='JAW/WK_STANDARD_SW/WDK_2', detail_price=Decimal(242.46))
Wood_kind.objects.create(forest_district=district, code='JAW/WK_STANDARD_SW/WDK_3', detail_price=Decimal(280.07))

Wood_kind.objects.create(forest_district=district, code='JAW/W_STANDARD_SW/WA0_2', detail_price=Decimal(491.67))
Wood_kind.objects.create(forest_district=district, code='JAW/W_STANDARD_SW/WA0_3', detail_price=Decimal(594.74))
Wood_kind.objects.create(forest_district=district, code='JAW/W_STANDARD_SW/WB0_1', detail_price=Decimal(381.00))
Wood_kind.objects.create(forest_district=district, code='JAW/W_STANDARD_SW/WB0_2', detail_price=Decimal(427.48))
Wood_kind.objects.create(forest_district=district, code='JAW/W_STANDARD_SW/WB0_3', detail_price=Decimal(467.63))
Wood_kind.objects.create(forest_district=district, code='JAW/W_STANDARD_SW/WC0_1', detail_price=Decimal(316.18))
Wood_kind.objects.create(forest_district=district, code='JAW/W_STANDARD_SW/WC0_2', detail_price=Decimal(368.03))
Wood_kind.objects.create(forest_district=district, code='JAW/W_STANDARD_SW/WC0_3', detail_price=Decimal(414.83))
Wood_kind.objects.create(forest_district=district, code='JAW/W_STANDARD_SW/WD_1', detail_price=Decimal(246.93))
Wood_kind.objects.create(forest_district=district, code='JAW/W_STANDARD_SW/WD_2', detail_price=Decimal(273.18))
Wood_kind.objects.create(forest_district=district, code='JAW/W_STANDARD_SW/WD_3', detail_price=Decimal(315.55))

# Jugów
print('Creating K price lists for Jugów...')
district = Forest_district.objects.create(code='JUG', name='Jugów K')
Wood_kind.objects.create(forest_district=district, code='JUG/WK_STANDARD_SW/WAKP_2', detail_price=Decimal(438.66))
Wood_kind.objects.create(forest_district=district, code='JUG/WK_STANDARD_SW/WAKP_3', detail_price=Decimal(530.63))
Wood_kind.objects.create(forest_district=district, code='JUG/WK_STANDARD_SW/WBKP_2', detail_price=Decimal(381.41))
Wood_kind.objects.create(forest_district=district, code='JUG/WK_STANDARD_SW/WBKP_3', detail_price=Decimal(417.23))
Wood_kind.objects.create(forest_district=district, code='JUG/WK_STANDARD_SW/WCKP_1', detail_price=Decimal(282.10))
Wood_kind.objects.create(forest_district=district, code='JUG/WK_STANDARD_SW/WCKP_2', detail_price=Decimal(328.36))
Wood_kind.objects.create(forest_district=district, code='JUG/WK_STANDARD_SW/WCKP_3', detail_price=Decimal(370.12))
Wood_kind.objects.create(forest_district=district, code='JUG/WK_STANDARD_SW/WDKP_1', detail_price=Decimal(220.32))
Wood_kind.objects.create(forest_district=district, code='JUG/WK_STANDARD_SW/WDKP_2', detail_price=Decimal(243.73))
Wood_kind.objects.create(forest_district=district, code='JUG/WK_STANDARD_SW/WDKP_3', detail_price=Decimal(281.54))

# Kamienna Góra
print('Creating K price lists for Kamienna Góra...')
district = Forest_district.objects.create(code='KAM', name='Kamienna Góra K')
Wood_kind.objects.create(forest_district=district, code='KAM/WK_STANDARD_SW/WAKP_2', detail_price=Decimal(427.49))
Wood_kind.objects.create(forest_district=district, code='KAM/WK_STANDARD_SW/WAKP_3', detail_price=Decimal(517.10))
Wood_kind.objects.create(forest_district=district, code='KAM/WK_STANDARD_SW/WBKP_2', detail_price=Decimal(371.68))
Wood_kind.objects.create(forest_district=district, code='KAM/WK_STANDARD_SW/WBKP_3', detail_price=Decimal(406.58))
Wood_kind.objects.create(forest_district=district, code='KAM/WK_STANDARD_SW/WCKP_1', detail_price=Decimal(274.91))
Wood_kind.objects.create(forest_district=district, code='KAM/WK_STANDARD_SW/WCKP_2', detail_price=Decimal(320.00))
Wood_kind.objects.create(forest_district=district, code='KAM/WK_STANDARD_SW/WCKP_3', detail_price=Decimal(360.68))
Wood_kind.objects.create(forest_district=district, code='KAM/WK_STANDARD_SW/WDKP_1', detail_price=Decimal(214.70))
Wood_kind.objects.create(forest_district=district, code='KAM/WK_STANDARD_SW/WDKP_2', detail_price=Decimal(237.52))
Wood_kind.objects.create(forest_district=district, code='KAM/WK_STANDARD_SW/WDKP_3', detail_price=Decimal(274.36))

Wood_kind.objects.create(forest_district=district, code='KAM/W_STANDARD_SW/WA0_2', detail_price=Decimal(464.92))
Wood_kind.objects.create(forest_district=district, code='KAM/W_STANDARD_SW/WA0_3', detail_price=Decimal(562.40))
Wood_kind.objects.create(forest_district=district, code='KAM/W_STANDARD_SW/WB0_1', detail_price=Decimal(360.28))
Wood_kind.objects.create(forest_district=district, code='KAM/W_STANDARD_SW/WB0_2', detail_price=Decimal(404.23))
Wood_kind.objects.create(forest_district=district, code='KAM/W_STANDARD_SW/WB0_3', detail_price=Decimal(442.21))
Wood_kind.objects.create(forest_district=district, code='KAM/W_STANDARD_SW/WC0_1', detail_price=Decimal(298.99))
Wood_kind.objects.create(forest_district=district, code='KAM/W_STANDARD_SW/WC0_2', detail_price=Decimal(348.03))
Wood_kind.objects.create(forest_district=district, code='KAM/W_STANDARD_SW/WC0_3', detail_price=Decimal(392.27))
Wood_kind.objects.create(forest_district=district, code='KAM/W_STANDARD_SW/WD_1', detail_price=Decimal(233.51))
Wood_kind.objects.create(forest_district=district, code='KAM/W_STANDARD_SW/WD_2', detail_price=Decimal(258.32))
Wood_kind.objects.create(forest_district=district, code='KAM/W_STANDARD_SW/WD_3', detail_price=Decimal(298.39))

# Lądek Zdrój
print('Creating K price lists for Lądek Zdrój...')
district = Forest_district.objects.create(code='LĄD', name='Lądek Zdrój K')
Wood_kind.objects.create(forest_district=district, code='LĄD/WK_STANDARD_SW/WAKP_2', detail_price=Decimal(430.52))
Wood_kind.objects.create(forest_district=district, code='LĄD/WK_STANDARD_SW/WAKP_3', detail_price=Decimal(520.78))
Wood_kind.objects.create(forest_district=district, code='LĄD/WK_STANDARD_SW/WBKP_2', detail_price=Decimal(374.31))
Wood_kind.objects.create(forest_district=district, code='LĄD/WK_STANDARD_SW/WBKP_3', detail_price=Decimal(409.48))
Wood_kind.objects.create(forest_district=district, code='LĄD/WK_STANDARD_SW/WCKP_1', detail_price=Decimal(276.86))
Wood_kind.objects.create(forest_district=district, code='LĄD/WK_STANDARD_SW/WCKP_2', detail_price=Decimal(322.27))
Wood_kind.objects.create(forest_district=district, code='LĄD/WK_STANDARD_SW/WCKP_3', detail_price=Decimal(363.24))
Wood_kind.objects.create(forest_district=district, code='LĄD/WK_STANDARD_SW/WDKP_1', detail_price=Decimal(216.23))
Wood_kind.objects.create(forest_district=district, code='LĄD/WK_STANDARD_SW/WDKP_2', detail_price=Decimal(239.21))
Wood_kind.objects.create(forest_district=district, code='LĄD/WK_STANDARD_SW/WDKP_3', detail_price=Decimal(276.31))

Wood_kind.objects.create(forest_district=district, code='LĄD/W_STANDARD_SW/WA0_2', detail_price=Decimal(511.57))
Wood_kind.objects.create(forest_district=district, code='LĄD/W_STANDARD_SW/WA0_3', detail_price=Decimal(618.82))
Wood_kind.objects.create(forest_district=district, code='LĄD/W_STANDARD_SW/WB0_1', detail_price=Decimal(396.43))
Wood_kind.objects.create(forest_district=district, code='LĄD/W_STANDARD_SW/WB0_2', detail_price=Decimal(444.79))
Wood_kind.objects.create(forest_district=district, code='LĄD/W_STANDARD_SW/WB0_3', detail_price=Decimal(486.58))
Wood_kind.objects.create(forest_district=district, code='LĄD/W_STANDARD_SW/WC0_1', detail_price=Decimal(329.00))
Wood_kind.objects.create(forest_district=district, code='LĄD/W_STANDARD_SW/WC0_2', detail_price=Decimal(382.94))
Wood_kind.objects.create(forest_district=district, code='LĄD/W_STANDARD_SW/WC0_3', detail_price=Decimal(431.63))
Wood_kind.objects.create(forest_district=district, code='LĄD/W_STANDARD_SW/WD_1', detail_price=Decimal(256.93))
Wood_kind.objects.create(forest_district=district, code='LĄD/W_STANDARD_SW/WD_2', detail_price=Decimal(284.25))
Wood_kind.objects.create(forest_district=district, code='LĄD/W_STANDARD_SW/WD_3', detail_price=Decimal(328.33))

# Lwówek Śląski
print('Creating K price lists for Lwówek Śląski...')
district = Forest_district.objects.create(code='LWÓ', name='Lwówek Śląski K')
Wood_kind.objects.create(forest_district=district, code='LWÓ/WK_STANDARD_SW/WAKP_2', detail_price=Decimal(396.53))
Wood_kind.objects.create(forest_district=district, code='LWÓ/WK_STANDARD_SW/WAKP_3', detail_price=Decimal(479.66))
Wood_kind.objects.create(forest_district=district, code='LWÓ/WK_STANDARD_SW/WBKP_2', detail_price=Decimal(344.77))
Wood_kind.objects.create(forest_district=district, code='LWÓ/WK_STANDARD_SW/WBKP_3', detail_price=Decimal(377.15))
Wood_kind.objects.create(forest_district=district, code='LWÓ/WK_STANDARD_SW/WCKP_1', detail_price=Decimal(255.00))
Wood_kind.objects.create(forest_district=district, code='LWÓ/WK_STANDARD_SW/WCKP_2', detail_price=Decimal(296.83))
Wood_kind.objects.create(forest_district=district, code='LWÓ/WK_STANDARD_SW/WCKP_3', detail_price=Decimal(334.56))
Wood_kind.objects.create(forest_district=district, code='LWÓ/WK_STANDARD_SW/WDKP_1', detail_price=Decimal(199.15))
Wood_kind.objects.create(forest_district=district, code='LWÓ/WK_STANDARD_SW/WDKP_2', detail_price=Decimal(220.32))
Wood_kind.objects.create(forest_district=district, code='LWÓ/WK_STANDARD_SW/WDKP_3', detail_price=Decimal(254.49))

# Międzylesie
print('Creating K price lists for Międzylesie...')
district = Forest_district.objects.create(code='MIĘ', name='Międzylesie K')
Wood_kind.objects.create(forest_district=district, code='MIĘ/S_S2A_ENER_LISCIASTE/S2AC', detail_price=Decimal(122.14))

Wood_kind.objects.create(forest_district=district, code='MIĘ/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(107.36))

Wood_kind.objects.create(forest_district=district, code='MIĘ/WK_STANDARD_SW/WAK_2', detail_price=Decimal(444.00))
Wood_kind.objects.create(forest_district=district, code='MIĘ/WK_STANDARD_SW/WAK_3', detail_price=Decimal(534.36))
Wood_kind.objects.create(forest_district=district, code='MIĘ/WK_STANDARD_SW/WBK_2', detail_price=Decimal(384.08))
Wood_kind.objects.create(forest_district=district, code='MIĘ/WK_STANDARD_SW/WBK_3', detail_price=Decimal(420.16))
Wood_kind.objects.create(forest_district=district, code='MIĘ/WK_STANDARD_SW/WCK_1', detail_price=Decimal(284.08))
Wood_kind.objects.create(forest_district=district, code='MIĘ/WK_STANDARD_SW/WCK_2', detail_price=Decimal(330.67))
Wood_kind.objects.create(forest_district=district, code='MIĘ/WK_STANDARD_SW/WCK_3', detail_price=Decimal(372.71))
Wood_kind.objects.create(forest_district=district, code='MIĘ/WK_STANDARD_SW/WDK_1', detail_price=Decimal(221.87))
Wood_kind.objects.create(forest_district=district, code='MIĘ/WK_STANDARD_SW/WDK_2', detail_price=Decimal(245.45))
Wood_kind.objects.create(forest_district=district, code='MIĘ/WK_STANDARD_SW/WDK_3', detail_price=Decimal(283.51))

Wood_kind.objects.create(forest_district=district, code='MIĘ/W_STANDARD_SW/WA0_2', detail_price=Decimal(486.66))
Wood_kind.objects.create(forest_district=district, code='MIĘ/W_STANDARD_SW/WA0_3', detail_price=Decimal(588.70))
Wood_kind.objects.create(forest_district=district, code='MIĘ/W_STANDARD_SW/WB0_1', detail_price=Decimal(377.12))
Wood_kind.objects.create(forest_district=district, code='MIĘ/W_STANDARD_SW/WB0_2', detail_price=Decimal(423.13))
Wood_kind.objects.create(forest_district=district, code='MIĘ/W_STANDARD_SW/WB0_3', detail_price=Decimal(462.88))
Wood_kind.objects.create(forest_district=district, code='MIĘ/W_STANDARD_SW/WC0_1', detail_price=Decimal(312.96))
Wood_kind.objects.create(forest_district=district, code='MIĘ/W_STANDARD_SW/WC0_2', detail_price=Decimal(364.29))
Wood_kind.objects.create(forest_district=district, code='MIĘ/W_STANDARD_SW/WC0_3', detail_price=Decimal(410.61))
Wood_kind.objects.create(forest_district=district, code='MIĘ/W_STANDARD_SW/WD_1', detail_price=Decimal(244.42))
Wood_kind.objects.create(forest_district=district, code='MIĘ/W_STANDARD_SW/WD_2', detail_price=Decimal(270.40))
Wood_kind.objects.create(forest_district=district, code='MIĘ/W_STANDARD_SW/WD_3', detail_price=Decimal(312.34))

# Szklarska Poręba
print('Creating K price lists for Szklarska Poręba...')
district = Forest_district.objects.create(code='SZK', name='Szklarska Poręba K')
Wood_kind.objects.create(forest_district=district, code='SZK/WK_STANDARD_SW/WAKP_2', detail_price=Decimal(495.11))
Wood_kind.objects.create(forest_district=district, code='SZK/WK_STANDARD_SW/WAKP_3', detail_price=Decimal(592.89))
Wood_kind.objects.create(forest_district=district, code='SZK/WK_STANDARD_SW/WBKP_2', detail_price=Decimal(426.15))
Wood_kind.objects.create(forest_district=district, code='SZK/WK_STANDARD_SW/WBKP_3', detail_price=Decimal(466.18))
Wood_kind.objects.create(forest_district=district, code='SZK/WK_STANDARD_SW/WCKP_1', detail_price=Decimal(315.20))
Wood_kind.objects.create(forest_district=district, code='SZK/WK_STANDARD_SW/WCKP_2', detail_price=Decimal(366.89))
Wood_kind.objects.create(forest_district=district, code='SZK/WK_STANDARD_SW/WCKP_3', detail_price=Decimal(413.54))
Wood_kind.objects.create(forest_district=district, code='SZK/WK_STANDARD_SW/WDKP_1', detail_price=Decimal(246.17))
Wood_kind.objects.create(forest_district=district, code='SZK/WK_STANDARD_SW/WDKP_2', detail_price=Decimal(272.33))
Wood_kind.objects.create(forest_district=district, code='SZK/WK_STANDARD_SW/WDKP_3', detail_price=Decimal(314.56))

# Śnieżka
print('Creating K price lists for Śnieżka...')
district = Forest_district.objects.create(code='ŚNI', name='Śnieżka K')
Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_BC_SW/WBCKP_1', detail_price=Decimal(304.36))
Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_BC_SW/WBCKP_2', detail_price=Decimal(357.02))
Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_BC_SW/WBCKP_3', detail_price=Decimal(401.76))

Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_STANDARD_SW/WAKP_2', detail_price=Decimal(369.13))
Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_STANDARD_SW/WAKP_3', detail_price=Decimal(446.52))
Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_STANDARD_SW/WBKP_2', detail_price=Decimal(320.94))
Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_STANDARD_SW/WBKP_3', detail_price=Decimal(351.09))
Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_STANDARD_SW/WCKP_1', detail_price=Decimal(237.38))
Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_STANDARD_SW/WCKP_2', detail_price=Decimal(276.31))
Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_STANDARD_SW/WCKP_3', detail_price=Decimal(311.44))
Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_STANDARD_SW/WDKP_1', detail_price=Decimal(185.39))
Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_STANDARD_SW/WDKP_2', detail_price=Decimal(205.09))
Wood_kind.objects.create(forest_district=district, code='ŚNI/WK_STANDARD_SW/WDKP_3', detail_price=Decimal(236.91))

# Świdnica
print('Creating K price lists for Świdnica...')
district = Forest_district.objects.create(code='ŚWD', name='Świdnica K')
Wood_kind.objects.create(forest_district=district, code='ŚWD/W_STANDARD_SW/WA0_2', detail_price=Decimal(465.62))
Wood_kind.objects.create(forest_district=district, code='ŚWD/W_STANDARD_SW/WA0_3', detail_price=Decimal(563.24))
Wood_kind.objects.create(forest_district=district, code='ŚWD/W_STANDARD_SW/WB0_1', detail_price=Decimal(360.82))
Wood_kind.objects.create(forest_district=district, code='ŚWD/W_STANDARD_SW/WB0_2', detail_price=Decimal(404.84))
Wood_kind.objects.create(forest_district=district, code='ŚWD/W_STANDARD_SW/WB0_3', detail_price=Decimal(442.87))
Wood_kind.objects.create(forest_district=district, code='ŚWD/W_STANDARD_SW/WC0_1', detail_price=Decimal(299.44))
Wood_kind.objects.create(forest_district=district, code='ŚWD/W_STANDARD_SW/WC0_2', detail_price=Decimal(348.55))
Wood_kind.objects.create(forest_district=district, code='ŚWD/W_STANDARD_SW/WC0_3', detail_price=Decimal(392.86))
Wood_kind.objects.create(forest_district=district, code='ŚWD/W_STANDARD_SW/WD_1', detail_price=Decimal(233.85))
Wood_kind.objects.create(forest_district=district, code='ŚWD/W_STANDARD_SW/WD_2', detail_price=Decimal(258.72))
Wood_kind.objects.create(forest_district=district, code='ŚWD/W_STANDARD_SW/WD_3', detail_price=Decimal(298.83))

# Zdroje
print('Creating K price lists for Zdroje...')
district = Forest_district.objects.create(code='ZDR', name='Zdroje K')
Wood_kind.objects.create(forest_district=district, code='ZDR/WK_STANDARD_SW/WAKP_2', detail_price=Decimal(435.78))
Wood_kind.objects.create(forest_district=district, code='ZDR/WK_STANDARD_SW/WAKP_3', detail_price=Decimal(527.15))
Wood_kind.objects.create(forest_district=district, code='ZDR/WK_STANDARD_SW/WBKP_2', detail_price=Decimal(378.90))
Wood_kind.objects.create(forest_district=district, code='ZDR/WK_STANDARD_SW/WBKP_3', detail_price=Decimal(414.48))
Wood_kind.objects.create(forest_district=district, code='ZDR/WK_STANDARD_SW/WCKP_1', detail_price=Decimal(280.25))
Wood_kind.objects.create(forest_district=district, code='ZDR/WK_STANDARD_SW/WCKP_2', detail_price=Decimal(326.21))
Wood_kind.objects.create(forest_district=district, code='ZDR/WK_STANDARD_SW/WCKP_3', detail_price=Decimal(367.69))
Wood_kind.objects.create(forest_district=district, code='ZDR/WK_STANDARD_SW/WDKP_1', detail_price=Decimal(218.87))
Wood_kind.objects.create(forest_district=district, code='ZDR/WK_STANDARD_SW/WDKP_2', detail_price=Decimal(242.13))
Wood_kind.objects.create(forest_district=district, code='ZDR/WK_STANDARD_SW/WDKP_3', detail_price=Decimal(279.69))

Wood_kind.objects.create(forest_district=district, code='ZDR/W_STANDARD_SW/WA0_2', detail_price=Decimal(474.81))
Wood_kind.objects.create(forest_district=district, code='ZDR/W_STANDARD_SW/WA0_3', detail_price=Decimal(574.36))
Wood_kind.objects.create(forest_district=district, code='ZDR/W_STANDARD_SW/WB0_1', detail_price=Decimal(367.94))
Wood_kind.objects.create(forest_district=district, code='ZDR/W_STANDARD_SW/WB0_2', detail_price=Decimal(412.83))
Wood_kind.objects.create(forest_district=district, code='ZDR/W_STANDARD_SW/WB0_3', detail_price=Decimal(451.61))
Wood_kind.objects.create(forest_district=district, code='ZDR/W_STANDARD_SW/WC0_1', detail_price=Decimal(305.35))
Wood_kind.objects.create(forest_district=district, code='ZDR/W_STANDARD_SW/WC0_2', detail_price=Decimal(355.42))
Wood_kind.objects.create(forest_district=district, code='ZDR/W_STANDARD_SW/WC0_3', detail_price=Decimal(400.61))
Wood_kind.objects.create(forest_district=district, code='ZDR/W_STANDARD_SW/WD_1', detail_price=Decimal(238.47))
Wood_kind.objects.create(forest_district=district, code='ZDR/W_STANDARD_SW/WD_2', detail_price=Decimal(263.82))
Wood_kind.objects.create(forest_district=district, code='ZDR/W_STANDARD_SW/WD_3', detail_price=Decimal(304.73))

# Złotoryja
print('Creating K price lists for Złotoryja...')
district = Forest_district.objects.create(code='ZŁO', name='Złotoryja K')
Wood_kind.objects.create(forest_district=district, code='ZŁO/WK_STANDARD_SW/WAKP_2', detail_price=Decimal(367.60))
Wood_kind.objects.create(forest_district=district, code='ZŁO/WK_STANDARD_SW/WAKP_3', detail_price=Decimal(444.66))
Wood_kind.objects.create(forest_district=district, code='ZŁO/WK_STANDARD_SW/WBKP_2', detail_price=Decimal(319.61))
Wood_kind.objects.create(forest_district=district, code='ZŁO/WK_STANDARD_SW/WBKP_3', detail_price=Decimal(349.63))
Wood_kind.objects.create(forest_district=district, code='ZŁO/WK_STANDARD_SW/WCKP_1', detail_price=Decimal(236.40))
Wood_kind.objects.create(forest_district=district, code='ZŁO/WK_STANDARD_SW/WCKP_2', detail_price=Decimal(275.16))
Wood_kind.objects.create(forest_district=district, code='ZŁO/WK_STANDARD_SW/WCKP_3', detail_price=Decimal(310.15))
Wood_kind.objects.create(forest_district=district, code='ZŁO/WK_STANDARD_SW/WDKP_1', detail_price=Decimal(184.62))
Wood_kind.objects.create(forest_district=district, code='ZŁO/WK_STANDARD_SW/WDKP_2', detail_price=Decimal(204.24))
Wood_kind.objects.create(forest_district=district, code='ZŁO/WK_STANDARD_SW/WDKP_3', detail_price=Decimal(235.92))

# Dojlidy
print('Creating K price lists for Dojlidy...')
district = Forest_district.objects.create(code='DOJ', name='Dojlidy K')
Wood_kind.objects.create(forest_district=district, code='DOJ/WK_STANDARD_SW/WAK_2', detail_price=Decimal(306.33))
Wood_kind.objects.create(forest_district=district, code='DOJ/WK_STANDARD_SW/WAK_3', detail_price=Decimal(370.55))
Wood_kind.objects.create(forest_district=district, code='DOJ/WK_STANDARD_SW/WBK_2', detail_price=Decimal(266.34))
Wood_kind.objects.create(forest_district=district, code='DOJ/WK_STANDARD_SW/WBK_3', detail_price=Decimal(389.86))
Wood_kind.objects.create(forest_district=district, code='DOJ/WK_STANDARD_SW/WCK_1', detail_price=Decimal(197.00))
Wood_kind.objects.create(forest_district=district, code='DOJ/WK_STANDARD_SW/WCK_2', detail_price=Decimal(229.30))
Wood_kind.objects.create(forest_district=district, code='DOJ/WK_STANDARD_SW/WCK_3', detail_price=Decimal(258.46))
Wood_kind.objects.create(forest_district=district, code='DOJ/WK_STANDARD_SW/WDK_1', detail_price=Decimal(153.85))
Wood_kind.objects.create(forest_district=district, code='DOJ/WK_STANDARD_SW/WDK_2', detail_price=Decimal(170.20))
Wood_kind.objects.create(forest_district=district, code='DOJ/WK_STANDARD_SW/WDK_3', detail_price=Decimal(196.60))

# Drygały
print('Creating K price lists for Drygały...')
district = Forest_district.objects.create(code='DRY', name='Drygały K')
Wood_kind.objects.create(forest_district=district, code='DRY/WK_STANDARD_SW/WAK_2', detail_price=Decimal(306.33))
Wood_kind.objects.create(forest_district=district, code='DRY/WK_STANDARD_SW/WAK_3', detail_price=Decimal(370.55))
Wood_kind.objects.create(forest_district=district, code='DRY/WK_STANDARD_SW/WBK_2', detail_price=Decimal(266.34))
Wood_kind.objects.create(forest_district=district, code='DRY/WK_STANDARD_SW/WBK_3', detail_price=Decimal(291.36))
Wood_kind.objects.create(forest_district=district, code='DRY/WK_STANDARD_SW/WCK_1', detail_price=Decimal(197.00))
Wood_kind.objects.create(forest_district=district, code='DRY/WK_STANDARD_SW/WCK_2', detail_price=Decimal(229.30))
Wood_kind.objects.create(forest_district=district, code='DRY/WK_STANDARD_SW/WCK_3', detail_price=Decimal(258.46))
Wood_kind.objects.create(forest_district=district, code='DRY/WK_STANDARD_SW/WDK_1', detail_price=Decimal(153.85))
Wood_kind.objects.create(forest_district=district, code='DRY/WK_STANDARD_SW/WDK_2', detail_price=Decimal(170.80))
Wood_kind.objects.create(forest_district=district, code='DRY/WK_STANDARD_SW/WDK_3', detail_price=Decimal(196.60))

# Górowo Iławieckie
print('Creating K price lists for Górowo Iławieckie...')
district = Forest_district.objects.create(code='GÓR', name='Górowo Iławieckie K')
Wood_kind.objects.create(forest_district=district, code='GÓR/WK_STANDARD_SW/WAK_2', detail_price=Decimal(295.61))
Wood_kind.objects.create(forest_district=district, code='GÓR/WK_STANDARD_SW/WAK_3', detail_price=Decimal(357.58))
Wood_kind.objects.create(forest_district=district, code='GÓR/WK_STANDARD_SW/WBK_2', detail_price=Decimal(257.02))
Wood_kind.objects.create(forest_district=district, code='GÓR/WK_STANDARD_SW/WBK_3', detail_price=Decimal(281.16))
Wood_kind.objects.create(forest_district=district, code='GÓR/WK_STANDARD_SW/WCK_1', detail_price=Decimal(190.10))
Wood_kind.objects.create(forest_district=district, code='GÓR/WK_STANDARD_SW/WCK_2', detail_price=Decimal(221.28))
Wood_kind.objects.create(forest_district=district, code='GÓR/WK_STANDARD_SW/WCK_3', detail_price=Decimal(249.42))
Wood_kind.objects.create(forest_district=district, code='GÓR/WK_STANDARD_SW/WDK_1', detail_price=Decimal(148.46))
Wood_kind.objects.create(forest_district=district, code='GÓR/WK_STANDARD_SW/WDK_2', detail_price=Decimal(164.24))
Wood_kind.objects.create(forest_district=district, code='GÓR/WK_STANDARD_SW/WDK_3', detail_price=Decimal(189.72))

# Olsztyn
print('Creating K price lists for Olsztyn...')
district = Forest_district.objects.create(code='OLS', name='Olsztyn K')
Wood_kind.objects.create(forest_district=district, code='OLS/WK_STANDARD_SW/WAK_2', detail_price=Decimal(306.33))
Wood_kind.objects.create(forest_district=district, code='OLS/WK_STANDARD_SW/WAK_3', detail_price=Decimal(370.55))
Wood_kind.objects.create(forest_district=district, code='OLS/WK_STANDARD_SW/WBK_2', detail_price=Decimal(266.34))
Wood_kind.objects.create(forest_district=district, code='OLS/WK_STANDARD_SW/WBK_3', detail_price=Decimal(291.36))
Wood_kind.objects.create(forest_district=district, code='OLS/WK_STANDARD_SW/WCK_1', detail_price=Decimal(197.00))
Wood_kind.objects.create(forest_district=district, code='OLS/WK_STANDARD_SW/WCK_2', detail_price=Decimal(229.30))
Wood_kind.objects.create(forest_district=district, code='OLS/WK_STANDARD_SW/WCK_3', detail_price=Decimal(258.46))
Wood_kind.objects.create(forest_district=district, code='OLS/WK_STANDARD_SW/WDK_1', detail_price=Decimal(153.85))
Wood_kind.objects.create(forest_district=district, code='OLS/WK_STANDARD_SW/WDK_2', detail_price=Decimal(170.20))
Wood_kind.objects.create(forest_district=district, code='OLS/WK_STANDARD_SW/WDK_3', detail_price=Decimal(196.60))

# Orneta
print('Creating K price lists for Orneta...')
district = Forest_district.objects.create(code='ORN', name='Orneta K')
Wood_kind.objects.create(forest_district=district, code='ORN/WK_STANDARD_SW/WAK_2', detail_price=Decimal(294.08))
Wood_kind.objects.create(forest_district=district, code='ORN/WK_STANDARD_SW/WAK_3', detail_price=Decimal(355.73))
Wood_kind.objects.create(forest_district=district, code='ORN/WK_STANDARD_SW/WBK_2', detail_price=Decimal(255.68))
Wood_kind.objects.create(forest_district=district, code='ORN/WK_STANDARD_SW/WBK_3', detail_price=Decimal(279.71))
Wood_kind.objects.create(forest_district=district, code='ORN/WK_STANDARD_SW/WCK_1', detail_price=Decimal(189.12))
Wood_kind.objects.create(forest_district=district, code='ORN/WK_STANDARD_SW/WCK_2', detail_price=Decimal(220.13))
Wood_kind.objects.create(forest_district=district, code='ORN/WK_STANDARD_SW/WCK_3', detail_price=Decimal(248.12))
Wood_kind.objects.create(forest_district=district, code='ORN/WK_STANDARD_SW/WDK_1', detail_price=Decimal(147.70))
Wood_kind.objects.create(forest_district=district, code='ORN/WK_STANDARD_SW/WDK_2', detail_price=Decimal(163.40))
Wood_kind.objects.create(forest_district=district, code='ORN/WK_STANDARD_SW/WDK_3', detail_price=Decimal(188.74))

# Płaska
print('Creating K price lists for Płaska...')
district = Forest_district.objects.create(code='PŁA', name='Płaska K')
Wood_kind.objects.create(forest_district=district, code='PŁA/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(86.68))

Wood_kind.objects.create(forest_district=district, code='PŁA/WK_STANDARD_SW/WAK_2', detail_price=Decimal(300.20))
Wood_kind.objects.create(forest_district=district, code='PŁA/WK_STANDARD_SW/WAK_3', detail_price=Decimal(363.14))
Wood_kind.objects.create(forest_district=district, code='PŁA/WK_STANDARD_SW/WBK_2', detail_price=Decimal(261.01))
Wood_kind.objects.create(forest_district=district, code='PŁA/WK_STANDARD_SW/WBK_3', detail_price=Decimal(285.53))
Wood_kind.objects.create(forest_district=district, code='PŁA/WK_STANDARD_SW/WCK_1', detail_price=Decimal(193.06))
Wood_kind.objects.create(forest_district=district, code='PŁA/WK_STANDARD_SW/WCK_2', detail_price=Decimal(224.71))
Wood_kind.objects.create(forest_district=district, code='PŁA/WK_STANDARD_SW/WCK_3', detail_price=Decimal(253.29))
Wood_kind.objects.create(forest_district=district, code='PŁA/WK_STANDARD_SW/WDK_1', detail_price=Decimal(150.78))
Wood_kind.objects.create(forest_district=district, code='PŁA/WK_STANDARD_SW/WDK_2', detail_price=Decimal(166.80))
Wood_kind.objects.create(forest_district=district, code='PŁA/WK_STANDARD_SW/WDK_3', detail_price=Decimal(192.67))

# Suwałki
print('Creating K price lists for Suwałki...')
district = Forest_district.objects.create(code='SUW', name='Suwałki K')
Wood_kind.objects.create(forest_district=district, code='SUW/WK_STANDARD_SW/WAK_2', detail_price=Decimal(300.20))
Wood_kind.objects.create(forest_district=district, code='SUW/WK_STANDARD_SW/WAK_3', detail_price=Decimal(363.14))
Wood_kind.objects.create(forest_district=district, code='SUW/WK_STANDARD_SW/WBK_2', detail_price=Decimal(261.01))
Wood_kind.objects.create(forest_district=district, code='SUW/WK_STANDARD_SW/WBK_3', detail_price=Decimal(285.53))
Wood_kind.objects.create(forest_district=district, code='SUW/WK_STANDARD_SW/WCK_1', detail_price=Decimal(193.06))
Wood_kind.objects.create(forest_district=district, code='SUW/WK_STANDARD_SW/WCK_2', detail_price=Decimal(224.71))
Wood_kind.objects.create(forest_district=district, code='SUW/WK_STANDARD_SW/WCK_3', detail_price=Decimal(253.29))
Wood_kind.objects.create(forest_district=district, code='SUW/WK_STANDARD_SW/WDK_1', detail_price=Decimal(150.78))
Wood_kind.objects.create(forest_district=district, code='SUW/WK_STANDARD_SW/WDK_2', detail_price=Decimal(166.80))
Wood_kind.objects.create(forest_district=district, code='SUW/WK_STANDARD_SW/WDK_3', detail_price=Decimal(192.67))

# Nowe Ramuki
print('Creating K price lists for Nowe Ramuki...')
district = Forest_district.objects.create(code='NOW', name='Nowe Ramuki K')
Wood_kind.objects.create(forest_district=district, code='NOW/WK_STANDARD_SW/WAKP_2', detail_price=Decimal(304.80))
Wood_kind.objects.create(forest_district=district, code='NOW/WK_STANDARD_SW/WAKP_3', detail_price=Decimal(368.70))
Wood_kind.objects.create(forest_district=district, code='NOW/WK_STANDARD_SW/WBKP_2', detail_price=Decimal(265.01))
Wood_kind.objects.create(forest_district=district, code='NOW/WK_STANDARD_SW/WBKP_3', detail_price=Decimal(289.90))
Wood_kind.objects.create(forest_district=district, code='NOW/WK_STANDARD_SW/WCKP_1', detail_price=Decimal(196.01))
Wood_kind.objects.create(forest_district=district, code='NOW/WK_STANDARD_SW/WCKP_2', detail_price=Decimal(228.16))
Wood_kind.objects.create(forest_district=district, code='NOW/WK_STANDARD_SW/WCKP_3', detail_price=Decimal(257.17))
Wood_kind.objects.create(forest_district=district, code='NOW/WK_STANDARD_SW/WDKP_1', detail_price=Decimal(153.08))
Wood_kind.objects.create(forest_district=district, code='NOW/WK_STANDARD_SW/WDKP_2', detail_price=Decimal(169.36))
Wood_kind.objects.create(forest_district=district, code='NOW/WK_STANDARD_SW/WDKP_3', detail_price=Decimal(195.62))

# Żednia
print('Creating K price lists for Żednia...')
district = Forest_district.objects.create(code='ŻED', name='Żednia K')
Wood_kind.objects.create(forest_district=district, code='ŻED/WK_STANDARD_SW/WAK_2', detail_price=Decimal(306.33))
Wood_kind.objects.create(forest_district=district, code='ŻED/WK_STANDARD_SW/WAK_3', detail_price=Decimal(370.55))
Wood_kind.objects.create(forest_district=district, code='ŻED/WK_STANDARD_SW/WBK_2', detail_price=Decimal(266.34))
Wood_kind.objects.create(forest_district=district, code='ŻED/WK_STANDARD_SW/WBK_3', detail_price=Decimal(291.36))
Wood_kind.objects.create(forest_district=district, code='ŻED/WK_STANDARD_SW/WCK_1', detail_price=Decimal(197.00))
Wood_kind.objects.create(forest_district=district, code='ŻED/WK_STANDARD_SW/WCK_2', detail_price=Decimal(229.30))
Wood_kind.objects.create(forest_district=district, code='ŻED/WK_STANDARD_SW/WCK_3', detail_price=Decimal(258.46))
Wood_kind.objects.create(forest_district=district, code='ŻED/WK_STANDARD_SW/WDK_1', detail_price=Decimal(153.85))
Wood_kind.objects.create(forest_district=district, code='ŻED/WK_STANDARD_SW/WDK_2', detail_price=Decimal(170.20))
Wood_kind.objects.create(forest_district=district, code='ŻED/WK_STANDARD_SW/WDK_3', detail_price=Decimal(196.60))

# Wichrowo
print('Creating K price lists for Wichrowo...')
district = Forest_district.objects.create(code='WIC', name='Wichrowo K')
Wood_kind.objects.create(forest_district=district, code='WIC/WK_STANDARD_SW/WAK_2', detail_price=Decimal(307.87))
Wood_kind.objects.create(forest_district=district, code='WIC/WK_STANDARD_SW/WAK_3', detail_price=Decimal(372.40))
Wood_kind.objects.create(forest_district=district, code='WIC/WK_STANDARD_SW/WBK_2', detail_price=Decimal(267.67))
Wood_kind.objects.create(forest_district=district, code='WIC/WK_STANDARD_SW/WBK_3', detail_price=Decimal(292.82))
Wood_kind.objects.create(forest_district=district, code='WIC/WK_STANDARD_SW/WCK_1', detail_price=Decimal(197.98))
Wood_kind.objects.create(forest_district=district, code='WIC/WK_STANDARD_SW/WCK_2', detail_price=Decimal(230.45))
Wood_kind.objects.create(forest_district=district, code='WIC/WK_STANDARD_SW/WCK_3', detail_price=Decimal(259.75))
Wood_kind.objects.create(forest_district=district, code='WIC/WK_STANDARD_SW/WDK_1', detail_price=Decimal(154.62))
Wood_kind.objects.create(forest_district=district, code='WIC/WK_STANDARD_SW/WDK_2', detail_price=Decimal(171.05))
Wood_kind.objects.create(forest_district=district, code='WIC/WK_STANDARD_SW/WDK_3', detail_price=Decimal(197.59))

print('Creating E price lists...')

# Gidle
print('Creating E price lists for Gidle...')
district = Forest_district.objects.create(code='E_GID', name='Gidle E')
Wood_kind.objects.create(forest_district=district, code='E_GID/S_S2A_OPAL_SO/S2AP', detail_price=Decimal(130.02))

Wood_kind.objects.create(forest_district=district, code='E_GID/S_S2B_CD_SO/S2BC', detail_price=Decimal(154.64))

# Lubliniec
print('Creating E price lists for Lubliniec...')
district = Forest_district.objects.create(code='E_LUB', name='Lubliniec E')
Wood_kind.objects.create(forest_district=district, code='E_LUB/S_S2A_SO/S2A', detail_price=Decimal(145.78))

# Prószków
print('Creating E price lists for Prószków...')
district = Forest_district.objects.create(code='E_PRÓ', name='Prószków E')
Wood_kind.objects.create(forest_district=district, code='E_PRÓ/S_S2A_OPAL_SO/S2AP', detail_price=Decimal(162.52))

# Turawa
print('Creating E price lists for Turawa...')
district = Forest_district.objects.create(code='E_TUR', name='Turawa E')
Wood_kind.objects.create(forest_district=district, code='E_TUR/S_S2A_SO/S2A', detail_price=Decimal(152.67))

# Turek
print('Creating E price lists for Turek...')
district = Forest_district.objects.create(code='E_TUK', name='Turek E')
Wood_kind.objects.create(forest_district=district, code='E_TUK/S_S2A_SO/S2A', detail_price=Decimal(122.14))

# Ujsoły
print('Creating E price lists for Ujsoły...')
district = Forest_district.objects.create(code='E_UJS', name='Ujsoły E')
Wood_kind.objects.create(forest_district=district, code='E_UJS/S_S2A_ENER_IGLASTE/S2AC', detail_price=Decimal(119.18))

# Wisła
print('Creating E price lists for Wisła...')
district = Forest_district.objects.create(code='E_WIS', name='Wisła E')
Wood_kind.objects.create(forest_district=district, code='E_WIS/S_S2A_ENER_IGLASTE/S2AC', detail_price=Decimal(130.02))

# Zawadzkie
print('Creating E price lists for Zawadzkie...')
district = Forest_district.objects.create(code='E_ZAW', name='Zawadzkie E')
Wood_kind.objects.create(forest_district=district, code='E_ZAW/S_S2A_SO/S2A', detail_price=Decimal(152.67))

# Lądek Zdrój
print('Creating E price lists for Lądek Zdrój...')
district = Forest_district.objects.create(code='E_LĄD', name='Lądek Zdrój E')
Wood_kind.objects.create(forest_district=district, code='E_LĄD/S_S2A_OPAL_SW/S2AP', detail_price=Decimal(109.33))

# Wałbrzych
print('Creating E price lists for Wałbrzych...')
district = Forest_district.objects.create(code='E_WAŁ', name='Wałbrzych E')
Wood_kind.objects.create(forest_district=district, code='E_WAŁ/S_S2A_OPAL_SW/S2A', detail_price=Decimal(102.44))

print('Creating contractors...')

Contractor.objects.create(code='PLAC', id=settings.PLAC_ID, name='Plac')
Contractor.objects.create(code='TARTAK', id=settings.TARTAK_ID, name='Tartak')


