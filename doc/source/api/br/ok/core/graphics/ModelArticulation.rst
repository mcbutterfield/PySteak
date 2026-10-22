ModelArticulation
=================

.. py:class:: br.ok.core.graphics.ModelArticulation

   A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

.. py:currentmodule:: ModelArticulation

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.ModelArticulation.contains`
              - Return true if the collection contains the transformation.
            * - :py:attr:`~br.ok.core.graphics.ModelArticulation.get_by_name`
              - Get a transformation by name.
            * - :py:attr:`~br.ok.core.graphics.ModelArticulation.get_item_by_string`
              - Get a transformation by name.
            * - :py:attr:`~br.ok.core.graphics.ModelArticulation.item`
              - Get the transformation at the given index. The index is zero-based.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.ModelArticulation._new_enum`
              - Return the enumerator for this collection.
            * - :py:attr:`~br.ok.core.graphics.ModelArticulation.count`
              - Get the number of transformations in the collection.
            * - :py:attr:`~br.ok.core.graphics.ModelArticulation.name`
              - Get the name of the articulation.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import ModelArticulation


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.graphics.ModelArticulation._new_enum
    :type: EnumeratorProxy

    Return the enumerator for this collection.

.. py:property:: count
    :canonical: br.ok.core.graphics.ModelArticulation.count
    :type: int

    Get the number of transformations in the collection.

.. py:property:: name
    :canonical: br.ok.core.graphics.ModelArticulation.name
    :type: str

    Get the name of the articulation.


Method detail
-------------

.. py:method:: contains(self, name: str) -> bool
    :canonical: br.ok.core.graphics.ModelArticulation.contains

    Return true if the collection contains the transformation.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`


.. py:method:: get_by_name(self, name: str) -> ModelTransformation
    :canonical: br.ok.core.graphics.ModelArticulation.get_by_name

    Get a transformation by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ModelTransformation`

.. py:method:: get_item_by_string(self, name: str) -> ModelTransformation
    :canonical: br.ok.core.graphics.ModelArticulation.get_item_by_string

    Get a transformation by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ModelTransformation`

.. py:method:: item(self, index: int) -> ModelTransformation
    :canonical: br.ok.core.graphics.ModelArticulation.item

    Get the transformation at the given index. The index is zero-based.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ModelTransformation`



