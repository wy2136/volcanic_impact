#!/usr/bin/env python
import os, os.path, sys, datetime
from lib.get_gpi import get_volc_gpi
from itertools import product


expnames = [f'{volc}_PI_ens_noleap' 
    for volc in ('Agung', 'StMaria', 'Pinatubo')]
datanames = ['GPI', 'eta', 'H', 'Vpot', 'Vshear']
ens = range(1, 31)
for expname, dataname in product(expnames, datanames):
    get_volc_gpi(expname=expname, dataname=dataname, ens=ens)
