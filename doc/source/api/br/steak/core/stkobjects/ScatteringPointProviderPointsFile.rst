ScatteringPointProviderPointsFile
=================================

.. py:class:: br.steak.core.stkobjects.ScatteringPointProviderPointsFile

   Bases: :py:class:`~br.steak.core.stkobjects.IScatteringPointProvider`, :py:class:`~br.steak.core.stkobjects.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.ICloneable`

   Class defining a scattring point provider where the points are defined in an ascii text file.

.. py:currentmodule:: ScatteringPointProviderPointsFile

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.ScatteringPointProviderPointsFile.default_scattering_point_model`
              - Get the link/embed controller for managing the default scattering point model component.
            * - :py:attr:`~br.steak.core.stkobjects.ScatteringPointProviderPointsFile.filename`
              - Get or set the scattering points filename.
            * - :py:attr:`~br.steak.core.stkobjects.ScatteringPointProviderPointsFile.scattering_points`
              - Get the collection of scattering points.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import ScatteringPointProviderPointsFile


Property detail
---------------

.. py:property:: default_scattering_point_model
    :canonical: br.steak.core.stkobjects.ScatteringPointProviderPointsFile.default_scattering_point_model
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the default scattering point model component.

.. py:property:: filename
    :canonical: br.steak.core.stkobjects.ScatteringPointProviderPointsFile.filename
    :type: str

    Get or set the scattering points filename.

.. py:property:: scattering_points
    :canonical: br.steak.core.stkobjects.ScatteringPointProviderPointsFile.scattering_points
    :type: ScatteringPointCollection

    Get the collection of scattering points.


