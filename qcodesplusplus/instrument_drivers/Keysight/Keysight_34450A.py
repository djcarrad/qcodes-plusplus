from .private.Keysight_344xxA import _Keysight_344xxA

class Keysight_34450A(_Keysight_344xxA):
    """
    This is the qcodes driver for the Keysight 34450A Multimeter
    """
    def __init__(self, name, address, silent=False,
                 **kwargs):
        super().__init__(name, address, silent, **kwargs)
