SpaceEnvironmentSAAContour
==========================

.. py:class:: br.steak.core.stkobjects.SpaceEnvironmentSAAContour

   SAA settings.

.. py:currentmodule:: SpaceEnvironmentSAAContour

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.SpaceEnvironmentSAAContour.compute_saa_flux_intensity`
              - Compute SAA flux intensity at the specified time on the vehicle's channel. Uses DateFormat and FluxIntensity Dimensions.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.SpaceEnvironmentSAAContour.channel`
              - Energy level for SAA protons.
            * - :py:attr:`~br.steak.core.stkobjects.SpaceEnvironmentSAAContour.flux_level`
              - Flux level for SAA contour.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import SpaceEnvironmentSAAContour


Property detail
---------------

.. py:property:: channel
    :canonical: br.steak.core.stkobjects.SpaceEnvironmentSAAContour.channel
    :type: SpaceEnvironmentSAAChannel

    Energy level for SAA protons.

.. py:property:: flux_level
    :canonical: br.steak.core.stkobjects.SpaceEnvironmentSAAContour.flux_level
    :type: SpaceEnvironmentSAAFluxLevel

    Flux level for SAA contour.


Method detail
-------------



.. py:method:: compute_saa_flux_intensity(self, time: typing.Any) -> float
    :canonical: br.steak.core.stkobjects.SpaceEnvironmentSAAContour.compute_saa_flux_intensity

    Compute SAA flux intensity at the specified time on the vehicle's channel. Uses DateFormat and FluxIntensity Dimensions.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~float`



