StateCalcReferenceRadius
========================

.. py:class:: br.ok.core.stkobjects.astrogator.StateCalcReferenceRadius

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~br.ok.core.stkobjects.astrogator.ICloneable`

   Reference Radius Calc objects.

.. py:currentmodule:: StateCalcReferenceRadius

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcReferenceRadius.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcReferenceRadius.gravity_filename`
              - Source for the reference radius if RefRadSource is set to Gravity File.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.StateCalcReferenceRadius.reference_radius_source`
              - Get or set the source for the reference radius.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import StateCalcReferenceRadius


Property detail
---------------

.. py:property:: central_body_name
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcReferenceRadius.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: gravity_filename
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcReferenceRadius.gravity_filename
    :type: str

    Source for the reference radius if RefRadSource is set to Gravity File.

.. py:property:: reference_radius_source
    :canonical: br.ok.core.stkobjects.astrogator.StateCalcReferenceRadius.reference_radius_source
    :type: ReferenceRadiusSource

    Get or set the source for the reference radius.


