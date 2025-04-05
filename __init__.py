from qcodes.utils.helpers import add_to_spyder_UMR_excludelist

# we dont want spyder to reload qcodes as this will overwrite the default station
# instrument list and running monitor
add_to_spyder_UMR_excludelist('qcodes-plusplus')
config = Config() # type: Config

from qcodes import *
from qcodes.parameters import ElapsedTimeParameter

from .version import __version__

from .loops import Loop, active_loop, active_data_set, param_move
from .measure import Measure
from .actions import Task, Wait, BreakIf

from .plots.qplot.RemotePlot import Plot
from .data.data_set import DataSet, new_data, load_data, load_data_num, load_data_nums, set_data_format, set_data_folder
from .data.location import FormatLocation
from .data.data_array import DataArray
from .data.format import Formatter
from .data.gnuplot_format import GNUPlotFormat
from .data.hdf5_format import HDF5Format
from .data.io import DiskIO

from .parameters import Parameter,MultiParameterWrapper, ArrayParameterWrapper


# ensure to close all instruments when interpreter is closed
import atexit
atexit.register(Instrument.close_all)
