#!/usr/bin/env python
import os, os.path, datetime
import xarray as xr
import pandas as pd

dirin = '/tigress/wenchang/MODEL_OUT/nudgeclimo_all_model_CTL1860_tigercpu_intelmpi_18_576PE/POSTP'
ens_default = range(1,6)

def open_data(data_name=None, nctag='atmos_month', year_start=101, n_years=100):
    ncfiles = [os.path.join(dirin, f'{year:04d}0101.{nctag}.nc') for year in range(year_start, year_start + n_years)]
    with xr.set_options(enable_cftimeindex=True):
        ds = xr.open_mfdataset(ncfiles)
    if data_name is None:
        return ds
    da = ds[data_name]

    return da

def open_ensemble(data_name, nctag='atmos_month', ens=None, year_start_ens1=111, n_years=5, year_volcano=1963):
    if ens is None:
        ens = ens_default
    das = []
    for en in ens:
        year_start = year_start_ens1 -1 + en
        da = open_data(data_name, nctag=nctag, year_start=year_start, n_years=n_years)
        year_shift = year_volcano - year_start
        new_time = [datetime.datetime(*t.replace(year=t.year+year_shift).timetuple()[0:6]) 
                            for t in da.time.values]
        da['time'] = new_time 
        das.append(da)

    dae = xr.concat(das, pd.Index(ens, name='en'))

    return dae

if __name__ == '__main__':
    ds = open_data()
    print(ds)
