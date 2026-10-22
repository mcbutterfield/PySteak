DifferentialCorrectorResultCollection
=====================================

.. py:class:: br.ok.core.stkobjects.astrogator.DifferentialCorrectorResultCollection

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The collection of results for a differential corrector.

.. py:currentmodule:: DifferentialCorrectorResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.get_result_by_paths`
              - Return the result specified by the object/result path.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.item`
              - Allow you to iterate through the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DifferentialCorrectorResultCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.count`
              - Return the size of the collection.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.provide_runtime_type_info`
              - Return the RuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import DifferentialCorrectorResultCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.ok.core.stkobjects.astrogator.DifferentialCorrectorResultCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: br.ok.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.count
    :type: int

    Return the size of the collection.

.. py:property:: provide_runtime_type_info
    :canonical: br.ok.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.provide_runtime_type_info
    :type: RuntimeTypeInfo

    Return the RuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------


.. py:method:: get_result_by_paths(self, object_path: str, result_path: str) -> DifferentialCorrectorResult
    :canonical: br.ok.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.get_result_by_paths

    Return the result specified by the object/result path.

    :Parameters:

        **object_path** : :obj:`~str`

        **result_path** : :obj:`~str`


    :Returns:

        :obj:`~DifferentialCorrectorResult`

.. py:method:: item(self, index: int) -> DifferentialCorrectorResult
    :canonical: br.ok.core.stkobjects.astrogator.DifferentialCorrectorResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~DifferentialCorrectorResult`



