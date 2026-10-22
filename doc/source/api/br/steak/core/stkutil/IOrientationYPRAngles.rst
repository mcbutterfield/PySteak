IOrientationYPRAngles
=====================

.. py:class:: br.steak.core.stkutil.IOrientationYPRAngles

   Bases: IOrientation

   Interface for Yaw-Pitch Roll (YPR) Angles orientation system.

.. py:currentmodule:: IOrientationYPRAngles

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkutil.IOrientationYPRAngles.pitch`
              - Pitch angle. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkutil.IOrientationYPRAngles.roll`
              - Roll angle. Uses Angle Dimension.
            * - :py:attr:`~br.steak.core.stkutil.IOrientationYPRAngles.sequence`
              - YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.
            * - :py:attr:`~br.steak.core.stkutil.IOrientationYPRAngles.yaw`
              - Yaw angle. Uses Angle Dimension.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkutil import IOrientationYPRAngles


Property detail
---------------

.. py:property:: pitch
    :canonical: br.steak.core.stkutil.IOrientationYPRAngles.pitch
    :type: typing.Any

    Pitch angle. Uses Angle Dimension.

.. py:property:: roll
    :canonical: br.steak.core.stkutil.IOrientationYPRAngles.roll
    :type: typing.Any

    Roll angle. Uses Angle Dimension.

.. py:property:: sequence
    :canonical: br.steak.core.stkutil.IOrientationYPRAngles.sequence
    :type: YPRAnglesSequence

    YPR sequence. Must be set before Yaw,Pitch,Roll values. Otherwise the current Yaw,Pitch,Roll values will be converted to the Sequence specified.

.. py:property:: yaw
    :canonical: br.steak.core.stkutil.IOrientationYPRAngles.yaw
    :type: typing.Any

    Yaw angle. Uses Angle Dimension.


