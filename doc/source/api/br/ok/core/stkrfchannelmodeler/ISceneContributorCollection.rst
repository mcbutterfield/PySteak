ISceneContributorCollection
===========================

.. py:class:: br.ok.core.stkrfchannelmodeler.ISceneContributorCollection

   Represents a collection of scene contributors.

.. py:currentmodule:: ISceneContributorCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.add_new`
              - Add and returns a new scene contributor.
            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.contains`
              - Check to see if a given scene contributor exists in the collection.
            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.item`
              - Given an index, returns the element in the collection.
            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.remove`
              - Remove the supplied scene contributor from the collection.
            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.remove_all`
              - Clear all scene contributors from the collection.
            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.remove_at`
              - Remove the scene contributor with the supplied index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.ISceneContributorCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.count`
              - Return the number of elements in the collection.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkrfchannelmodeler import ISceneContributorCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkrfchannelmodeler.ISceneContributorCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------

.. py:method:: add_new(self, stk_object_path: str) -> SceneContributor
    :canonical: br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.add_new

    Add and returns a new scene contributor.

    :Parameters:

        **stk_object_path** : :obj:`~str`


    :Returns:

        :obj:`~SceneContributor`

.. py:method:: contains(self, stk_object_path: str) -> bool
    :canonical: br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.contains

    Check to see if a given scene contributor exists in the collection.

    :Parameters:

        **stk_object_path** : :obj:`~str`


    :Returns:

        :obj:`~bool`


.. py:method:: item(self, index: int) -> SceneContributor
    :canonical: br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~SceneContributor`

.. py:method:: remove(self, stk_object_path: str) -> None
    :canonical: br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.remove

    Remove the supplied scene contributor from the collection.

    :Parameters:

        **stk_object_path** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.remove_all

    Clear all scene contributors from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_at(self, index: int) -> None
    :canonical: br.ok.core.stkrfchannelmodeler.ISceneContributorCollection.remove_at

    Remove the scene contributor with the supplied index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


