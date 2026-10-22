ClassicalSizeShapeSemimajorAxis
===============================

.. py:class:: br.ok.core.stkobjects.ClassicalSizeShapeSemimajorAxis

   Bases: :py:class:`~br.ok.core.stkobjects.IClassicalSizeShape`

   Orbit size and shape using Semimajor Axis and Eccentricity.

.. py:currentmodule:: ClassicalSizeShapeSemimajorAxis

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ClassicalSizeShapeSemimajorAxis.eccentricity`
              - Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.ClassicalSizeShapeSemimajorAxis.semi_major_axis`
              - Half the length of the major (longest) axis of the orbital ellipse. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import ClassicalSizeShapeSemimajorAxis


Property detail
---------------

.. py:property:: eccentricity
    :canonical: br.ok.core.stkobjects.ClassicalSizeShapeSemimajorAxis.eccentricity
    :type: float

    Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.

.. py:property:: semi_major_axis
    :canonical: br.ok.core.stkobjects.ClassicalSizeShapeSemimajorAxis.semi_major_axis
    :type: float

    Half the length of the major (longest) axis of the orbital ellipse. Uses Distance Dimension.


