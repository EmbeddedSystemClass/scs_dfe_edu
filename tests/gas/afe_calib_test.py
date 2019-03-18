#!/usr/bin/env python3

"""
Created on 18 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

import json

from scs_core.gas.afe_calib import AFECalib

from scs_host.sys.host import Host


# --------------------------------------------------------------------------------------------------------------------

jstr = '{"serial_number": "99-000000", "type": "999-0000-00", ' \
       '"calibrated_on": "2016-11-01", "dispatched_on": null, "pt1000_v20": null, ' \
       '"sn1": {"serial_number": "212320130", "sensor_type": "NOGA4", ' \
       '"we_electronic_zero_mv": 282, "we_sensor_zero_mv": -1, "we_total_zero_mv": 281, ' \
       '"ae_electronic_zero_mv": 277, "ae_sensor_zero_mv": -2, "ae_total_zero_mv": 275, ' \
       '"we_sensitivity_na_ppb": -0.433, "we_cross_sensitivity_no2_na_ppb": -0.433, "pcb_gain": -0.73, ' \
       '"we_sensitivity_mv_ppb": 0.316, "we_cross_sensitivity_no2_mv_ppb": 0.316}}'

calib = AFECalib.construct_from_jdict(json.loads(jstr))
print(calib)
print("-")

calib.save(Host)
print("-")

