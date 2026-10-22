DataProviderResult
==================

.. py:class:: br.ok.core.stkobjects.DataProviderResult

   Results returned by the data provider.

.. py:currentmodule:: DataProviderResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResult.category`
              - Return a value representing the category of the result.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResult.data_sets`
              - Return a collection of Datasets.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResult.intervals`
              - Return a collection of intervals.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResult.message`
              - Return the message returned with the result.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResult.sections`
              - Return a collection of sections.
            * - :py:attr:`~br.ok.core.stkobjects.DataProviderResult.value`
              - Return the reference to the object containing the actual results returned by the data provider. The type of the object returned depends on the category. The categories currently defined are: Interval, SubSection and TextMessage.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import DataProviderResult


Property detail
---------------

.. py:property:: category
    :canonical: br.ok.core.stkobjects.DataProviderResult.category
    :type: DataProviderResultCategory

    Return a value representing the category of the result.

.. py:property:: data_sets
    :canonical: br.ok.core.stkobjects.DataProviderResult.data_sets
    :type: DataProviderResultDataSetCollection

    Return a collection of Datasets.

.. py:property:: intervals
    :canonical: br.ok.core.stkobjects.DataProviderResult.intervals
    :type: DataProviderResultIntervalCollection

    Return a collection of intervals.

.. py:property:: message
    :canonical: br.ok.core.stkobjects.DataProviderResult.message
    :type: DataProviderResultTextMessage

    Return the message returned with the result.

.. py:property:: sections
    :canonical: br.ok.core.stkobjects.DataProviderResult.sections
    :type: DataProviderResultSubSectionCollection

    Return a collection of sections.

.. py:property:: value
    :canonical: br.ok.core.stkobjects.DataProviderResult.value
    :type: typing.Any

    Return the reference to the object containing the actual results returned by the data provider. The type of the object returned depends on the category. The categories currently defined are: Interval, SubSection and TextMessage.


