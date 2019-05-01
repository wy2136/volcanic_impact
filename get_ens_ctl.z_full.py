#!/usr/bin/env python
import os, os.path, sys, datetime
from lib.get_data import get_ctl_data
from itertools import product

expname = 'CTL1860_noleap_tigercpu_intelmpi_18_576PE'
compname = 'atmos_month'
datanames = ['z_full',]
plev = 200
year_start = 11
n_ens = 30
n_years = 5

for dataname in datanames:
    get_ctl_data(expname=expname, compname=compname, dataname=dataname, 
        year_start=year_start, n_ens=n_ens, n_years=n_years, plev=plev)


