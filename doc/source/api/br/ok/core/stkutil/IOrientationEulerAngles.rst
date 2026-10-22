IOrientationEulerAngles
=======================

.. py:class:: br.ok.core.stkutil.IOrientationEulerAngles

   Bases: IOrientation

   Interface for Euler Angles orientation method.

.. py:currentmodule:: IOrientationEulerAngles

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkutil.IOrientationEulerAngles.a`
              - Euler A angle. Uses Angle Dimension.
            * - :py:attr:`~br.ok.core.stkutil.IOrientationEulerAngles.b`
              - Euler b angle. Uses Angle Dimension.
            * - :py:attr:`~br.ok.core.stkutil.IOrientationEulerAngles.c`
              - Euler C angle. Uses Angle Dimension.
            * - :py:attr:`~br.ok.core.stkutil.IOrientationEulerAngles.sequence`
              - Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.


Import detail
-------------

.. code-block:: python

    from br.ok.core.stkutil import IOrientationEulerAngles


Property detail
---------------

.. py:property:: a
    :canonical: br.ok.core.stkutil.IOrientationEulerAngles.a
    :type: typing.Any

    Euler A angle. Uses Angle Dimension.

.. py:property:: b
    :canonical: br.ok.core.stkutil.IOrientationEulerAngles.b
    :type: typing.Any

    Euler b angle. Uses Angle Dimension.

.. py:property:: c
    :canonical: br.ok.core.stkutil.IOrientationEulerAngles.c
    :type: typing.Any

    Euler C angle. Uses Angle Dimension.

.. py:property:: sequence
    :canonical: br.ok.core.stkutil.IOrientationEulerAngles.sequence
    :type: EulerOrientationSequenceType

    Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.


