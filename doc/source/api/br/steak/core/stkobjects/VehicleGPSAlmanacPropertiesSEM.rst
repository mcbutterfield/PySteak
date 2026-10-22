VehicleGPSAlmanacPropertiesSEM
==============================

.. py:class:: br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM

   Bases: :py:class:`~br.steak.core.stkobjects.IVehicleGPSAlmanacProperties`

   SEM almanac properties.

.. py:currentmodule:: VehicleGPSAlmanacPropertiesSEM

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM.almanac_week`
              - Get the week number from the reference week.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM.avg_ura`
              - Get the satellite 'average' URA number, with the URA number as defined in the ICD-GPS-200. This is not an item in the raw almanac file, but is based on the average URA value transmitted by this satellite in its subframe 1 data sets.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM.date_of_almanac`
              - Get the almanac reference date for all almanacs in the file per ICD-GPS-200.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM.health`
              - Get the satellite health code as defined in the ICD-GPS-200 expressed in integer form. 0=healthy.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM.reference_week`
              - Get or set the almanac reference week (VINA) for all almanacs in this file per the ICD-GPS-200.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM.time_of_almanac`
              - Get the almanac reference time (Time of Appilcability) for all almanacs in the file per ICD-GPS-200.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleGPSAlmanacPropertiesSEM


Property detail
---------------

.. py:property:: almanac_week
    :canonical: br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM.almanac_week
    :type: int

    Get the week number from the reference week.

.. py:property:: avg_ura
    :canonical: br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM.avg_ura
    :type: int

    Get the satellite 'average' URA number, with the URA number as defined in the ICD-GPS-200. This is not an item in the raw almanac file, but is based on the average URA value transmitted by this satellite in its subframe 1 data sets.

.. py:property:: date_of_almanac
    :canonical: br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM.date_of_almanac
    :type: str

    Get the almanac reference date for all almanacs in the file per ICD-GPS-200.

.. py:property:: health
    :canonical: br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM.health
    :type: int

    Get the satellite health code as defined in the ICD-GPS-200 expressed in integer form. 0=healthy.

.. py:property:: reference_week
    :canonical: br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM.reference_week
    :type: GPSReferenceWeek

    Get or set the almanac reference week (VINA) for all almanacs in this file per the ICD-GPS-200.

.. py:property:: time_of_almanac
    :canonical: br.steak.core.stkobjects.VehicleGPSAlmanacPropertiesSEM.time_of_almanac
    :type: float

    Get the almanac reference time (Time of Appilcability) for all almanacs in the file per ICD-GPS-200.


