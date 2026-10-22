LaserTroposphericScintillationLossModelITURP1814
================================================

.. py:class:: br.ok.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814

   Bases: :py:class:`~br.ok.core.stkobjects.ILaserTroposphericScintillationLossModel`, :py:class:`~br.ok.core.stkobjects.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.ICloneable`

   Class defining an ITU-R P.1814 laser tropospheric scintillation loss model.

.. py:currentmodule:: LaserTroposphericScintillationLossModelITURP1814

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814.set_atmospheric_turbulence_model_type`
              - Set the atmospheric turbulence model type.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814.atmospheric_turbulence_model`
              - Get the atmospheric turbulence model.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import LaserTroposphericScintillationLossModelITURP1814


Property detail
---------------

.. py:property:: atmospheric_turbulence_model
    :canonical: br.ok.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814.atmospheric_turbulence_model
    :type: IAtmosphericTurbulenceModel

    Get the atmospheric turbulence model.


Method detail
-------------


.. py:method:: set_atmospheric_turbulence_model_type(self, value: AtmosphericTurbulenceModelType) -> None
    :canonical: br.ok.core.stkobjects.LaserTroposphericScintillationLossModelITURP1814.set_atmospheric_turbulence_model_type

    Set the atmospheric turbulence model type.

    :Parameters:

        **value** : :obj:`~AtmosphericTurbulenceModelType`


    :Returns:

        :obj:`~None`

