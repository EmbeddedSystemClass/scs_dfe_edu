#!/usr/bin/env python3

"""
Created on 18 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_core.data.json import JSONify

from scs_core.gas.afe_baseline import AFEBaseline
from scs_core.gas.afe_calib import AFECalib

from scs_dfe.climate.sht_conf import SHTConf
from scs_dfe.gas.afe import AFE

from scs_host.bus.i2c import I2C

from scs_host.sys.host import Host

# --------------------------------------------------------------------------------------------------------------------

sht_conf = SHTConf.load(Host)
sht = sht_conf.int_sht()

calib = AFECalib.load(Host)

afe_calib = AFECalib.load(Host)
afe_baseline = AFEBaseline.load(Host)

sensors = afe_calib.sensors(afe_baseline)

try:
    I2C.open(Host.I2C_SENSORS)

    afe = AFE(None, None, sensors)
    print(afe)
    print("=")

    sht_datum = sht.sample()
    print(sht_datum)

    datum = afe.sample(sht_datum)
    print(datum)
    print("-")

    print(JSONify.dumps(datum))
    print("=")

    datum = afe.null_datum()
    print(datum)
    print("-")

    print(JSONify.dumps(datum))
    print("=")

finally:
    I2C.close()
