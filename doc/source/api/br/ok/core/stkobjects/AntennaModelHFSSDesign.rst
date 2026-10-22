AntennaModelHFSSDesign
======================

.. py:class:: br.ok.core.stkobjects.AntennaModelHFSSDesign

   Bases: :py:class:`~br.ok.core.stkobjects.IAntennaModel`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining an HFSS design antenna model.

.. py:currentmodule:: AntennaModelHFSSDesign

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AntennaModelHFSSDesign.generate`
              - Generate the HFSS design antenna.
            * - :py:attr:`~br.ok.core.stkobjects.AntennaModelHFSSDesign.set_design_type`
              - Set the HFSS design type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AntennaModelHFSSDesign.availability`
              - Get the availability of the HFSS design antenna.
            * - :py:attr:`~br.ok.core.stkobjects.AntennaModelHFSSDesign.design`
              - Get the HFSS design.
            * - :py:attr:`~br.ok.core.stkobjects.AntennaModelHFSSDesign.status`
              - Get the status of the HFSS design antenna.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AntennaModelHFSSDesign


Property detail
---------------

.. py:property:: availability
    :canonical: br.ok.core.stkobjects.AntennaModelHFSSDesign.availability
    :type: str

    Get the availability of the HFSS design antenna.

.. py:property:: design
    :canonical: br.ok.core.stkobjects.AntennaModelHFSSDesign.design
    :type: IAntennaHFSSDesign

    Get the HFSS design.

.. py:property:: status
    :canonical: br.ok.core.stkobjects.AntennaModelHFSSDesign.status
    :type: AntennaHFSSDesignStatus

    Get the status of the HFSS design antenna.


Method detail
-------------



.. py:method:: generate(self) -> None
    :canonical: br.ok.core.stkobjects.AntennaModelHFSSDesign.generate

    Generate the HFSS design antenna.

    :Returns:

        :obj:`~None`

.. py:method:: set_design_type(self, type: AntennaHFSSDesignType) -> None
    :canonical: br.ok.core.stkobjects.AntennaModelHFSSDesign.set_design_type

    Set the HFSS design type.

    :Parameters:

        **type** : :obj:`~AntennaHFSSDesignType`


    :Returns:

        :obj:`~None`


