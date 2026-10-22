ProfileChangePropagator
=======================

.. py:class:: br.ok.core.stkobjects.astrogator.ProfileChangePropagator

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IProfile`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Change Propagator profile.

.. py:currentmodule:: ProfileChangePropagator

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileChangePropagator.set_segment`
              - Set the targeted segment.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileChangePropagator.propagator_name`
              - Get or set the new propagator's name.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.ProfileChangePropagator.segment_name`
              - Get or set the name of the profile.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import ProfileChangePropagator


Property detail
---------------

.. py:property:: propagator_name
    :canonical: br.ok.core.stkobjects.astrogator.ProfileChangePropagator.propagator_name
    :type: str

    Get or set the new propagator's name.

.. py:property:: segment_name
    :canonical: br.ok.core.stkobjects.astrogator.ProfileChangePropagator.segment_name
    :type: str

    Get or set the name of the profile.


Method detail
-------------





.. py:method:: set_segment(self, mcs_segment: IMCSSegment) -> None
    :canonical: br.ok.core.stkobjects.astrogator.ProfileChangePropagator.set_segment

    Set the targeted segment.

    :Parameters:

        **mcs_segment** : :obj:`~IMCSSegment`


    :Returns:

        :obj:`~None`

