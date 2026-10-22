ClassicalSizeShapePeriod
========================

.. py:class:: br.steak.core.stkobjects.ClassicalSizeShapePeriod

   Bases: :py:class:`~br.steak.core.stkobjects.IClassicalSizeShape`

   Orbit size and shape using Period and Eccentricity.

.. py:currentmodule:: ClassicalSizeShapePeriod

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ClassicalSizeShapePeriod.eccentricity`
              - Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.ClassicalSizeShapePeriod.period`
              - Get or set the duration of one orbit, based on assumed two-body motion. Uses Time Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ClassicalSizeShapePeriod


Property detail
---------------

.. py:property:: eccentricity
    :canonical: br.steak.core.stkobjects.ClassicalSizeShapePeriod.eccentricity
    :type: float

    Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.

.. py:property:: period
    :canonical: br.steak.core.stkobjects.ClassicalSizeShapePeriod.period
    :type: float

    Get or set the duration of one orbit, based on assumed two-body motion. Uses Time Dimension.


