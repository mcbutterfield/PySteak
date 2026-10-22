MissileExternalPropulsion
=========================

.. py:class:: br.ok.core.stkobjects.aviator.MissileExternalPropulsion

   Class defining the External propulsion options for a missile.

.. py:currentmodule:: MissileExternalPropulsion

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.MissileExternalPropulsion.reload`
              - Reload the external prop file.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.MissileExternalPropulsion.set_filepath`
              - Set the filepath for the external prop file.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.aviator.MissileExternalPropulsion.filepath`
              - Get the filepath for the external prop file.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.MissileExternalPropulsion.is_valid`
              - Check whether the filepath is valid.
            * - :py:attr:`~br.ok.core.stkobjects.aviator.MissileExternalPropulsion.no_thrust_when_no_fuel`
              - Opt to have no thrust if the fuel is empty.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.aviator import MissileExternalPropulsion


Property detail
---------------

.. py:property:: filepath
    :canonical: br.ok.core.stkobjects.aviator.MissileExternalPropulsion.filepath
    :type: str

    Get the filepath for the external prop file.

.. py:property:: is_valid
    :canonical: br.ok.core.stkobjects.aviator.MissileExternalPropulsion.is_valid
    :type: bool

    Check whether the filepath is valid.

.. py:property:: no_thrust_when_no_fuel
    :canonical: br.ok.core.stkobjects.aviator.MissileExternalPropulsion.no_thrust_when_no_fuel
    :type: bool

    Opt to have no thrust if the fuel is empty.


Method detail
-------------





.. py:method:: reload(self) -> str
    :canonical: br.ok.core.stkobjects.aviator.MissileExternalPropulsion.reload

    Reload the external prop file.

    :Returns:

        :obj:`~str`

.. py:method:: set_filepath(self, filepath: str) -> str
    :canonical: br.ok.core.stkobjects.aviator.MissileExternalPropulsion.set_filepath

    Set the filepath for the external prop file.

    :Parameters:

        **filepath** : :obj:`~str`


    :Returns:

        :obj:`~str`

