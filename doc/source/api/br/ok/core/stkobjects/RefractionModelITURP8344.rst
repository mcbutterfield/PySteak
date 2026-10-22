RefractionModelITURP8344
========================

.. py:class:: br.ok.core.stkobjects.RefractionModelITURP8344

   ITU-R P.834-4.

.. py:currentmodule:: RefractionModelITURP8344

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.RefractionModelITURP8344.atmosphere_altitude`
              - Altitude of the atmosphere. Used to compute the knee bend point of the refracted path. Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.RefractionModelITURP8344.ceiling`
              - Refraction will be ignored if object altitude is higher than the ceiling. Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.RefractionModelITURP8344.knee_bend_factor`
              - Used to compute the distance to the knee bend point of the refracted path. Dimensionless.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import RefractionModelITURP8344


Property detail
---------------

.. py:property:: atmosphere_altitude
    :canonical: br.ok.core.stkobjects.RefractionModelITURP8344.atmosphere_altitude
    :type: float

    Altitude of the atmosphere. Used to compute the knee bend point of the refracted path. Uses Distance Dimension.

.. py:property:: ceiling
    :canonical: br.ok.core.stkobjects.RefractionModelITURP8344.ceiling
    :type: float

    Refraction will be ignored if object altitude is higher than the ceiling. Uses Distance Dimension.

.. py:property:: knee_bend_factor
    :canonical: br.ok.core.stkobjects.RefractionModelITURP8344.knee_bend_factor
    :type: float

    Used to compute the distance to the knee bend point of the refracted path. Dimensionless.


