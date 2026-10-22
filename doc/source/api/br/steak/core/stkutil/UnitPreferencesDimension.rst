UnitPreferencesDimension
========================

.. py:class:: br.steak.core.stkutil.UnitPreferencesDimension

   Object that contains info on the Dimension.

.. py:currentmodule:: UnitPreferencesDimension

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkutil.UnitPreferencesDimension.set_current_unit`
              - Set the Unit for this simple dimension.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkutil.UnitPreferencesDimension.available_units`
              - Return collection of Units.
            * - :py:attr:`~br.steak.core.stkutil.UnitPreferencesDimension.current_unit`
              - Return the current unit for this dimension.
            * - :py:attr:`~br.steak.core.stkutil.UnitPreferencesDimension.identifier`
              - Return the ID of the dimension.
            * - :py:attr:`~br.steak.core.stkutil.UnitPreferencesDimension.name`
              - Return the current Dimension's full name.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkutil import UnitPreferencesDimension


Property detail
---------------

.. py:property:: available_units
    :canonical: br.steak.core.stkutil.UnitPreferencesDimension.available_units
    :type: UnitPreferencesUnitCollection

    Return collection of Units.

.. py:property:: current_unit
    :canonical: br.steak.core.stkutil.UnitPreferencesDimension.current_unit
    :type: UnitPreferencesUnit

    Return the current unit for this dimension.

.. py:property:: identifier
    :canonical: br.steak.core.stkutil.UnitPreferencesDimension.identifier
    :type: int

    Return the ID of the dimension.

.. py:property:: name
    :canonical: br.steak.core.stkutil.UnitPreferencesDimension.name
    :type: str

    Return the current Dimension's full name.


Method detail
-------------





.. py:method:: set_current_unit(self, unit_abbrv: str) -> None
    :canonical: br.steak.core.stkutil.UnitPreferencesDimension.set_current_unit

    Set the Unit for this simple dimension.

    :Parameters:

        **unit_abbrv** : :obj:`~str`


    :Returns:

        :obj:`~None`

