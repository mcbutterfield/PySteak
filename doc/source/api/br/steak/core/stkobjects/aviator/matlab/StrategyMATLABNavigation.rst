StrategyMATLABNavigation
========================

.. py:class:: br.steak.core.stkobjects.aviator.matlab.StrategyMATLABNavigation

   Bases: :py:class:`~br.steak.core.stkobjects.aviator.matlab.IBasicManeuverStrategy`

   Class defining the MATLAB - Horizontal Plane strategy for a basic maneuver procedure.

.. py:currentmodule:: StrategyMATLABNavigation

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.matlab.StrategyMATLABNavigation.is_function_path_valid`
              - Check if the MATLAB function path is valid.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.aviator.matlab.StrategyMATLABNavigation.check_for_errors`
              - Get or set the option to check the function for errors.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.matlab.StrategyMATLABNavigation.display_output`
              - Get or set the option to display the output from the MATLAB function.
            * - :py:attr:`~br.steak.core.stkobjects.aviator.matlab.StrategyMATLABNavigation.function_name`
              - Get or set the name of the MATLAB function.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.aviator.matlab import StrategyMATLABNavigation


Property detail
---------------

.. py:property:: check_for_errors
    :canonical: br.steak.core.stkobjects.aviator.matlab.StrategyMATLABNavigation.check_for_errors
    :type: bool

    Get or set the option to check the function for errors.

.. py:property:: display_output
    :canonical: br.steak.core.stkobjects.aviator.matlab.StrategyMATLABNavigation.display_output
    :type: bool

    Get or set the option to display the output from the MATLAB function.

.. py:property:: function_name
    :canonical: br.steak.core.stkobjects.aviator.matlab.StrategyMATLABNavigation.function_name
    :type: str

    Get or set the name of the MATLAB function.


Method detail
-------------







.. py:method:: is_function_path_valid(self) -> bool
    :canonical: br.steak.core.stkobjects.aviator.matlab.StrategyMATLABNavigation.is_function_path_valid

    Check if the MATLAB function path is valid.

    :Returns:

        :obj:`~bool`

