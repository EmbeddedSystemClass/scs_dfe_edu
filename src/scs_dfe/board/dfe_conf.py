"""
Created on 27 Feb 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

The DFE configuration file must be present to enable sampling operations. In this configuration it has no fields.

example document:
{"pt1000-addr": null}
"""

from collections import OrderedDict

from scs_core.data.json import PersistentJSONable

from scs_core.gas.afe_baseline import AFEBaseline
from scs_core.gas.afe_calib import AFECalib
from scs_core.gas.sensor import Sensor

from scs_dfe.gas.afe import AFE


# --------------------------------------------------------------------------------------------------------------------

class DFEConf(PersistentJSONable):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    __FILENAME = "dfe_conf.json"

    @classmethod
    def persistence_location(cls, host):
        return host.conf_dir(), cls.__FILENAME


    # ----------------------------------------------------------------------------------------------------------------

    @staticmethod
    def board_temp_sensor():
        return None


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, jdict):
        if not jdict:
            return None

        return DFEConf(None)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, _):
        """
        Constructor
        """
        super().__init__()


    # ----------------------------------------------------------------------------------------------------------------

    def afe(self, host):
        # sensors...
        afe_calib = AFECalib.load(host)

        if afe_calib is None:
            sensors = [Sensor.SENSORS[Sensor.CODE_NO2]]

        else:
            afe_baseline = AFEBaseline.load(host)
            sensors = afe_calib.sensors(afe_baseline)

        return AFE(self, None, sensors)


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['pt1000-addr'] = None

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "DFEConf:{pt1000_addr:None}"
