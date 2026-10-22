ClassicalSizeShapeAltitude
==========================

.. py:class:: br.ok.core.stkobjects.ClassicalSizeShapeAltitude

   Bases: :py:class:`~br.ok.core.stkobjects.IClassicalSizeShape`

   Orbit size and shape using altitude.

.. py:currentmodule:: ClassicalSizeShapeAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.ClassicalSizeShapeAltitude.apogee_altitude`
              - Measured from the 'surface' of the Earth to the point of maximum radius in the orbit. For this value, the surface of the Earth is modeled as a sphere whose radius equals the equatorial radius of the Earth. Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.ClassicalSizeShapeAltitude.perigee_altitude`
              - Measured from the 'surface' of the Earth to the point of minimum radius in the orbit. For this value, the surface of the Earth is modeled as a sphere whose radius equals the equatorial radius of the Earth. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import ClassicalSizeShapeAltitude


Property detail
---------------

.. py:property:: apogee_altitude
    :canonical: br.ok.core.stkobjects.ClassicalSizeShapeAltitude.apogee_altitude
    :type: float

    Measured from the 'surface' of the Earth to the point of maximum radius in the orbit. For this value, the surface of the Earth is modeled as a sphere whose radius equals the equatorial radius of the Earth. Uses Distance Dimension.

.. py:property:: perigee_altitude
    :canonical: br.ok.core.stkobjects.ClassicalSizeShapeAltitude.perigee_altitude
    :type: float

    Measured from the 'surface' of the Earth to the point of minimum radius in the orbit. For this value, the surface of the Earth is modeled as a sphere whose radius equals the equatorial radius of the Earth. Uses Distance Dimension.


