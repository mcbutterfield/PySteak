PickInfoData
============

.. py:class:: br.steak.core.stkx.PickInfoData

   Single mouse pick result.

.. py:currentmodule:: PickInfoData

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkx.PickInfoData.altitude`
              - Altitude of point clicked (if available).
            * - :py:attr:`~br.steak.core.stkx.PickInfoData.is_lat_lon_altitude_valid`
              - Indicate if the Lat/Lon/Alt properties are valid.
            * - :py:attr:`~br.steak.core.stkx.PickInfoData.is_object_path_valid`
              - Indicate if the ObjPath property is valid.
            * - :py:attr:`~br.steak.core.stkx.PickInfoData.latitude`
              - Latitude of point clicked (if available).
            * - :py:attr:`~br.steak.core.stkx.PickInfoData.longitude`
              - Longitude of point clicked (if available).
            * - :py:attr:`~br.steak.core.stkx.PickInfoData.object_path`
              - Path of the STK object picked if any (or empty string).



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkx import PickInfoData


Property detail
---------------

.. py:property:: altitude
    :canonical: br.steak.core.stkx.PickInfoData.altitude
    :type: float

    Altitude of point clicked (if available).

.. py:property:: is_lat_lon_altitude_valid
    :canonical: br.steak.core.stkx.PickInfoData.is_lat_lon_altitude_valid
    :type: bool

    Indicate if the Lat/Lon/Alt properties are valid.

.. py:property:: is_object_path_valid
    :canonical: br.steak.core.stkx.PickInfoData.is_object_path_valid
    :type: bool

    Indicate if the ObjPath property is valid.

.. py:property:: latitude
    :canonical: br.steak.core.stkx.PickInfoData.latitude
    :type: float

    Latitude of point clicked (if available).

.. py:property:: longitude
    :canonical: br.steak.core.stkx.PickInfoData.longitude
    :type: float

    Longitude of point clicked (if available).

.. py:property:: object_path
    :canonical: br.steak.core.stkx.PickInfoData.object_path
    :type: str

    Path of the STK object picked if any (or empty string).


