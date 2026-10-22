LinkToObject
============

.. py:class:: br.steak.core.stkobjects.LinkToObject

   Class defining a link to an STK object.

.. py:currentmodule:: LinkToObject

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.LinkToObject.bind_to_object`
              - Binds to existing object instance using the specified object path.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.LinkToObject.available_objects`
              - Return a list of available objects that can be linked to.
            * - :py:attr:`~br.steak.core.stkobjects.LinkToObject.is_intrinsic`
              - Return true if the link references an intrinsic object, otherwise returns false.
            * - :py:attr:`~br.steak.core.stkobjects.LinkToObject.linked_object`
              - Dereferences the link and returns the linked object.
            * - :py:attr:`~br.steak.core.stkobjects.LinkToObject.name`
              - Return a name of linked object.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import LinkToObject


Property detail
---------------

.. py:property:: available_objects
    :canonical: br.steak.core.stkobjects.LinkToObject.available_objects
    :type: list

    Return a list of available objects that can be linked to.

.. py:property:: is_intrinsic
    :canonical: br.steak.core.stkobjects.LinkToObject.is_intrinsic
    :type: bool

    Return true if the link references an intrinsic object, otherwise returns false.

.. py:property:: linked_object
    :canonical: br.steak.core.stkobjects.LinkToObject.linked_object
    :type: ISTKObject

    Dereferences the link and returns the linked object.

.. py:property:: name
    :canonical: br.steak.core.stkobjects.LinkToObject.name
    :type: str

    Return a name of linked object.


Method detail
-------------


.. py:method:: bind_to_object(self, path: str) -> ISTKObject
    :canonical: br.steak.core.stkobjects.LinkToObject.bind_to_object

    Binds to existing object instance using the specified object path.

    :Parameters:

        **path** : :obj:`~str`


    :Returns:

        :obj:`~ISTKObject`




