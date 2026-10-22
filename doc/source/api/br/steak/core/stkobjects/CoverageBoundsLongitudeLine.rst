CoverageBoundsLongitudeLine
===========================

.. py:class:: br.steak.core.stkobjects.CoverageBoundsLongitudeLine

   Bases: :py:class:`~br.steak.core.stkobjects.ICoverageBounds`

   Longitude Line:  Create a set of points along a single meridian, useful when the coverage is only expected to vary with latitude.

.. py:currentmodule:: CoverageBoundsLongitudeLine

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.CoverageBoundsLongitudeLine.longitude`
              - Longitude of the meridian defining the longitude line. Uses Longitude Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.CoverageBoundsLongitudeLine.maximum_latitude`
              - Maximum latitude used to define the longitude line. Uses Latitude Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.CoverageBoundsLongitudeLine.minimum_latitude`
              - Minimum latitude used to define the longitude line. Uses Latitude Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import CoverageBoundsLongitudeLine


Property detail
---------------

.. py:property:: longitude
    :canonical: br.steak.core.stkobjects.CoverageBoundsLongitudeLine.longitude
    :type: typing.Any

    Longitude of the meridian defining the longitude line. Uses Longitude Dimension.

.. py:property:: maximum_latitude
    :canonical: br.steak.core.stkobjects.CoverageBoundsLongitudeLine.maximum_latitude
    :type: typing.Any

    Maximum latitude used to define the longitude line. Uses Latitude Dimension.

.. py:property:: minimum_latitude
    :canonical: br.steak.core.stkobjects.CoverageBoundsLongitudeLine.minimum_latitude
    :type: typing.Any

    Minimum latitude used to define the longitude line. Uses Latitude Dimension.


