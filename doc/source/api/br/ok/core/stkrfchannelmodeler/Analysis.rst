Analysis
========

.. py:class:: br.ok.core.stkrfchannelmodeler.Analysis

   An RF Channel Modeler analysis.

.. py:currentmodule:: Analysis

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.Analysis.terminate`
              - Terminate the analysis and free resources. Calls to the Compute method of any IAnalysisLink instance, obtained from this analysis instance, after calling terminate, will fail.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkrfchannelmodeler.Analysis.analysis_link_collection`
              - Get the analysis link collection.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkrfchannelmodeler import Analysis


Property detail
---------------

.. py:property:: analysis_link_collection
    :canonical: br.ok.core.stkrfchannelmodeler.Analysis.analysis_link_collection
    :type: AnalysisLinkCollection

    Get the analysis link collection.


Method detail
-------------


.. py:method:: terminate(self) -> None
    :canonical: br.ok.core.stkrfchannelmodeler.Analysis.terminate

    Terminate the analysis and free resources. Calls to the Compute method of any IAnalysisLink instance, obtained from this analysis instance, after calling terminate, will fail.

    :Returns:

        :obj:`~None`

