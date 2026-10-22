SceneCollection
===============

.. py:class:: br.steak.core.graphics.SceneCollection

   A collection of scenes.

.. py:currentmodule:: SceneCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.SceneCollection.item`
              - Return a scene in the collection at a specified index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.SceneCollection._new_enum`
              - Return an enumerator that iterates through the collection.
            * - :py:attr:`~br.steak.core.graphics.SceneCollection.count`
              - Total number of scenes in the collection.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import SceneCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.graphics.SceneCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that iterates through the collection.

.. py:property:: count
    :canonical: br.steak.core.graphics.SceneCollection.count
    :type: int

    Total number of scenes in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> Scene
    :canonical: br.steak.core.graphics.SceneCollection.item

    Return a scene in the collection at a specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~Scene`


