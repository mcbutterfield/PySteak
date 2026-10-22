ObjectCoverage
==============

.. py:class:: br.steak.core.stkobjects.ObjectCoverage

   Class defining object coverage.

.. py:currentmodule:: ObjectCoverage

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ObjectCoverage.clear`
              - Remove the computation on the object coverage.
            * - :py:attr:`~br.steak.core.stkobjects.ObjectCoverage.clear_coverage`
              - Clear object coverage.
            * - :py:attr:`~br.steak.core.stkobjects.ObjectCoverage.compute`
              - Compute the object coverage.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ObjectCoverage.access_interval`
              - The object coverage's access interval.
            * - :py:attr:`~br.steak.core.stkobjects.ObjectCoverage.assets`
              - Get the asset list collection.
            * - :py:attr:`~br.steak.core.stkobjects.ObjectCoverage.data_providers`
              - Return the object representing a list of available data providers for the object.
            * - :py:attr:`~br.steak.core.stkobjects.ObjectCoverage.figure_of_merit`
              - Get the figure of merit on the object coverage.
            * - :py:attr:`~br.steak.core.stkobjects.ObjectCoverage.is_coverage_configuration_saved`
              - Save the single-object coverage definitions when the scenario is saved to disk, if a compute has been done.
            * - :py:attr:`~br.steak.core.stkobjects.ObjectCoverage.start_time`
              - Get or set the start time of object coverage. Uses DateFormat Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.ObjectCoverage.stop_time`
              - Get or set the stop time of object coverage. Uses DateFormat Dimension.
            * - :py:attr:`~br.steak.core.stkobjects.ObjectCoverage.use_object_times`
              - Use object interval times.



Examples
--------

Compute Object Coverage

.. code-block:: python

    # Aircraft aircraft: Aircraft object
    objCoverage = aircraft.object_coverage
    objCoverage.assets.remove_all
    objCoverage.assets.add("Satellite/MySatellite")
    objCoverage.use_object_times = True
    objCoverage.compute()

    objCoverageFOM = objCoverage.figure_of_merit
    objCoverageFOM.set_definition_type(FigureOfMeritDefinitionType.COVERAGE_TIME)
    objCoverageFOM.definition.set_compute_type(FigureOfMeritCompute.TOTAL)


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ObjectCoverage


Property detail
---------------

.. py:property:: access_interval
    :canonical: br.steak.core.stkobjects.ObjectCoverage.access_interval
    :type: ITimeToolTimeIntervalSmartInterval

    The object coverage's access interval.

.. py:property:: assets
    :canonical: br.steak.core.stkobjects.ObjectCoverage.assets
    :type: CoverageAssetListCollection

    Get the asset list collection.

.. py:property:: data_providers
    :canonical: br.steak.core.stkobjects.ObjectCoverage.data_providers
    :type: DataProviderCollection

    Return the object representing a list of available data providers for the object.

.. py:property:: figure_of_merit
    :canonical: br.steak.core.stkobjects.ObjectCoverage.figure_of_merit
    :type: ObjectCoverageFigureOfMerit

    Get the figure of merit on the object coverage.

.. py:property:: is_coverage_configuration_saved
    :canonical: br.steak.core.stkobjects.ObjectCoverage.is_coverage_configuration_saved
    :type: bool

    Save the single-object coverage definitions when the scenario is saved to disk, if a compute has been done.

.. py:property:: start_time
    :canonical: br.steak.core.stkobjects.ObjectCoverage.start_time
    :type: typing.Any

    Get or set the start time of object coverage. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: br.steak.core.stkobjects.ObjectCoverage.stop_time
    :type: typing.Any

    Get or set the stop time of object coverage. Uses DateFormat Dimension.

.. py:property:: use_object_times
    :canonical: br.steak.core.stkobjects.ObjectCoverage.use_object_times
    :type: bool

    Use object interval times.


Method detail
-------------



.. py:method:: clear(self) -> None
    :canonical: br.steak.core.stkobjects.ObjectCoverage.clear

    Remove the computation on the object coverage.

    :Returns:

        :obj:`~None`

.. py:method:: clear_coverage(self) -> None
    :canonical: br.steak.core.stkobjects.ObjectCoverage.clear_coverage

    Clear object coverage.

    :Returns:

        :obj:`~None`

.. py:method:: compute(self) -> None
    :canonical: br.steak.core.stkobjects.ObjectCoverage.compute

    Compute the object coverage.

    :Returns:

        :obj:`~None`











