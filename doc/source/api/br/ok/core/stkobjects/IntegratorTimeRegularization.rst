IntegratorTimeRegularization
============================

.. py:class:: br.ok.core.stkobjects.IntegratorTimeRegularization

   Class defining time regularization for the HPOP integrator, i.e. integration the orbit with respect to regularized time.

.. py:currentmodule:: IntegratorTimeRegularization

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.IntegratorTimeRegularization.exponent`
              - Exponent used in the regularization equation. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.IntegratorTimeRegularization.steps_per_orbit`
              - Integration steps per orbit. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.IntegratorTimeRegularization.use`
              - Opt whether to integrate the orbit with respect to regularized time.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import IntegratorTimeRegularization


Property detail
---------------

.. py:property:: exponent
    :canonical: br.ok.core.stkobjects.IntegratorTimeRegularization.exponent
    :type: float

    Exponent used in the regularization equation. Dimensionless.

.. py:property:: steps_per_orbit
    :canonical: br.ok.core.stkobjects.IntegratorTimeRegularization.steps_per_orbit
    :type: int

    Integration steps per orbit. Dimensionless.

.. py:property:: use
    :canonical: br.ok.core.stkobjects.IntegratorTimeRegularization.use
    :type: bool

    Opt whether to integrate the orbit with respect to regularized time.


