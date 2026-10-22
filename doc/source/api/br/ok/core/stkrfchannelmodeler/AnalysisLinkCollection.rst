AnalysisLinkCollection
======================

.. py:class:: br.ok.core.stkrfchannelmodeler.AnalysisLinkCollection

   A collection of links between transceivers.

.. py:currentmodule:: AnalysisLinkCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.AnalysisLinkCollection.item`
              - Given an index, returns the element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.AnalysisLinkCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.AnalysisLinkCollection.count`
              - Return the number of elements in the collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkrfchannelmodeler import AnalysisLinkCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkrfchannelmodeler.AnalysisLinkCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: count
    :canonical: br.ok.core.stkrfchannelmodeler.AnalysisLinkCollection.count
    :type: int

    Return the number of elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IAnalysisLink
    :canonical: br.ok.core.stkrfchannelmodeler.AnalysisLinkCollection.item

    Given an index, returns the element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IAnalysisLink`


