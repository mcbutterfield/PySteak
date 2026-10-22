IRadarAnalysisConfigurationModel
================================

.. py:class:: br.steak.core.stkrfchannelmodeler.IRadarAnalysisConfigurationModel

   Properties for an analysis configuration model for a radar analysis. This contains a collection of the transceiver configurations belonging to the radar analysis.

.. py:currentmodule:: IRadarAnalysisConfigurationModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.IRadarAnalysisConfigurationModel.imaging_data_product_list`
              - Get the imaging product list.
            * - :py:attr:`~br.steak.core.stkrfchannelmodeler.IRadarAnalysisConfigurationModel.transceiver_configuration_collection`
              - Get the collection of transceiver configurations.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkrfchannelmodeler import IRadarAnalysisConfigurationModel


Property detail
---------------

.. py:property:: imaging_data_product_list
    :canonical: br.steak.core.stkrfchannelmodeler.IRadarAnalysisConfigurationModel.imaging_data_product_list
    :type: RadarImagingDataProductCollection

    Get the imaging product list.

.. py:property:: transceiver_configuration_collection
    :canonical: br.steak.core.stkrfchannelmodeler.IRadarAnalysisConfigurationModel.transceiver_configuration_collection
    :type: RadarTransceiverConfigurationCollection

    Get the collection of transceiver configurations.


