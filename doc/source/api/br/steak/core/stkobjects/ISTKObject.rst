ISTKObject
==========

.. py:class:: br.steak.core.stkobjects.ISTKObject

   Represents the instance of STK object.

.. py:currentmodule:: ISTKObject

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.copy_object`
              - Copy and paste the current instance of STK Object. The copied object will be pasted as the sibling of the instance being copied.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.create_one_point_access`
              - Create one point access to the supplied object name. The Remove method in OnePointAccess should be called when you are done with the data.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.export`
              - Export the object to a file.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.get_access`
              - Return an Access object associated with this STK object and another STK object specified using its path. The path can be fully-qualified or truncated.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.get_access_to_object`
              - Return an Access object associated with this STK object and another STK object.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.is_access_supported`
              - Determine whether or not the object supports Access.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.is_color_supported`
              - Determine whether or not the object supports setting color.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.is_object_coverage_supported`
              - Determine whether or not the object supports ObjectCoverage.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.supports_analysis_workbench`
              - Return whether the object supports Vector Geometry.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.is_visibility_supported`
              - Determine whether or not the object supports setting graphics visibility.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.unload`
              - Remove the object from the scenario.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.access_constraints`
              - Get the constraints imposed on the object.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.analysis_workbench_components`
              - Return an instance of Vector Geometry Tool provider.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.central_body_name`
              - The object's central body.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.children`
              - Return a collection of direct descendants of the current object.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.class_name`
              - Return a class name of the object (i.e. Aircraft, Facility.).
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.class_type`
              - Return a class type of the object (i.e. eAircraft, eFacility etc.).
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.color`
              - The object's color.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.data_providers`
              - Return the object representing a list of available data providers for the object.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.has_children`
              - Return true if the object has direct descendants.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.instance_name`
              - A name of the object.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.long_description`
              - A long description of the object.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.metadata`
              - Get the object's metadata. Metadata is a collection of keys and their associated values.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.object_coverage`
              - Return an ObjectCoverage object.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.object_files`
              - Return the list of files that constitute an object.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.parent`
              - Return the parent object or null if the object has become orphaned. The exception is STKObjectRoot object which is a topmost element and does not have a parent.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.path`
              - Return the object path.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.root`
              - Return the Root object or null.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.short_description`
              - The short description of the object.
            * - :py:attr:`~br.steak.core.stkobjects.ISTKObject.show_object`
              - Whether the object is visible.


Examples
--------

Create a New AdvCAT Object

.. code-block:: python

    # Scenario scenario: Scenario object
    advCAT = scenario.children.new(STKObjectType.ADVCAT, "MyAdvCAT")


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ISTKObject


Property detail
---------------

.. py:property:: access_constraints
    :canonical: br.steak.core.stkobjects.ISTKObject.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the object.

.. py:property:: analysis_workbench_components
    :canonical: br.steak.core.stkobjects.ISTKObject.analysis_workbench_components
    :type: IAnalysisWorkbenchComponentProvider

    Return an instance of Vector Geometry Tool provider.

.. py:property:: central_body_name
    :canonical: br.steak.core.stkobjects.ISTKObject.central_body_name
    :type: str

    The object's central body.

.. py:property:: children
    :canonical: br.steak.core.stkobjects.ISTKObject.children
    :type: ISTKObjectCollection

    Return a collection of direct descendants of the current object.

.. py:property:: class_name
    :canonical: br.steak.core.stkobjects.ISTKObject.class_name
    :type: str

    Return a class name of the object (i.e. Aircraft, Facility.).

.. py:property:: class_type
    :canonical: br.steak.core.stkobjects.ISTKObject.class_type
    :type: STKObjectType

    Return a class type of the object (i.e. eAircraft, eFacility etc.).

.. py:property:: color
    :canonical: br.steak.core.stkobjects.ISTKObject.color
    :type: Color

    The object's color.

.. py:property:: data_providers
    :canonical: br.steak.core.stkobjects.ISTKObject.data_providers
    :type: DataProviderCollection

    Return the object representing a list of available data providers for the object.

.. py:property:: has_children
    :canonical: br.steak.core.stkobjects.ISTKObject.has_children
    :type: bool

    Return true if the object has direct descendants.

.. py:property:: instance_name
    :canonical: br.steak.core.stkobjects.ISTKObject.instance_name
    :type: str

    A name of the object.

.. py:property:: long_description
    :canonical: br.steak.core.stkobjects.ISTKObject.long_description
    :type: str

    A long description of the object.

.. py:property:: metadata
    :canonical: br.steak.core.stkobjects.ISTKObject.metadata
    :type: KeyValueCollection

    Get the object's metadata. Metadata is a collection of keys and their associated values.

.. py:property:: object_coverage
    :canonical: br.steak.core.stkobjects.ISTKObject.object_coverage
    :type: ObjectCoverage

    Return an ObjectCoverage object.

.. py:property:: object_files
    :canonical: br.steak.core.stkobjects.ISTKObject.object_files
    :type: list

    Return the list of files that constitute an object.

.. py:property:: parent
    :canonical: br.steak.core.stkobjects.ISTKObject.parent
    :type: ISTKObject

    Return the parent object or null if the object has become orphaned. The exception is STKObjectRoot object which is a topmost element and does not have a parent.

.. py:property:: path
    :canonical: br.steak.core.stkobjects.ISTKObject.path
    :type: str

    Return the object path.

.. py:property:: root
    :canonical: br.steak.core.stkobjects.ISTKObject.root
    :type: STKObjectRoot

    Return the Root object or null.

.. py:property:: short_description
    :canonical: br.steak.core.stkobjects.ISTKObject.short_description
    :type: str

    The short description of the object.

.. py:property:: show_object
    :canonical: br.steak.core.stkobjects.ISTKObject.show_object
    :type: bool

    Whether the object is visible.


Method detail
-------------








.. py:method:: copy_object(self, new_object_name: str) -> ISTKObject
    :canonical: br.steak.core.stkobjects.ISTKObject.copy_object

    Copy and paste the current instance of STK Object. The copied object will be pasted as the sibling of the instance being copied.

    :Parameters:

        **new_object_name** : :obj:`~str`


    :Returns:

        :obj:`~ISTKObject`

.. py:method:: create_one_point_access(self, path_to_object: str) -> OnePointAccess
    :canonical: br.steak.core.stkobjects.ISTKObject.create_one_point_access

    Create one point access to the supplied object name. The Remove method in OnePointAccess should be called when you are done with the data.

    :Parameters:

        **path_to_object** : :obj:`~str`


    :Returns:

        :obj:`~OnePointAccess`


.. py:method:: export(self, filename: str) -> None
    :canonical: br.steak.core.stkobjects.ISTKObject.export

    Export the object to a file.

    :Parameters:

        **filename** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: get_access(self, object_path: str) -> Access
    :canonical: br.steak.core.stkobjects.ISTKObject.get_access

    Return an Access object associated with this STK object and another STK object specified using its path. The path can be fully-qualified or truncated.

    :Parameters:

        **object_path** : :obj:`~str`


    :Returns:

        :obj:`~Access`

.. py:method:: get_access_to_object(self, object: ISTKObject) -> Access
    :canonical: br.steak.core.stkobjects.ISTKObject.get_access_to_object

    Return an Access object associated with this STK object and another STK object.

    :Parameters:

        **object** : :obj:`~ISTKObject`


    :Returns:

        :obj:`~Access`




.. py:method:: is_access_supported(self) -> bool
    :canonical: br.steak.core.stkobjects.ISTKObject.is_access_supported

    Determine whether or not the object supports Access.

    :Returns:

        :obj:`~bool`

.. py:method:: is_color_supported(self) -> bool
    :canonical: br.steak.core.stkobjects.ISTKObject.is_color_supported

    Determine whether or not the object supports setting color.

    :Returns:

        :obj:`~bool`

.. py:method:: is_object_coverage_supported(self) -> bool
    :canonical: br.steak.core.stkobjects.ISTKObject.is_object_coverage_supported

    Determine whether or not the object supports ObjectCoverage.

    :Returns:

        :obj:`~bool`



.. py:method:: supports_analysis_workbench(self) -> bool
    :canonical: br.steak.core.stkobjects.ISTKObject.supports_analysis_workbench

    Return whether the object supports Vector Geometry.

    :Returns:

        :obj:`~bool`

.. py:method:: is_visibility_supported(self) -> bool
    :canonical: br.steak.core.stkobjects.ISTKObject.is_visibility_supported

    Determine whether or not the object supports setting graphics visibility.

    :Returns:

        :obj:`~bool`











.. py:method:: unload(self) -> None
    :canonical: br.steak.core.stkobjects.ISTKObject.unload

    Remove the object from the scenario.

    :Returns:

        :obj:`~None`


