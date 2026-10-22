IOrientationEulerAngles
=======================

.. py:class:: br.steak.core.stkutil.IOrientationEulerAngles

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

            * - :py:attr:`~br.steak.core.stkutil.IOrientationEulerAngles.a`
              - Euler A angle. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkutil.IOrientationEulerAngles.b`
              - Euler b angle. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkutil.IOrientationEulerAngles.c`
              - Euler C angle. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkutil.IOrientationEulerAngles.sequence`
              - Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkutil import IOrientationEulerAngles


Property detail
---------------

.. py:property:: a
    :canonical: br.steak.core.stkutil.IOrientationEulerAngles.a
    :type: typing.Any

    Euler A angle. Uses Angle Dimension.

.. py:property:: b
    :canonical: br.steak.core.stkutil.IOrientationEulerAngles.b
    :type: typing.Any

    Euler b angle. Uses Angle Dimension.

.. py:property:: c
    :canonical: br.steak.core.stkutil.IOrientationEulerAngles.c
    :type: typing.Any

    Euler C angle. Uses Angle Dimension.

.. py:property:: sequence
    :canonical: br.steak.core.stkutil.IOrientationEulerAngles.sequence
    :type: EulerOrientationSequenceType

    Euler rotation sequence. Must be set before A,B,C values. Otherwise the current A,B,C values will be converted to the Sequence specified.


