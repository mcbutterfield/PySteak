VehicleGraphics3DVelocityCovariance
===================================

.. py:class:: br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance

   3D velocity covariance ellipsoids.

.. py:currentmodule:: VehicleGraphics3DVelocityCovariance

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance.is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance.set_attributes_type`
              - Set the velocity ellipsoid attributes type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance.attributes`
              - Get the velocity ellipsoid graphics attributes.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance.attributes_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance.attributes_type`
              - Get the velocity ellipsoid attributes type.
            * - :py:attr:`~br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance.scale`
              - A scale value for the velocity ellipsoid size. Dimensionless.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import VehicleGraphics3DVelocityCovariance


Property detail
---------------

.. py:property:: attributes
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance.attributes
    :type: IVehicleGraphics3DAttributes

    Get the velocity ellipsoid graphics attributes.

.. py:property:: attributes_supported_types
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance.attributes_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: attributes_type
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance.attributes_type
    :type: VehicleGraphics3DAttributeType

    Get the velocity ellipsoid attributes type.

.. py:property:: scale
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance.scale
    :type: float

    A scale value for the velocity ellipsoid size. Dimensionless.


Method detail
-------------




.. py:method:: is_attributes_type_supported(self, attributes: VehicleGraphics3DAttributeType) -> bool
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics3DAttributeType`


    :Returns:

        :obj:`~bool`



.. py:method:: set_attributes_type(self, attributes: VehicleGraphics3DAttributeType) -> None
    :canonical: br.steak.core.stkobjects.VehicleGraphics3DVelocityCovariance.set_attributes_type

    Set the velocity ellipsoid attributes type.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics3DAttributeType`


    :Returns:

        :obj:`~None`

