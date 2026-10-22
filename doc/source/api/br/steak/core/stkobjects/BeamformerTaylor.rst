BeamformerTaylor
================

.. py:class:: br.steak.core.stkobjects.BeamformerTaylor

   Bases: :py:class:`~br.steak.core.stkobjects.IBeamformer`

   Class defining a Taylor tapered beamformer.

.. py:currentmodule:: BeamformerTaylor

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.BeamformerTaylor.sidelobe_count`
              - Get or set the number of desired sidelobes to hold close to the desired sidelobe level.
            * - :py:attr:`~br.steak.core.stkobjects.BeamformerTaylor.sidelobe_level`
              - Get or set the sidelobe level relative to the maximum gain.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import BeamformerTaylor


Property detail
---------------

.. py:property:: sidelobe_count
    :canonical: br.steak.core.stkobjects.BeamformerTaylor.sidelobe_count
    :type: int

    Get or set the number of desired sidelobes to hold close to the desired sidelobe level.

.. py:property:: sidelobe_level
    :canonical: br.steak.core.stkobjects.BeamformerTaylor.sidelobe_level
    :type: float

    Get or set the sidelobe level relative to the maximum gain.


