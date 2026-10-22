IFigureOfMeritDefinitionCompute
===============================

.. py:class:: br.ok.core.stkobjects.IFigureOfMeritDefinitionCompute

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

            * - :py:attr:`~br.ok.core.stkobjects.IFigureOfMeritDefinitionCompute.is_compute_type_supported`
              - Is the type of compute option supported?
            * - :py:attr:`~br.ok.core.stkobjects.IFigureOfMeritDefinitionCompute.set_compute_type`
              - Set the type of compute option.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.IFigureOfMeritDefinitionCompute.compute`
              - Compute.
            * - :py:attr:`~br.ok.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_supported_types`
              - Compute supported types.
            * - :py:attr:`~br.ok.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_type`
              - Type of compute option to be used for navigation accuracy.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import IFigureOfMeritDefinitionCompute


Property detail
---------------

.. py:property:: compute
    :canonical: br.ok.core.stkobjects.IFigureOfMeritDefinitionCompute.compute
    :type: IFigureOfMeritDefinitionData

    Compute.

.. py:property:: compute_supported_types
    :canonical: br.ok.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_supported_types
    :type: list

    Compute supported types.

.. py:property:: compute_type
    :canonical: br.ok.core.stkobjects.IFigureOfMeritDefinitionCompute.compute_type
    :type: FigureOfMeritCompute

    Type of compute option to be used for navigation accuracy.


Method detail
-------------




.. py:method:: is_compute_type_supported(self, compute_type: FigureOfMeritCompute) -> bool
    :canonical: br.ok.core.stkobjects.IFigureOfMeritDefinitionCompute.is_compute_type_supported

    Is the type of compute option supported?

    :Parameters:

        **compute_type** : :obj:`~FigureOfMeritCompute`


    :Returns:

        :obj:`~bool`

.. py:method:: set_compute_type(self, compute_type: FigureOfMeritCompute) -> None
    :canonical: br.ok.core.stkobjects.IFigureOfMeritDefinitionCompute.set_compute_type

    Set the type of compute option.

    :Parameters:

        **compute_type** : :obj:`~FigureOfMeritCompute`


    :Returns:

        :obj:`~None`

