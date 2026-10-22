DirectionEuler
==============

.. py:class:: br.ok.core.stkutil.DirectionEuler

   Bases: :py:class:`~br.ok.core.stkutil.IDirection`

   Euler direction sequence.

.. py:currentmodule:: DirectionEuler

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkutil.DirectionEuler.b`
              - Euler B angle. Uses Angle Dimension.
            * - :py:attr:`~br.ok.core.stkutil.DirectionEuler.c`
              - Euler C angle. Uses Angle Dimension.
            * - :py:attr:`~br.ok.core.stkutil.DirectionEuler.sequence`
              - Euler direction sequence.  Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkutil import DirectionEuler


Property detail
---------------

.. py:property:: b
    :canonical: br.ok.core.stkutil.DirectionEuler.b
    :type: typing.Any

    Euler B angle. Uses Angle Dimension.

.. py:property:: c
    :canonical: br.ok.core.stkutil.DirectionEuler.c
    :type: typing.Any

    Euler C angle. Uses Angle Dimension.

.. py:property:: sequence
    :canonical: br.ok.core.stkutil.DirectionEuler.sequence
    :type: EulerDirectionSequence

    Euler direction sequence.  Must be set before B,C values. Otherwise the B,C values will converted to the Sequence specified.


