
The ``stkrfchannelmodeler`` module
==================================


.. py:module:: br.ok.core.stkrfchannelmodeler


Summary
-------

.. tab-set::


    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~br.ok.core.stkrfchannelmodeler.IAnalysisConfigurationModel`
              - Base interface for all analysis configuration models.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.IAnalysisLink`
              - Properties for a transceiver link for an analysis.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.IAntenna`
              - Base interface for a transceiver antenna model.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.IProgressTrackCancel`
              - Control for progress tracker.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.IRadarAnalysisConfigurationModel`
              - Properties for an analysis configuration model for a radar analysis. This contains a collection of the transceiver configurations belonging to the radar analysis.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.IResponse`
              - Properties and data for a channel characaterization response.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.ISceneContributorCollection`
              - Represents a collection of scene contributors.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.ITransceiverModel`
              - Base interface which defines common properties for a transceiver model.


    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~br.ok.core.stkrfchannelmodeler.Analysis`
              - An RF Channel Modeler analysis.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.AnalysisConfiguration`
              - The configuration for an analysis.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.AnalysisConfigurationCollection`
              - A collection of analysis configurations.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.AnalysisLink`
              - A transceiver link for an analysis.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.AnalysisLinkCollection`
              - A collection of links between transceivers.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.CommunicationsAnalysisConfigurationModel`
              - The analysis configuration model for a communications analysis. This contains a collection of the transceiver configurations belonging to the communications analysis.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.CommunicationsTransceiverConfiguration`
              - The transceiver configuration for a communications transceiver.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.CommunicationsTransceiverConfigurationCollection`
              - A collection of communication transceivers.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.CommunicationsTransceiverModel`
              - The model for a communications transceiver.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.CommunicationsWaveform`
              - The waveform settings of a communications transceiver.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.ComputeOptions`
              - The options for computing RF Channel Modeler.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.ElementExportPatternAntenna`
              - The antenna settings for an element export pattern antenna.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.Extent`
              - The extent in which the channel characterizations will be computed.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.FacetTileset`
              - The facet tileset information.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.FacetTilesetCollection`
              - A collection of facet tilesets.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.FarFieldDataPatternAntenna`
              - The antenna settings for a far field data pattern antenna.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.FrequencyPulseResponse`
              - The response data and properties for a frequency pulse channel characterization.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.GpuProperties`
              - The properties of a GPU pertaining to RF Channel Modeler.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.Material`
              - A material for scene contributors.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.ParametricBeamAntenna`
              - The antenna settings for a parametric beam antenna.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarImagingDataProduct`
              - Imaging data product that facilitates the generation of range doppler radar images.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarImagingDataProductCollection`
              - A collection of radar transceivers.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarISarAnalysisConfigurationModel`
              - The analysis configuration model for an ISar analysis. This contains a collection of the transceiver configurations belonging to the ISar analysis.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarISarAnalysisLink`
              - A transceiver link for an ISar analysis.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarSarAnalysisConfigurationModel`
              - The analysis configuration model for a Sar analysis. This contains a collection of the transceiver configurations belonging to the Sar analysis.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarSarAnalysisLink`
              - A transceiver link for a Sar analysis.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarSarImageLocation`
              - The image location information for use by a range doppler Sar analysis.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarSarImageLocationCollection`
              - A collection of image location information.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarTargetCollection`
              - A collection of radar target objects.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarTransceiverConfiguration`
              - The transceiver configuration for a radar transceiver.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarTransceiverConfigurationCollection`
              - A collection of radar transceivers.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarTransceiverModel`
              - The model for a radar transceiver.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RadarWaveform`
              - The waveform settings of a radar transceiver.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.RangeDopplerResponse`
              - The response data and properties for a range doppler channel characterization.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.SceneContributor`
              - A scene contributor object.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.SceneContributorCollection`
              - A collection of scene contributor objects.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.STKRFChannelModeler`
              - The main RF Channel Modeler object.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.Transceiver`
              - The transceiver object and its settings.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.TransceiverCollection`
              - A collection of transceiver objects.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.ValidationResponse`
              - The response from validating an analysis configuration.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~br.ok.core.stkrfchannelmodeler.AnalysisConfigurationComputeStepMode`
              - Analysis configuration compute step mode.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.AnalysisConfigurationModelType`
              - Analysis Configuration Model Type

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.AnalysisResultsFileMode`
              - Analysis results file mode.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.AnalysisSolverBoundingBoxMode`
              - Analysis solver bounding box mode.

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.ChannelResponseType`
              - Channel Response Type

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.ImageWindowType`
              - Polarization Type

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.PolarizationType`
              - Polarization Type

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.TransceiverMode`
              - Transceiver Mode

            * - :py:class:`~br.ok.core.stkrfchannelmodeler.TransceiverModelType`
              - Transceiver Model Type



Description
-----------

Object Model components specifically designed to support STK RF Channel Modeler.


