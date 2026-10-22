ThirdBodyFunction
=================

.. py:class:: br.ok.core.stkobjects.astrogator.ThirdBodyFunction

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   ThirdBody propagator function.

.. py:currentmodule:: ThirdBodyFunction

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ThirdBodyFunction.set_mode_type`
              - Set the third body gravity mode.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ThirdBodyFunction.ephemeris_source`
              - Source for the third body's ephemeris.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ThirdBodyFunction.ephemeris_source_warning`
              - Return a warning message if the Ephemeris source and the gravity are not compatible.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ThirdBodyFunction.mode`
              - Get the third body gravity mode. The IComponentInfo object returned by this property can be cast to GravityFieldFunction or PointMassFunction depending on the selected ModeType.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ThirdBodyFunction.mode_type`
              - Get the third body gravity mode type.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ThirdBodyFunction.third_body_name`
              - Get or set the selected third body model.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import ThirdBodyFunction


Property detail
---------------

.. py:property:: ephemeris_source
    :canonical: br.ok.core.stkobjects.astrogator.ThirdBodyFunction.ephemeris_source
    :type: EphemerisSource

    Source for the third body's ephemeris.

.. py:property:: ephemeris_source_warning
    :canonical: br.ok.core.stkobjects.astrogator.ThirdBodyFunction.ephemeris_source_warning
    :type: str

    Return a warning message if the Ephemeris source and the gravity are not compatible.

.. py:property:: mode
    :canonical: br.ok.core.stkobjects.astrogator.ThirdBodyFunction.mode
    :type: IComponentInfo

    Get the third body gravity mode. The IComponentInfo object returned by this property can be cast to GravityFieldFunction or PointMassFunction depending on the selected ModeType.

.. py:property:: mode_type
    :canonical: br.ok.core.stkobjects.astrogator.ThirdBodyFunction.mode_type
    :type: ThirdBodyMode

    Get the third body gravity mode type.

.. py:property:: third_body_name
    :canonical: br.ok.core.stkobjects.astrogator.ThirdBodyFunction.third_body_name
    :type: str

    Get or set the selected third body model.


Method detail
-------------






.. py:method:: set_mode_type(self, mode: ThirdBodyMode) -> None
    :canonical: br.ok.core.stkobjects.astrogator.ThirdBodyFunction.set_mode_type

    Set the third body gravity mode.

    :Parameters:

        **mode** : :obj:`~ThirdBodyMode`


    :Returns:

        :obj:`~None`



