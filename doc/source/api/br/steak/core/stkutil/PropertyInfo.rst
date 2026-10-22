PropertyInfo
============

.. py:class:: br.steak.core.stkutil.PropertyInfo

   Property Information coclass.

.. py:currentmodule:: PropertyInfo

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkutil.PropertyInfo.get_value`
              - Get the value of the property. Use PropertyType to determine the type to cast to.
            * - :py:attr:`~br.steak.core.stkutil.PropertyInfo.set_value`
              - Set the value of the property. Use PropertyType to determine the type to cast to.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkutil.PropertyInfo.has_max`
              - Determine if the property has a maximum value.
            * - :py:attr:`~br.steak.core.stkutil.PropertyInfo.has_min`
              - Determine if the property has a minimum value.
            * - :py:attr:`~br.steak.core.stkutil.PropertyInfo.max`
              - Get the maximum value of this property. Use PropertyType to determine the type to cast to.
            * - :py:attr:`~br.steak.core.stkutil.PropertyInfo.min`
              - Get the minimum value of this property. Use PropertyType to determine the type to cast to.
            * - :py:attr:`~br.steak.core.stkutil.PropertyInfo.name`
              - Get the name of the property.
            * - :py:attr:`~br.steak.core.stkutil.PropertyInfo.property_type`
              - Get the type of property.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkutil import PropertyInfo


Property detail
---------------

.. py:property:: has_max
    :canonical: br.steak.core.stkutil.PropertyInfo.has_max
    :type: bool

    Determine if the property has a maximum value.

.. py:property:: has_min
    :canonical: br.steak.core.stkutil.PropertyInfo.has_min
    :type: bool

    Determine if the property has a minimum value.

.. py:property:: max
    :canonical: br.steak.core.stkutil.PropertyInfo.max
    :type: typing.Any

    Get the maximum value of this property. Use PropertyType to determine the type to cast to.

.. py:property:: min
    :canonical: br.steak.core.stkutil.PropertyInfo.min
    :type: typing.Any

    Get the minimum value of this property. Use PropertyType to determine the type to cast to.

.. py:property:: name
    :canonical: br.steak.core.stkutil.PropertyInfo.name
    :type: str

    Get the name of the property.

.. py:property:: property_type
    :canonical: br.steak.core.stkutil.PropertyInfo.property_type
    :type: PropertyInfoValueType

    Get the type of property.


Method detail
-------------

.. py:method:: get_value(self) -> typing.Any
    :canonical: br.steak.core.stkutil.PropertyInfo.get_value

    Get the value of the property. Use PropertyType to determine the type to cast to.

    :Returns:

        :obj:`~typing.Any`







.. py:method:: set_value(self, property_info: typing.Any) -> None
    :canonical: br.steak.core.stkutil.PropertyInfo.set_value

    Set the value of the property. Use PropertyType to determine the type to cast to.

    :Parameters:

        **property_info** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

