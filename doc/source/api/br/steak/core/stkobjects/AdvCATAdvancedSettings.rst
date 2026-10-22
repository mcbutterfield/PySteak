AdvCATAdvancedSettings
======================

.. py:class:: br.steak.core.stkobjects.AdvCATAdvancedSettings

   AdvCAT advanced properties.

.. py:currentmodule:: AdvCATAdvancedSettings

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.allow_partial_ephemeris`
              - Flag to allow computation even when ephemeris does not completely overlap analysis interval.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.compute_on_load`
              - Flag to force compute on load.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.conjunction_type`
              - Mode for computing events involving conjunction TCA.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.correlation_filename`
              - Correlation File Path.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.cross_reference_database`
              - Cross Reference Database Path.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.ellipsoid_advanced_settings`
              - Get AdvCAT advanced ellipsoid properties.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.force_repropagation_on_load`
              - Flag to force repropagation on load.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.log_filename`
              - Name of the Log File.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.maximum_sample_step_size`
              - Maximum step size used in sampling.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.minimum_sample_step_size`
              - Minimum step size used in sampling.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.pre_filters`
              - Get AdvCAT filter settings.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.remove_secondary_by_ssc`
              - Remove from cosniseration any secondary whose SSC number is the same as the primary.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.show_message_in_message_viewer`
              - Flag to specify whether to write messages to message viewer.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.ssc_hard_body_radius_file`
              - SSC Reference File Path.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.use_correlation_file`
              - Flag to specify Use of Correlation File.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.use_cross_reference_database`
              - Flag to specify Use of Cross Reference Database.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.use_log_file`
              - Use the log file.
            * - :py:attr:`~br.steak.core.stkobjects.AdvCATAdvancedSettings.use_ssc_hard_body_radius_file`
              - Flag to specify Use of SSC Reference File.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AdvCATAdvancedSettings


Property detail
---------------

.. py:property:: allow_partial_ephemeris
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.allow_partial_ephemeris
    :type: bool

    Flag to allow computation even when ephemeris does not completely overlap analysis interval.

.. py:property:: compute_on_load
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.compute_on_load
    :type: bool

    Flag to force compute on load.

.. py:property:: conjunction_type
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.conjunction_type
    :type: AdvCATConjunctionType

    Mode for computing events involving conjunction TCA.

.. py:property:: correlation_filename
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.correlation_filename
    :type: str

    Correlation File Path.

.. py:property:: cross_reference_database
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.cross_reference_database
    :type: str

    Cross Reference Database Path.

.. py:property:: ellipsoid_advanced_settings
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.ellipsoid_advanced_settings
    :type: AdvCATAdvancedEllipsoid

    Get AdvCAT advanced ellipsoid properties.

.. py:property:: force_repropagation_on_load
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.force_repropagation_on_load
    :type: bool

    Flag to force repropagation on load.

.. py:property:: log_filename
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.log_filename
    :type: str

    Name of the Log File.

.. py:property:: maximum_sample_step_size
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.maximum_sample_step_size
    :type: float

    Maximum step size used in sampling.

.. py:property:: minimum_sample_step_size
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.minimum_sample_step_size
    :type: float

    Minimum step size used in sampling.

.. py:property:: pre_filters
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.pre_filters
    :type: AdvCATPreFilters

    Get AdvCAT filter settings.

.. py:property:: remove_secondary_by_ssc
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.remove_secondary_by_ssc
    :type: bool

    Remove from cosniseration any secondary whose SSC number is the same as the primary.

.. py:property:: show_message_in_message_viewer
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.show_message_in_message_viewer
    :type: bool

    Flag to specify whether to write messages to message viewer.

.. py:property:: ssc_hard_body_radius_file
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.ssc_hard_body_radius_file
    :type: str

    SSC Reference File Path.

.. py:property:: use_correlation_file
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.use_correlation_file
    :type: bool

    Flag to specify Use of Correlation File.

.. py:property:: use_cross_reference_database
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.use_cross_reference_database
    :type: bool

    Flag to specify Use of Cross Reference Database.

.. py:property:: use_log_file
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.use_log_file
    :type: bool

    Use the log file.

.. py:property:: use_ssc_hard_body_radius_file
    :canonical: br.steak.core.stkobjects.AdvCATAdvancedSettings.use_ssc_hard_body_radius_file
    :type: bool

    Flag to specify Use of SSC Reference File.