.. py:currentmodule:: br.ok.core.stkrfchannelmodeler


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     IAnalysisConfigurationModel<stkrfchannelmodeler/IAnalysisConfigurationModel>
     IAnalysisLink<stkrfchannelmodeler/IAnalysisLink>
     IAntenna<stkrfchannelmodeler/IAntenna>
     IProgressTrackCancel<stkrfchannelmodeler/IProgressTrackCancel>
     IRadarAnalysisConfigurationModel<stkrfchannelmodeler/IRadarAnalysisConfigurationModel>
     IResponse<stkrfchannelmodeler/IResponse>
     ISceneContributorCollection<stkrfchannelmodeler/ISceneContributorCollection>
     ITransceiverModel<stkrfchannelmodeler/ITransceiverModel>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     Analysis<stkrfchannelmodeler/Analysis>
     AnalysisConfiguration<stkrfchannelmodeler/AnalysisConfiguration>
     AnalysisConfigurationCollection<stkrfchannelmodeler/AnalysisConfigurationCollection>
     AnalysisLink<stkrfchannelmodeler/AnalysisLink>
     AnalysisLinkCollection<stkrfchannelmodeler/AnalysisLinkCollection>
     CommunicationsAnalysisConfigurationModel<stkrfchannelmodeler/CommunicationsAnalysisConfigurationModel>
     CommunicationsTransceiverConfiguration<stkrfchannelmodeler/CommunicationsTransceiverConfiguration>
     CommunicationsTransceiverConfigurationCollection<stkrfchannelmodeler/CommunicationsTransceiverConfigurationCollection>
     CommunicationsTransceiverModel<stkrfchannelmodeler/CommunicationsTransceiverModel>
     CommunicationsWaveform<stkrfchannelmodeler/CommunicationsWaveform>
     ComputeOptions<stkrfchannelmodeler/ComputeOptions>
     ElementExportPatternAntenna<stkrfchannelmodeler/ElementExportPatternAntenna>
     Extent<stkrfchannelmodeler/Extent>
     FacetTileset<stkrfchannelmodeler/FacetTileset>
     FacetTilesetCollection<stkrfchannelmodeler/FacetTilesetCollection>
     FarFieldDataPatternAntenna<stkrfchannelmodeler/FarFieldDataPatternAntenna>
     FrequencyPulseResponse<stkrfchannelmodeler/FrequencyPulseResponse>
     GpuProperties<stkrfchannelmodeler/GpuProperties>
     Material<stkrfchannelmodeler/Material>
     ParametricBeamAntenna<stkrfchannelmodeler/ParametricBeamAntenna>
     RadarImagingDataProduct<stkrfchannelmodeler/RadarImagingDataProduct>
     RadarImagingDataProductCollection<stkrfchannelmodeler/RadarImagingDataProductCollection>
     RadarISarAnalysisConfigurationModel<stkrfchannelmodeler/RadarISarAnalysisConfigurationModel>
     RadarISarAnalysisLink<stkrfchannelmodeler/RadarISarAnalysisLink>
     RadarSarAnalysisConfigurationModel<stkrfchannelmodeler/RadarSarAnalysisConfigurationModel>
     RadarSarAnalysisLink<stkrfchannelmodeler/RadarSarAnalysisLink>
     RadarSarImageLocation<stkrfchannelmodeler/RadarSarImageLocation>
     RadarSarImageLocationCollection<stkrfchannelmodeler/RadarSarImageLocationCollection>
     RadarTargetCollection<stkrfchannelmodeler/RadarTargetCollection>
     RadarTransceiverConfiguration<stkrfchannelmodeler/RadarTransceiverConfiguration>
     RadarTransceiverConfigurationCollection<stkrfchannelmodeler/RadarTransceiverConfigurationCollection>
     RadarTransceiverModel<stkrfchannelmodeler/RadarTransceiverModel>
     RadarWaveform<stkrfchannelmodeler/RadarWaveform>
     RangeDopplerResponse<stkrfchannelmodeler/RangeDopplerResponse>
     SceneContributor<stkrfchannelmodeler/SceneContributor>
     SceneContributorCollection<stkrfchannelmodeler/SceneContributorCollection>
     STKRFChannelModeler<stkrfchannelmodeler/STKRFChannelModeler>
     Transceiver<stkrfchannelmodeler/Transceiver>
     TransceiverCollection<stkrfchannelmodeler/TransceiverCollection>
     ValidationResponse<stkrfchannelmodeler/ValidationResponse>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ AnalysisConfigurationComputeStepMode<stkrfchannelmodeler/AnalysisConfigurationComputeStepMode>
    ≔ AnalysisConfigurationModelType<stkrfchannelmodeler/AnalysisConfigurationModelType>
    ≔ AnalysisResultsFileMode<stkrfchannelmodeler/AnalysisResultsFileMode>
    ≔ AnalysisSolverBoundingBoxMode<stkrfchannelmodeler/AnalysisSolverBoundingBoxMode>
    ≔ ChannelResponseType<stkrfchannelmodeler/ChannelResponseType>
    ≔ ImageWindowType<stkrfchannelmodeler/ImageWindowType>
    ≔ PolarizationType<stkrfchannelmodeler/PolarizationType>
    ≔ TransceiverMode<stkrfchannelmodeler/TransceiverMode>
    ≔ TransceiverModelType<stkrfchannelmodeler/TransceiverModelType>

