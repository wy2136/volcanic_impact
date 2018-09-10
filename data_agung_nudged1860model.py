#!/usr/bin/env python
import os, os.path
import xarray as xr
import pandas as pd

dirin = '/tigress/wenchang/MODEL_OUT/Agung_ens_noleap_nudgeclimo_all_model1860'
ens_default = range(1,6)

def open_data(data_name=None, nctag='atmos_month', ens=None):
    if ens is None:
        ens = ens_default 
    das = []
    for en in ens:
        ncfiles = os.path.join(dirin, 
            f'en{en:02d}', 'POSTP', f'*.{nctag}.nc')
        with xr.set_options(enable_cftimeindex=True):
            ds = xr.open_mfdataset(ncfiles)
        if data_name is None: # if data_name is not provided, return the first dataset
            return ds #######################
        da = ds[data_name]
        das.append(da)
    dae = xr.concat(das, pd.Index(ens, name='en'))
    return dae

if __name__ == '__main__':
    ds = open_data()
    print(ds)
