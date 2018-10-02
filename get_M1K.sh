#!/usr/bin/env bash

expname=nudgeclimo_all_model_CTL1860_M1K_tigercpu_intelmpi_18_576PE
otype=atmos_month
ifiles=/tigress/wenchang/MODEL_OUT/$expname/POSTP/????0101.$otype.nc
#dataname=$1 #precip
ofile=data/$1.$expname.$otype.nc

ncrcat -v $1 $ifiles $ofile

