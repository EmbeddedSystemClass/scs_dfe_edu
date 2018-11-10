"""
Created on 16 Jul 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

a dummy GPS configuration, to maintain compatibility with the DFE Eng package

example JSON:
{"model": null}
"""

import os

from collections import OrderedDict

from scs_core.data.json import PersistentJSONable


# --------------------------------------------------------------------------------------------------------------------

class GPSConf(PersistentJSONable):
    """
    classdocs
    """

    __FILENAME = "gps_conf.json"

    @classmethod
    def filename(cls, host):
        return os.path.join(host.conf_dir(), cls.__FILENAME)


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def construct_from_jdict(cls, _):
        return None


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, _):
        """
        Constructor
        """
        super().__init__()


    # ----------------------------------------------------------------------------------------------------------------

    @staticmethod
    def gps_monitor(_):
        return None


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def model(self):
        return None


    # ----------------------------------------------------------------------------------------------------------------

    def as_json(self):
        jdict = OrderedDict()

        jdict['model'] = None

        return jdict


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "GPSConf:{model:None}"
