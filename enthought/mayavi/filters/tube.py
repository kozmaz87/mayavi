# Author: Gael Varoquaux <gael.varoquaux@normalesup.org> 
# Copyright (c) 2007, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance
from enthought.tvtk.api import tvtk

# Local imports
from enthought.mayavi.filters.filter_base import FilterBase


######################################################################
# `Tube` class.
######################################################################
class Tube(FilterBase):

    """Turns lines into tubes.
    """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.TubeFilter, args=(), allow_none=False)

