PreferencesVDF
==============

.. py:class:: br.ok.core.stkobjects.PreferencesVDF

   Allow configuring VDF preferences.

.. py:currentmodule:: PreferencesVDF

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.PreferencesVDF.base_directory`
              - Get or set the Base Directory where VDF file is extracted.
            * - :py:attr:`~br.ok.core.stkobjects.PreferencesVDF.save_scenario_as_vdf`
              - Get or set the SaveScenarioAsVDF property determines whether a scenario will be saved as a scenario file or as a VDF file when the Save method is called. If a VDF file is loaded, then the SaveScenarioAsVDF property has no effect when Save is called.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import PreferencesVDF


Property detail
---------------

.. py:property:: base_directory
    :canonical: br.ok.core.stkobjects.PreferencesVDF.base_directory
    :type: str

    Get or set the Base Directory where VDF file is extracted.

.. py:property:: save_scenario_as_vdf
    :canonical: br.ok.core.stkobjects.PreferencesVDF.save_scenario_as_vdf
    :type: bool

    Get or set the SaveScenarioAsVDF property determines whether a scenario will be saved as a scenario file or as a VDF file when the Save method is called. If a VDF file is loaded, then the SaveScenarioAsVDF property has no effect when Save is called.

    Examples
    --------

    Save the current scenario as a VDF

    .. code-block:: python

        # STKObjectRoot root: STK Object Model Root
        scenario = root.current_scenario
        root.preferences.vdf_preferences.save_scenario_as_vdf = True



