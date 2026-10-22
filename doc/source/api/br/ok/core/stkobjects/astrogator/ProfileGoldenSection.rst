ProfileGoldenSection
====================

.. py:class:: br.ok.core.stkobjects.astrogator.ProfileGoldenSection

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IProfile`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Golden Section profile.

.. py:currentmodule:: ProfileGoldenSection

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileGoldenSection.controls`
              - Get the list of control parameters defined for the profile.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileGoldenSection.enable_display_status`
              - If true, a page will appear during the targeting run to report the status of the targeting effort in terms of proximity to the desired value for each dependent variable in the profile.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileGoldenSection.log_file`
              - Name of the log file for this profile.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileGoldenSection.max_iterations`
              - Get or set the number of complete iterations of the profile to try before stopping. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileGoldenSection.results`
              - Get the list of results defined for the profile.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileGoldenSection.scripting_tool`
              - Return the Scripting tool for the sequence.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileGoldenSection.targeter_graphs`
              - Graphs.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import ProfileGoldenSection


Property detail
---------------

.. py:property:: controls
    :canonical: br.ok.core.stkobjects.astrogator.ProfileGoldenSection.controls
    :type: GoldenSectionControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: enable_display_status
    :canonical: br.ok.core.stkobjects.astrogator.ProfileGoldenSection.enable_display_status
    :type: bool

    If true, a page will appear during the targeting run to report the status of the targeting effort in terms of proximity to the desired value for each dependent variable in the profile.

.. py:property:: log_file
    :canonical: br.ok.core.stkobjects.astrogator.ProfileGoldenSection.log_file
    :type: str

    Name of the log file for this profile.

.. py:property:: max_iterations
    :canonical: br.ok.core.stkobjects.astrogator.ProfileGoldenSection.max_iterations
    :type: int

    Get or set the number of complete iterations of the profile to try before stopping. Dimensionless.

.. py:property:: results
    :canonical: br.ok.core.stkobjects.astrogator.ProfileGoldenSection.results
    :type: GoldenSectionResultCollection

    Get the list of results defined for the profile.

.. py:property:: scripting_tool
    :canonical: br.ok.core.stkobjects.astrogator.ProfileGoldenSection.scripting_tool
    :type: ScriptingTool

    Return the Scripting tool for the sequence.

.. py:property:: targeter_graphs
    :canonical: br.ok.core.stkobjects.astrogator.ProfileGoldenSection.targeter_graphs
    :type: TargeterGraphCollection

    Graphs.


