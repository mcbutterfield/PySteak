AccessConstraintPluginMinMax
============================

.. py:class:: br.steak.core.stkobjects.AccessConstraintPluginMinMax

   Bases: :py:class:`~br.steak.core.stkobjects.IAccessConstraintMinMaxBase`, :py:class:`~br.steak.core.stkobjects.IAccessConstraint`

   Class related to defining access plugin constraints in terms of minimum and/or maximum values.

.. py:currentmodule:: AccessConstraintPluginMinMax

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintPluginMinMax.get_property`
              - Get a property.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintPluginMinMax.get_raw_plugin_object`
              - Return a raw pointer to the access plugin constraint.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintPluginMinMax.set_property`
              - Set a property.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintPluginMinMax.available_properties`
              - Available properties.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AccessConstraintPluginMinMax


Property detail
---------------

.. py:property:: available_properties
    :canonical: br.steak.core.stkobjects.AccessConstraintPluginMinMax.available_properties
    :type: list

    Available properties.


Method detail
-------------


.. py:method:: get_property(self, path: str) -> typing.Any
    :canonical: br.steak.core.stkobjects.AccessConstraintPluginMinMax.get_property

    Get a property.

    :Parameters:

        **path** : :obj:`~str`


    :Returns:

        :obj:`~typing.Any`

.. py:method:: get_raw_plugin_object(self) -> typing.Any
    :canonical: br.steak.core.stkobjects.AccessConstraintPluginMinMax.get_raw_plugin_object

    Return a raw pointer to the access plugin constraint.

    :Returns:

        :obj:`~typing.Any`

.. py:method:: set_property(self, path: str, value: typing.Any) -> None
    :canonical: br.steak.core.stkobjects.AccessConstraintPluginMinMax.set_property

    Set a property.

    :Parameters:

        **path** : :obj:`~str`

        **value** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

