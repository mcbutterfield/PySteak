ClassicalSizeShapeMeanMotion
============================

.. py:class:: br.steak.core.stkobjects.ClassicalSizeShapeMeanMotion

   Bases: :py:class:`~br.steak.core.stkobjects.IClassicalSizeShape`

   Orbit size and shape using Mean Motion and Eccentricity.

.. py:currentmodule:: ClassicalSizeShapeMeanMotion

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ClassicalSizeShapeMeanMotion.eccentricity`
              - Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.ClassicalSizeShapeMeanMotion.mean_motion`
              - Identifies the number of orbits per day (86400 sec/period), based on assumed two-body motion. Uses AngleRate Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ClassicalSizeShapeMeanMotion


Property detail
---------------

.. py:property:: eccentricity
    :canonical: br.steak.core.stkobjects.ClassicalSizeShapeMeanMotion.eccentricity
    :type: float

    Describes the shape of the ellipse (a real number >= 0 and <1, where 0 = a circular orbit). Dimensionless.

.. py:property:: mean_motion
    :canonical: br.steak.core.stkobjects.ClassicalSizeShapeMeanMotion.mean_motion
    :type: float

    Identifies the number of orbits per day (86400 sec/period), based on assumed two-body motion. Uses AngleRate Dimension.


