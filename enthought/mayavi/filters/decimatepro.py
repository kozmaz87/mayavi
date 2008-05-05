# Author: Gael Varoquaux <gael _dot_ varoquaux _at_ normalesup _dot_ org> 
# Copyright (c) 2008, Enthought, Inc.
# License: BSD Style.

# Enthought library imports.
from enthought.traits.api import Instance
from enthought.tvtk.api import tvtk

# Local imports
from enthought.mayavi.filters.filter_base import FilterBase


######################################################################
# `DecimatePro` class.
######################################################################
class DecimatePro(FilterBase):

    """ Reduces the number of triangles in a mesh using the
        tvtk.DecimatePro class. """

    # The version of this class.  Used for persistence.
    __version__ = 0

    # The actual TVTK filter that this class manages.
    filter = Instance(tvtk.DecimatePro, args=(), allow_none=False)

