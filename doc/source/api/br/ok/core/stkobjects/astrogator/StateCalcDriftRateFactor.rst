StateCalcDriftRateFactor
========================

.. py:class:: br.ok.core.stkobjects.astrogator.StateCalcDriftRateFactor

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   DriftRateFactor Calc objects.

.. py:currentmodule:: StateCalcDriftRateFactor

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcDriftRateFactor.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcDriftRateFactor.drift_rate_model`
              - Get or set the gravity model used to compute drift rate.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import StateCalcDriftRateFactor


Property detail
---------------

.. py:property:: central_body_name
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcDriftRateFactor.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: drift_rate_model
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcDriftRateFactor.drift_rate_model
    :type: GeoStationaryDriftRateModel

    Get or set the gravity model used to compute drift rate.


