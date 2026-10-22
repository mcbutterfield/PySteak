TransmitterGraphics3D
=====================

.. py:class:: br.steak.core.stkobjects.TransmitterGraphics3D

   Class defining 3D Graphics properties of a Transmitter.

.. py:currentmodule:: TransmitterGraphics3D

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.TransmitterGraphics3D.show_boresight`
              - Opt whether to display boresight graphics for the transmitter's antenna.
            * - :py:attr:`~br.steak.core.stkobjects.TransmitterGraphics3D.show_contours`
              - Opt whether to display contour graphics for the transmitter's antenna.
            * - :py:attr:`~br.steak.core.stkobjects.TransmitterGraphics3D.vector`
              - Get the transmitter's Vector properties.
            * - :py:attr:`~br.steak.core.stkobjects.TransmitterGraphics3D.volume`
              - Get the transmitter's antenna volume graphics interface.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import TransmitterGraphics3D


Property detail
---------------

.. py:property:: show_boresight
    :canonical: br.steak.core.stkobjects.TransmitterGraphics3D.show_boresight
    :type: bool

    Opt whether to display boresight graphics for the transmitter's antenna.

.. py:property:: show_contours
    :canonical: br.steak.core.stkobjects.TransmitterGraphics3D.show_contours
    :type: bool

    Opt whether to display contour graphics for the transmitter's antenna.

.. py:property:: vector
    :canonical: br.steak.core.stkobjects.TransmitterGraphics3D.vector
    :type: Graphics3DVector

    Get the transmitter's Vector properties.

.. py:property:: volume
    :canonical: br.steak.core.stkobjects.TransmitterGraphics3D.volume
    :type: AntennaVolumeGraphics

    Get the transmitter's antenna volume graphics interface.


