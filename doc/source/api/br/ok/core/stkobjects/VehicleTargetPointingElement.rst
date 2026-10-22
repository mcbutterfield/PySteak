VehicleTargetPointingElement
============================

.. py:class:: br.ok.core.stkobjects.VehicleTargetPointingElement

   Target pointing data for target pointing attitude.

.. py:currentmodule:: VehicleTargetPointingElement

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingElement.reset_constrained_vector_reference`
              - Set the constrained vector reference to a default value. Returns true if succeeded, otherwise return false.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingElement.aligned_vector`
              - Get the aligned vector.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingElement.altitude`
              - Get the LLA position's altitude. Uses Distance Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingElement.available_constrained_vectors`
              - Return the available constrained vectors.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingElement.constrained_vector`
              - Get the constrained vector.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingElement.constrained_vector_reference`
              - Get or set the reference for the constrained vector.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingElement.intervals`
              - Return a list of scheduled time intervals for the current target.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingElement.latitude`
              - Get the LLA position's latitude. Uses Latitude Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingElement.longitude`
              - Get the LLA position's longitude. Uses Longitude Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleTargetPointingElement.target`
              - Get a reference to the targeted object.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleTargetPointingElement


Property detail
---------------

.. py:property:: aligned_vector
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingElement.aligned_vector
    :type: IDirection

    Get the aligned vector.

.. py:property:: altitude
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingElement.altitude
    :type: float

    Get the LLA position's altitude. Uses Distance Dimension.

.. py:property:: available_constrained_vectors
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingElement.available_constrained_vectors
    :type: list

    Return the available constrained vectors.

.. py:property:: constrained_vector
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingElement.constrained_vector
    :type: IDirection

    Get the constrained vector.

.. py:property:: constrained_vector_reference
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingElement.constrained_vector_reference
    :type: str

    Get or set the reference for the constrained vector.

.. py:property:: intervals
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingElement.intervals
    :type: VehicleTargetPointingIntervalCollection

    Return a list of scheduled time intervals for the current target.

.. py:property:: latitude
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingElement.latitude
    :type: float

    Get the LLA position's latitude. Uses Latitude Dimension.

.. py:property:: longitude
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingElement.longitude
    :type: float

    Get the LLA position's longitude. Uses Longitude Dimension.

.. py:property:: target
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingElement.target
    :type: LinkToObject

    Get a reference to the targeted object.


Method detail
-------------










.. py:method:: reset_constrained_vector_reference(self) -> bool
    :canonical: br.ok.core.stkobjects.VehicleTargetPointingElement.reset_constrained_vector_reference

    Set the constrained vector reference to a default value. Returns true if succeeded, otherwise return false.

    :Returns:

        :obj:`~bool`


