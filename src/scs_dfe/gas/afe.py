"""
Created on 18 Mar 2018

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)

Compatibility with the scs_dfe_eng AFE interface
"""

import time

from scs_core.gas.a4_datum import A4Datum
from scs_core.gas.d4_datum import D4Datum

from scs_core.gas.afe_datum import AFEDatum

from scs_dfe.gas.ads1115 import ADS1115


# --------------------------------------------------------------------------------------------------------------------

class AFE(object):
    """
    Alphasense Educational Board with Ti ADS1115 ADC
    """

    __H2S_GAIN_INDEX = 3            # ADS1115.GAIN_2p048
    __CO_GAIN_INDEX = 3             # ADS1115.GAIN_2p048
    __RATE = ADS1115.RATE_8

    __MUX = (ADS1115.MUX_A0_GND, ADS1115.MUX_A2_GND, ADS1115.MUX_A3_GND)


    # ----------------------------------------------------------------------------------------------------------------

    # noinspection PyUnusedLocal
    def __init__(self, dfe_conf, pt1000, sensors):
        """
        Constructor
        """
        self.__sensors = sensors

        self.__wrk_adc = ADS1115(ADS1115.ADDR_WRK, AFE.__RATE)
        self.__aux_adc = ADS1115(ADS1115.ADDR_AUX, AFE.__RATE)

        self.__tconv = self.__wrk_adc.tconv


    # ----------------------------------------------------------------------------------------------------------------

    # noinspection PyUnusedLocal
    def sample(self, sht_datum=None):
        # temperature...
        temp = self.sample_temp(sht_datum)

        # gases...
        samples = []

        # NO2...
        sample = self.__sensors[0].sample(self, temp, 0, None)

        samples.append(('NO2', sample))

        # H2S...
        we_v = self.sample_raw_wrk(1, self.__H2S_GAIN_INDEX)
        sample = D4Datum(we_v)

        samples.append(('H2S', sample))

        # CO...
        we_v = self.sample_raw_wrk(2, self.__CO_GAIN_INDEX)
        sample = D4Datum(we_v)

        samples.append(('CO', sample))

        return AFEDatum(None, *samples)


    @classmethod
    def null_datum(cls):
        samples = [
            ('NO2', A4Datum(None, None)),
            ('H2S', D4Datum(None)),
            ('CO', D4Datum(None)),
        ]

        return AFEDatum(None, *samples)


    @staticmethod
    def sample_temp(sht_datum):
        if sht_datum is None:
            return None

        return sht_datum.temp


    # ----------------------------------------------------------------------------------------------------------------

    def sample_raw_wrk_aux(self, sensor_index, gain_index):
        try:
            mux = AFE.__MUX[sensor_index]
            gain = ADS1115.gain(gain_index)

            self.__wrk_adc.start_conversion(mux, gain)
            self.__aux_adc.start_conversion(mux, gain)

            time.sleep(self.__tconv)

            we_v = self.__wrk_adc.read_conversion()
            ae_v = self.__aux_adc.read_conversion()

            return we_v, ae_v

        finally:
            self.__wrk_adc.release_lock()
            self.__aux_adc.release_lock()


    def sample_raw_wrk(self, sensor_index, gain_index):
        try:
            mux = AFE.__MUX[sensor_index]
            gain = ADS1115.gain(gain_index)

            self.__wrk_adc.start_conversion(mux, gain)

            time.sleep(self.__tconv)

            we_v = self.__wrk_adc.read_conversion()

            return we_v

        finally:
            self.__wrk_adc.release_lock()


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "AFE:{tconv:%0.3f, wrk_adc:%s, aux_adc:%s}" %  (self.__tconv, self.__wrk_adc, self.__aux_adc)
