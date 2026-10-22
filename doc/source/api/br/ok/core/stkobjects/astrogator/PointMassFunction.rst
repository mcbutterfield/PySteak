PointMassFunction
=================

.. py:class:: br.ok.core.stkobjects.astrogator.PointMassFunction

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   Point Mass function.

.. py:currentmodule:: PointMassFunction

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.PointMassFunction.gravitational_parameter_source`
              - Get or set the source for the third body's gravitational parameter.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.PointMassFunction.mu`
              - Get or set the gravitational parameter. Uses Gravity Param Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import PointMassFunction


Property detail
---------------

.. py:property:: gravitational_parameter_source
    :canonical: br.ok.core.stkobjects.astrogator.PointMassFunction.gravitational_parameter_source
    :type: GravParameterSource

    Get or set the source for the third body's gravitational parameter.

.. py:property:: mu
    :canonical: br.ok.core.stkobjects.astrogator.PointMassFunction.mu
    :type: float

    Get or set the gravitational parameter. Uses Gravity Param Dimension.


