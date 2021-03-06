"""
Created on 23 Jan 2019

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from abc import ABC, abstractmethod

from scs_host.lock.lock import Lock


# --------------------------------------------------------------------------------------------------------------------

class OPC(ABC):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    @abstractmethod
    def uses_spi(cls):
        pass


    @classmethod
    @abstractmethod
    def datum_class(cls):
        pass


    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    @abstractmethod
    def lock_timeout(cls):
        pass


    @classmethod
    @abstractmethod
    def boot_time(cls):
        pass


    @classmethod
    @abstractmethod
    def power_cycle_time(cls):
        pass


    # ----------------------------------------------------------------------------------------------------------------

    @abstractmethod
    def power_on(self):
        pass


    @abstractmethod
    def power_off(self):
        pass


    @abstractmethod
    def operations_on(self):
        pass


    @abstractmethod
    def operations_off(self):
        pass


    # ----------------------------------------------------------------------------------------------------------------

    @abstractmethod
    def clean(self):
        pass


    @property
    @abstractmethod
    def cleaning_interval(self):
        pass


    @cleaning_interval.setter
    @abstractmethod
    def cleaning_interval(self, interval):
        pass


    # ----------------------------------------------------------------------------------------------------------------

    @abstractmethod
    def data_ready(self):
        pass


    @abstractmethod
    def sample(self):
        pass


    # ----------------------------------------------------------------------------------------------------------------

    @abstractmethod
    def firmware(self):
        pass


    # ----------------------------------------------------------------------------------------------------------------

    @property
    @abstractmethod
    def bus(self):
        pass


    @property
    @abstractmethod
    def address(self):
        pass


    # ----------------------------------------------------------------------------------------------------------------

    def obtain_lock(self):
        Lock.acquire(self.lock_name, self.lock_timeout())


    def release_lock(self):
        Lock.release(self.lock_name)


    @property
    @abstractmethod
    def lock_name(self):
        pass

