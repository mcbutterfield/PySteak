Graphics3DReferencePoint
========================

.. py:class:: br.steak.core.stkobjects.Graphics3DReferencePoint

   Bases: :py:class:`~br.steak.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchComponent`, :py:class:`~br.steak.core.stkobjects.IDisplayTime`

   Class defining a reference point (3D Graphics, Vector Geometry Tool).

.. py:currentmodule:: Graphics3DReferencePoint

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DReferencePoint.available_systems`
              - Return an array of available Systems.
            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DReferencePoint.cartesian_units_abbreviation`
              - Cartesian Unit Abrv uses Distance.
            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DReferencePoint.magnitude_units_abbreviation`
              - The Magnitude Unit abrv.
            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DReferencePoint.right_ascension_declination_units_abbreviation`
              - Right Ascension Declination Unit Abrv.
            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DReferencePoint.show_cartesian_value`
              - If selected, the cartesian value is displayed on the selected geometric element.
            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DReferencePoint.show_magnitude_value`
              - If selected, the magnitude value is displayed on the selected geometric element.
            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DReferencePoint.show_right_ascension_declination_values`
              - Displays right-ascension and declination values with the selected point.
            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DReferencePoint.size`
              - Get or set the size of the selected geometric plane or point. Dimensionless.
            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DReferencePoint.system`
              - The name of the system used to define the coordinate frame associated with the selected RefCrdn.
            * - :py:attr:`~br.steak.core.stkobjects.Graphics3DReferencePoint.trajectory_type`
              - Specify the arrow type used to represent the geometric element.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import Graphics3DReferencePoint


Property detail
---------------

.. py:property:: available_systems
    :canonical: br.steak.core.stkobjects.Graphics3DReferencePoint.available_systems
    :type: list

    Return an array of available Systems.

.. py:property:: cartesian_units_abbreviation
    :canonical: br.steak.core.stkobjects.Graphics3DReferencePoint.cartesian_units_abbreviation
    :type: str

    Cartesian Unit Abrv uses Distance.

.. py:property:: magnitude_units_abbreviation
    :canonical: br.steak.core.stkobjects.Graphics3DReferencePoint.magnitude_units_abbreviation
    :type: str

    The Magnitude Unit abrv.

.. py:property:: right_ascension_declination_units_abbreviation
    :canonical: br.steak.core.stkobjects.Graphics3DReferencePoint.right_ascension_declination_units_abbreviation
    :type: str

    Right Ascension Declination Unit Abrv.

.. py:property:: show_cartesian_value
    :canonical: br.steak.core.stkobjects.Graphics3DReferencePoint.show_cartesian_value
    :type: bool

    If selected, the cartesian value is displayed on the selected geometric element.

.. py:property:: show_magnitude_value
    :canonical: br.steak.core.stkobjects.Graphics3DReferencePoint.show_magnitude_value
    :type: bool

    If selected, the magnitude value is displayed on the selected geometric element.

.. py:property:: show_right_ascension_declination_values
    :canonical: br.steak.core.stkobjects.Graphics3DReferencePoint.show_right_ascension_declination_values
    :type: bool

    Displays right-ascension and declination values with the selected point.

.. py:property:: size
    :canonical: br.steak.core.stkobjects.Graphics3DReferencePoint.size
    :type: float

    Get or set the size of the selected geometric plane or point. Dimensionless.

.. py:property:: system
    :canonical: br.steak.core.stkobjects.Graphics3DReferencePoint.system
    :type: str

    The name of the system used to define the coordinate frame associated with the selected RefCrdn.

.. py:property:: trajectory_type
    :canonical: br.steak.core.stkobjects.Graphics3DReferencePoint.trajectory_type
    :type: TrajectoryType

    Specify the arrow type used to represent the geometric element.


