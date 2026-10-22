ProfileBisection
================

.. py:class:: br.steak.core.stkobjects.astrogator.ProfileBisection

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IProfile`, :py:class:`~br.steak.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   Single Parameter Bisection profile.

.. py:currentmodule:: ProfileBisection

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ProfileBisection.control_parameters`
              - Get the list of control parameters defined for the profile.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ProfileBisection.maximum_iterations`
              - Get or set the maximum number of iterations allowed.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ProfileBisection.reset_controls_before_run`
              - Reset controls before each run.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ProfileBisection.results`
              - Get the list of results defined for the profile.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ProfileBisection.scripting_tool`
              - Return the Scripting tool for the sequence.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ProfileBisection.targeter_graphs`
              - Graphs.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import ProfileBisection


Property detail
---------------

.. py:property:: control_parameters
    :canonical: br.steak.core.stkobjects.astrogator.ProfileBisection.control_parameters
    :type: BisectionControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: maximum_iterations
    :canonical: br.steak.core.stkobjects.astrogator.ProfileBisection.maximum_iterations
    :type: int

    Get or set the maximum number of iterations allowed.

.. py:property:: reset_controls_before_run
    :canonical: br.steak.core.stkobjects.astrogator.ProfileBisection.reset_controls_before_run
    :type: bool

    Reset controls before each run.

.. py:property:: results
    :canonical: br.steak.core.stkobjects.astrogator.ProfileBisection.results
    :type: BisectionResultCollection

    Get the list of results defined for the profile.

.. py:property:: scripting_tool
    :canonical: br.steak.core.stkobjects.astrogator.ProfileBisection.scripting_tool
    :type: ScriptingTool

    Return the Scripting tool for the sequence.

.. py:property:: targeter_graphs
    :canonical: br.steak.core.stkobjects.astrogator.ProfileBisection.targeter_graphs
    :type: TargeterGraphCollection

    Graphs.


