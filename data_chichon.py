#!/usr/bin/env python
import os, os.path
import xarray as xr
import pandas as pd

dirin = '/tigress/wenchang/MODEL_OUT/Chichon_PI_ens_noleap'
ens_default = range(1,31)

def open_data(data_name=None, nctag='atmos_month', ens=None):
    if ens is None:
        ens = ens_default 
    das = []
    for en in ens:
        ncfiles = os.path.join(dirin, 
            f'en{en:02d}', 'POSTP', f'*.{nctag}.nc')
        ds = xr.open_mfdataset(ncfiles)
        if data_name is None:
            return ds # return the dataset of the first ensemble member if data_name is not provided
        da = ds[data_name]
        das.append(da)
    dae = xr.concat(das, pd.Index(ens, name='en'))
    return dae.resample(time='MS').mean('time')

if __name__ == '__main__':
    ds = open_data()
    print(ds)
