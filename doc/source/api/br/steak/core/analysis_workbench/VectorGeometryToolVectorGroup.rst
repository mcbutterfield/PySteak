VectorGeometryToolVectorGroup
=============================

.. py:class:: br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup

   Access or create VGT vectors associated with an object or a central body.

.. py:currentmodule:: VectorGeometryToolVectorGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.get_item_by_index`
              - Retrieve a vector from the collection by index.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.get_item_by_name`
              - Retrieve a vector from the collection by name.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.item`
              - Return a vector by name or at a specified position.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.remove`
              - Remove a specified vector.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup._new_enum`
              - Return a COM enumerator.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.context`
              - Return a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.count`
              - Return a number of elements in the group.
            * - :py:attr:`~br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.factory`
              - Return a Factory object used to create custom vectors.



Import detail
-------------

.. code-block:: python

    from br.steak.core.analysis_workbench import VectorGeometryToolVectorGroup


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup._new_enum
    :type: EnumeratorProxy

    Return a COM enumerator.

.. py:property:: context
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.context
    :type: IAnalysisWorkbenchComponentContext

    Return a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.count
    :type: int

    Return a number of elements in the group.

.. py:property:: factory
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.factory
    :type: VectorGeometryToolVectorFactory

    Return a Factory object used to create custom vectors.


Method detail
-------------

.. py:method:: contains(self, name: str) -> bool
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`




.. py:method:: get_item_by_index(self, index: int) -> IVectorGeometryToolVector
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.get_item_by_index

    Retrieve a vector from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: get_item_by_name(self, name: str) -> IVectorGeometryToolVector
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.get_item_by_name

    Retrieve a vector from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: item(self, index_or_name: typing.Any) -> IVectorGeometryToolVector
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.item

    Return a vector by name or at a specified position.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~IVectorGeometryToolVector`

.. py:method:: remove(self, vector_name: str) -> None
    :canonical: br.steak.core.analysis_workbench.VectorGeometryToolVectorGroup.remove

    Remove a specified vector.

    :Parameters:

        **vector_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


