FlightDynamicsRecord
====================

.. py:class:: br.ok.core.stkobjects.astrogator.FlightDynamicsRecord

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   Flight Dynamics Records.

.. py:currentmodule:: FlightDynamicsRecord

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.FlightDynamicsRecord.export_propulsion_to_browser`
              - Export the version of the propagator stored in this record to the component browser.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.FlightDynamicsRecord.notes`
              - User commecnt/information associated with the record.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.FlightDynamicsRecord.propagator`
              - The numerical propagator (force model and integrator) configuration associated with this record
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.FlightDynamicsRecord.propagator_name`
              - Propagator name.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.FlightDynamicsRecord.record_time_stamp`
              - Time stamp when the FD record was created from its source.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.FlightDynamicsRecord.state_config_properties`
              - State Config. properties



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import FlightDynamicsRecord


Property detail
---------------

.. py:property:: notes
    :canonical: br.ok.core.stkobjects.astrogator.FlightDynamicsRecord.notes
    :type: str

    User commecnt/information associated with the record.

.. py:property:: propagator
    :canonical: br.ok.core.stkobjects.astrogator.FlightDynamicsRecord.propagator
    :type: IComponentInfo

    The numerical propagator (force model and integrator) configuration associated with this record

.. py:property:: propagator_name
    :canonical: br.ok.core.stkobjects.astrogator.FlightDynamicsRecord.propagator_name
    :type: str

    Propagator name.

.. py:property:: record_time_stamp
    :canonical: br.ok.core.stkobjects.astrogator.FlightDynamicsRecord.record_time_stamp
    :type: str

    Time stamp when the FD record was created from its source.

.. py:property:: state_config_properties
    :canonical: br.ok.core.stkobjects.astrogator.FlightDynamicsRecord.state_config_properties
    :type: StateConfigCollection

    State Config. properties


Method detail
-------------

.. py:method:: export_propulsion_to_browser(self) -> None
    :canonical: br.ok.core.stkobjects.astrogator.FlightDynamicsRecord.export_propulsion_to_browser

    Export the version of the propagator stored in this record to the component browser.

    :Returns:

        :obj:`~None`







