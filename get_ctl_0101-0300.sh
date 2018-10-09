#!/usr/bin/env bash


expname=CTL1860_noleap_tigercpu_intelmpi_18_576PE
otype=atmos_month
ifiles="/tigress/wenchang/MODEL_OUT/$expname/POSTP/010[1-9]0101.$otype.nc"
ifiles="$ifiles /tigress/wenchang/MODEL_OUT/$expname/POSTP/01[1-9][0-9]0101.$otype.nc"
ifiles="$ifiles /tigress/wenchang/MODEL_OUT/$expname/POSTP/[0-9][2][0-9][0-9]0101.$otype.nc"
ifiles="$ifiles /tigress/wenchang/MODEL_OUT/$expname/POSTP/03000101.$otype.nc"
#dataname=$1 #precip
ofile=data/$1.$expname.$otype.0101_0300.nc

echo "ncrcat -v $1 $ifiles $ofile"
ncrcat -v $1 $ifiles $ofile

