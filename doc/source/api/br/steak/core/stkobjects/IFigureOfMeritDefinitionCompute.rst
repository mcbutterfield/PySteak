IFigureOfMeritDefinitionCompute
===============================

.. py:class:: br.steak.core.stkobjects.IFigureOfMeritDefinitionCompute

   Bases: IFigureOfMeritDefinition

   Compute options for navigation accuracy.

.. py:currentmodule:: IFigureOfMeritDefinitionCompute

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.IFigureOfMeritDefinitionCompute.is_compute_type_supported`
              - Is the type of compute option supported?
            * - :py:attr:`~br.steak.core.stkobjects.IFigureOfMeritDefinitionCompute.set_compute_type`
              - Set the type of compute option.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.IFigureOfMeritDefinitionCompute.compute`
              - Compute.
            * - :py:attr:`~br.steak.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_supported_types`
              - Compute supported types.
            * - :py:attr:`~br.steak.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_type`
              - Type of compute option to be used for navigation accuracy.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import IFigureOfMeritDefinitionCompute


Property detail
---------------

.. py:property:: compute
    :canonical: br.steak.core.stkobjects.IFigureOfMeritDefinitionCompute.compute
    :type: IFigureOfMeritDefinitionData

    Compute.

.. py:property:: compute_supported_types
    :canonical: br.steak.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_supported_types
    :type: list

    Compute supported types.

.. py:property:: compute_type
    :canonical: br.steak.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_type
    :type: FigureOfMeritCompute

    Type of compute option to be used for navigation accuracy.


Method detail
-------------




.. py:method:: is_compute_type_supported(self, compute_type: FigureOfMeritCompute) -> bool
    :canonical: br.steak.core.stkobjects.IFigureOfMeritDefinitionCompute.is_compute_type_supported

    Is the type of compute option supported?

    :Parameters:

        **compute_type** : :obj:`~FigureOfMeritCompute`


    :Returns:

        :obj:`~bool`

.. py:method:: set_compute_type(self, compute_type: FigureOfMeritCompute) -> None
    :canonical: br.steak.core.stkobjects.IFigureOfMeritDefinitionCompute.set_compute_type

    Set the type of compute option.

    :Parameters:

        **compute_type** : :obj:`~FigureOfMeritCompute`


    :Returns:

        :obj:`~None`

