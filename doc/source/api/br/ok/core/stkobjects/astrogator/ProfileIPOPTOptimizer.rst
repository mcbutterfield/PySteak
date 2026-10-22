ProfileIPOPTOptimizer
=====================

.. py:class:: br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IProfile`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   IPOPT optimizer profile.

.. py:currentmodule:: ProfileIPOPTOptimizer

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.control_parameters`
              - Get the list of control parameters defined for the profile.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.maximum_iterations`
              - Get or set the maximum number of iterations before IPOPT should give up if it hasn't yet converged on a solution. The default value is 3000.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.options_filename`
              - If used, the associated IPOPT specifications file may define any of the various IPOPT options. Options in the file that conflict with options specified elsewhere will take precedence.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.reset_controls_before_run`
              - Reset controls before each run.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.results`
              - Get the list of results defined for the profile.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.scripting_tool`
              - Return the Scripting tool for the sequence.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.targeter_graphs`
              - Graphs.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.tolerance_on_complementary_infeasibility`
              - Get or set the desired absolute tolerance on the maximum norm of the complementarity conditions. The default value is 1.0E-4.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.tolerance_on_constraint_violation`
              - Get or set the tolerance by which user-specified constraints are allowed to be violated with the solution still considered feasible. The default value is 1.0E-4.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.tolerance_on_convergence`
              - Get or set the tolerance by which the optimality conditions must be satisfied for the problem to be considered converged. The default value is 1E-8.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.tolerance_on_dual_infeasibility`
              - Get or set the desired absolute tolerance on the maximum norm of the dual infeasibility. The default value is 1.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import ProfileIPOPTOptimizer


Property detail
---------------

.. py:property:: control_parameters
    :canonical: br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.control_parameters
    :type: IPOPTControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: maximum_iterations
    :canonical: br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.maximum_iterations
    :type: int

    Get or set the maximum number of iterations before IPOPT should give up if it hasn't yet converged on a solution. The default value is 3000.

.. py:property:: options_filename
    :canonical: br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.options_filename
    :type: str

    If used, the associated IPOPT specifications file may define any of the various IPOPT options. Options in the file that conflict with options specified elsewhere will take precedence.

.. py:property:: reset_controls_before_run
    :canonical: br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.reset_controls_before_run
    :type: bool

    Reset controls before each run.

.. py:property:: results
    :canonical: br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.results
    :type: IPOPTResultCollection

    Get the list of results defined for the profile.

.. py:property:: scripting_tool
    :canonical: br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.scripting_tool
    :type: ScriptingTool

    Return the Scripting tool for the sequence.

.. py:property:: targeter_graphs
    :canonical: br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.targeter_graphs
    :type: TargeterGraphCollection

    Graphs.

.. py:property:: tolerance_on_complementary_infeasibility
    :canonical: br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.tolerance_on_complementary_infeasibility
    :type: float

    Get or set the desired absolute tolerance on the maximum norm of the complementarity conditions. The default value is 1.0E-4.

.. py:property:: tolerance_on_constraint_violation
    :canonical: br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.tolerance_on_constraint_violation
    :type: float

    Get or set the tolerance by which user-specified constraints are allowed to be violated with the solution still considered feasible. The default value is 1.0E-4.

.. py:property:: tolerance_on_convergence
    :canonical: br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.tolerance_on_convergence
    :type: float

    Get or set the tolerance by which the optimality conditions must be satisfied for the problem to be considered converged. The default value is 1E-8.

.. py:property:: tolerance_on_dual_infeasibility
    :canonical: br.ok.core.stkobjects.astrogator.ProfileIPOPTOptimizer.tolerance_on_dual_infeasibility
    :type: float

    Get or set the desired absolute tolerance on the maximum norm of the dual infeasibility. The default value is 1.


