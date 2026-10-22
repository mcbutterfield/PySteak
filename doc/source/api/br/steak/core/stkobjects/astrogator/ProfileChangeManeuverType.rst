ProfileChangeManeuverType
=========================

.. py:class:: br.steak.core.stkobjects.astrogator.ProfileChangeManeuverType

   Bases: :py:class:`~br.steak.core.stkobjects.astrogator.IProfile`, :py:class:`~br.steak.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Change Maneuver Type profile.

.. py:currentmodule:: ProfileChangeManeuverType

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ProfileChangeManeuverType.maneuver_type`
              - Get or set the new maneuver type for the targeted segment.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.ProfileChangeManeuverType.segment`
              - Get or set the targeted maneuver segment.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import ProfileChangeManeuverType


Property detail
---------------

.. py:property:: maneuver_type
    :canonical: br.steak.core.stkobjects.astrogator.ProfileChangeManeuverType.maneuver_type
    :type: ManeuverType

    Get or set the new maneuver type for the targeted segment.

.. py:property:: segment
    :canonical: br.steak.core.stkobjects.astrogator.ProfileChangeManeuverType.segment
    :type: MCSManeuver

    Get or set the targeted maneuver segment.


