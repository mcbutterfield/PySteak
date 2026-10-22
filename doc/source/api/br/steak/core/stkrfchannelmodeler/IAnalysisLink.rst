IAnalysisLink
=============

.. py:class:: br.steak.core.stkrfchannelmodeler.IAnalysisLink

   Properties for a transceiver link for an analysis.

.. py:currentmodule:: IAnalysisLink

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.IAnalysisLink.compute`
              - Compute the analysis link at the given time.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.IAnalysisLink.analysis_intervals`
              - Get the analysis intervals array.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.IAnalysisLink.name`
              - Get the analysis link name.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.IAnalysisLink.receive_antenna_count`
              - Get the receive antenna count.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.IAnalysisLink.receive_transceiver_identifier`
              - Get the receive transceiver identifier.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.IAnalysisLink.receive_transceiver_name`
              - Get the receive transceiver name.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.IAnalysisLink.transmit_antenna_count`
              - Get the transmit antenna count.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.IAnalysisLink.transmit_transceiver_identifier`
              - Get the transmit transceiver identifier.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.IAnalysisLink.transmit_transceiver_name`
              - Get the transmit transceiver name.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkrfchannelmodeler import IAnalysisLink


Property detail
---------------

.. py:property:: analysis_intervals
    :canonical: br.steak.core.stkrfchannelmodeler.IAnalysisLink.analysis_intervals
    :type: list

    Get the analysis intervals array.

.. py:property:: name
    :canonical: br.steak.core.stkrfchannelmodeler.IAnalysisLink.name
    :type: str

    Get the analysis link name.

.. py:property:: receive_antenna_count
    :canonical: br.steak.core.stkrfchannelmodeler.IAnalysisLink.receive_antenna_count
    :type: int

    Get the receive antenna count.

.. py:property:: receive_transceiver_identifier
    :canonical: br.steak.core.stkrfchannelmodeler.IAnalysisLink.receive_transceiver_identifier
    :type: str

    Get the receive transceiver identifier.

.. py:property:: receive_transceiver_name
    :canonical: br.steak.core.stkrfchannelmodeler.IAnalysisLink.receive_transceiver_name
    :type: str

    Get the receive transceiver name.

.. py:property:: transmit_antenna_count
    :canonical: br.steak.core.stkrfchannelmodeler.IAnalysisLink.transmit_antenna_count
    :type: int

    Get the transmit antenna count.

.. py:property:: transmit_transceiver_identifier
    :canonical: br.steak.core.stkrfchannelmodeler.IAnalysisLink.transmit_transceiver_identifier
    :type: str

    Get the transmit transceiver identifier.

.. py:property:: transmit_transceiver_name
    :canonical: br.steak.core.stkrfchannelmodeler.IAnalysisLink.transmit_transceiver_name
    :type: str

    Get the transmit transceiver name.


Method detail
-------------


.. py:method:: compute(self, time: float) -> IResponse
    :canonical: br.steak.core.stkrfchannelmodeler.IAnalysisLink.compute

    Compute the analysis link at the given time.

    :Parameters:

        **time** : :obj:`~float`


    :Returns:

        :obj:`~IResponse`








