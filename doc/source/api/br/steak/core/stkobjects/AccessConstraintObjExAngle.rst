AccessConstraintObjExAngle
==========================

.. py:class:: br.steak.core.stkobjects.AccessConstraintObjExAngle

   Bases: :py:class:`~br.steak.core.stkobjects.IAccessConstraint`

   Class defining the Object Exclusion Angle constraint.

.. py:currentmodule:: AccessConstraintObjExAngle

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintObjExAngle.add_exclusion_object`
              - Add an exclusion object.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintObjExAngle.is_object_assigned`
              - Return true if an exclusion object is assigned.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintObjExAngle.remove_exclusion_object`
              - Remove an exclusion object.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintObjExAngle.assigned_objects`
              - Return a safearray of assigned objects.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintObjExAngle.available_objects`
              - Return a safearray of available objects.
            * - :py:attr:`~br.steak.core.stkobjects.AccessConstraintObjExAngle.exclusion_angle`
              - Exclusion Angle value. Uses Angle Dimension.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AccessConstraintObjExAngle


Property detail
---------------

.. py:property:: assigned_objects
    :canonical: br.steak.core.stkobjects.AccessConstraintObjExAngle.assigned_objects
    :type: list

    Return a safearray of assigned objects.

.. py:property:: available_objects
    :canonical: br.steak.core.stkobjects.AccessConstraintObjExAngle.available_objects
    :type: list

    Return a safearray of available objects.

.. py:property:: exclusion_angle
    :canonical: br.steak.core.stkobjects.AccessConstraintObjExAngle.exclusion_angle
    :type: typing.Any

    Exclusion Angle value. Uses Angle Dimension.


Method detail
-------------

.. py:method:: add_exclusion_object(self, object_name: str) -> None
    :canonical: br.steak.core.stkobjects.AccessConstraintObjExAngle.add_exclusion_object

    Add an exclusion object.

    :Parameters:

        **object_name** : :obj:`~str`


    :Returns:

        :obj:`~None`





.. py:method:: is_object_assigned(self, object_name: str) -> bool
    :canonical: br.steak.core.stkobjects.AccessConstraintObjExAngle.is_object_assigned

    Return true if an exclusion object is assigned.

    :Parameters:

        **object_name** : :obj:`~str`


    :Returns:

        :obj:`~bool`

.. py:method:: remove_exclusion_object(self, object_name: str) -> None
    :canonical: br.steak.core.stkobjects.AccessConstraintObjExAngle.remove_exclusion_object

    Remove an exclusion object.

    :Parameters:

        **object_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

