AttitudeProfileFixedInAxes
==========================

.. py:class:: br.ok.core.stkobjects.AttitudeProfileFixedInAxes

   Bases: :py:class:`~br.ok.core.stkobjects.IVehicleAttitudeProfile`

   Fixed in Axes attitude profile: maintains a constant orientation of the body-fixed axes with respect to the specified reference axes, using the selected coordinate type.

.. py:currentmodule:: AttitudeProfileFixedInAxes

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.AttitudeProfileFixedInAxes.available_reference_axes`
              - Return the available reference axes.
            * - :py:attr:`~br.ok.core.stkobjects.AttitudeProfileFixedInAxes.orientation`
              - Get the orientation of the body-fixed axes.
            * - :py:attr:`~br.ok.core.stkobjects.AttitudeProfileFixedInAxes.reference_axes`
              - Reference axes with respect to which the body-fixed axes are oriented. The satellite's body axes or any axes dependent upon the satellite's body axes are invalid for this attitude profile; all other axes are valid choices for the reference axes.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import AttitudeProfileFixedInAxes


Property detail
---------------

.. py:property:: available_reference_axes
    :canonical: br.ok.core.stkobjects.AttitudeProfileFixedInAxes.available_reference_axes
    :type: list

    Return the available reference axes.

.. py:property:: orientation
    :canonical: br.ok.core.stkobjects.AttitudeProfileFixedInAxes.orientation
    :type: IOrientation

    Get the orientation of the body-fixed axes.

.. py:property:: reference_axes
    :canonical: br.ok.core.stkobjects.AttitudeProfileFixedInAxes.reference_axes
    :type: str

    Reference axes with respect to which the body-fixed axes are oriented. The satellite's body axes or any axes dependent upon the satellite's body axes are invalid for this attitude profile; all other axes are valid choices for the reference axes.


