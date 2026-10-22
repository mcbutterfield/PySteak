RFFilterModelIIR
================

.. py:class:: br.steak.core.stkobjects.RFFilterModelIIR

   Bases: :py:class:`~br.steak.core.stkobjects.IRFFilterModel`, :py:class:`~br.steak.core.stkobjects.IComponentInfo`, :py:class:`~br.steak.core.stkobjects.ICloneable`

   Class defining a IIR box car filter model.

.. py:currentmodule:: RFFilterModelIIR

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.RFFilterModelIIR.denominator_complex_polynomial`
              - Get the denominator complex polynomial.
            * - :py:attr:`~br.steak.core.stkobjects.RFFilterModelIIR.numerator_complex_polynomial`
              - Get the numerator complex polynomial.
            * - :py:attr:`~br.steak.core.stkobjects.RFFilterModelIIR.sampling_frequency`
              - Get or set the sampling frequency.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import RFFilterModelIIR


Property detail
---------------

.. py:property:: denominator_complex_polynomial
    :canonical: br.steak.core.stkobjects.RFFilterModelIIR.denominator_complex_polynomial
    :type: CommRadComplexNumberCollection

    Get the denominator complex polynomial.

.. py:property:: numerator_complex_polynomial
    :canonical: br.steak.core.stkobjects.RFFilterModelIIR.numerator_complex_polynomial
    :type: CommRadComplexNumberCollection

    Get the numerator complex polynomial.

.. py:property:: sampling_frequency
    :canonical: br.steak.core.stkobjects.RFFilterModelIIR.sampling_frequency
    :type: float

    Get or set the sampling frequency.


