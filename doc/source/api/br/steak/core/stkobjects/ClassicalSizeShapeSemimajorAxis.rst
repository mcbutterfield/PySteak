ClassicalSizeShapeSemimajorAxis
===============================

.. py:class:: br.steak.core.stkobjects.ClassicalSizeShapeSemimajorAxis

   Bases: :py:class:`~br.steak.core.stkobjects.IClassicalSizeShape`

   Orbit size and shape using Semimajor Axis and Eccentricity.

.. py:currentmodule:: ClassicalSizeShapeSemimajorAxis

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ClassicalSizeShapeSemimajorAxis.eccentricity`
              - Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.ClassicalSizeShapeSemimajorAxis.semi_major_axis`
              - Half the length of the major (longest) axis of the orbital ellipse. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ClassicalSizeShapeSemimajorAxis


Property detail
---------------

.. py:property:: eccentricity
    :canonical: br.steak.core.stkobjects.ClassicalSizeShapeSemimajorAxis.eccentricity
    :type: float

    Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.

.. py:property:: semi_major_axis
    :canonical: br.steak.core.stkobjects.ClassicalSizeShapeSemimajorAxis.semi_major_axis
    :type: float

    Half the length of the major (longest) axis of the orbital ellipse. Uses Distance Dimension.


