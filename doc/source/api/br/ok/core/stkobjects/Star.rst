Star
====

.. py:class:: br.ok.core.stkobjects.Star

   Bases: :py:class:`~br.ok.core.stkobjects.ISTKObject`, :py:class:`~br.ok.core.stkobjects.ILifetimeInformation`

   Class defining the Star object.

.. py:currentmodule:: Star

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Star.access_constraints`
              - Get the constraints imposed on the star.
            * - :py:attr:`~br.ok.core.stkobjects.Star.chain_analysis_options`
              - Get the star's chain analysis options.
            * - :py:attr:`~br.ok.core.stkobjects.Star.epoch`
              - Epoch of the star position information as a Julian epoch (yyyy.yy). The Julian epoch is related to the Julian date by the expression JD = 2451545.0 + (yyyy.yy - 2000.0) x 365.25, where 2451545.0 (TT) represents the standard J2000 epoch.
            * - :py:attr:`~br.ok.core.stkobjects.Star.graphics`
              - Get the star's 2D Graphics properties.
            * - :py:attr:`~br.ok.core.stkobjects.Star.graphics_3d`
              - Get the star's 3D Graphics properties.
            * - :py:attr:`~br.ok.core.stkobjects.Star.location_declination`
              - The star's declination: the angle from the inertial equator measured toward the inertial positive Z-axis. Uses Angle Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Star.location_right_ascension`
              - The star's right ascension: the angle in the equatorial plane measured in a right-handed sense about the inertial Z-axis from the inertial X-axis. Uses Angle Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Star.magnitude`
              - Magnitude, the visual brightness of the star. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.Star.parallax`
              - Annual parallax: motion of a star due to changes in the Earth's position relative to the solar system barycenter. Uses Angle Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Star.proper_motion_declination`
              - Motion of the star relative to the solar system barycenter expressed in arc seconds per year. Here, declination refers to motion from the inertial equator measured towards the inertial positive Z-axis. Uses AngleRate Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Star.proper_motion_right_ascension`
              - Motion of star relative to solar system barycenter expressed in arc seconds per year. Here, right ascension refers to motion in equatorial plane measured in a right-handed sense about the inertial Z-axis from inertial X-axis. Uses AngleRate Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Star.radial_velocity`
              - The star's radial velocity relative to the solar system barycenter. Uses Rate dimension.
            * - :py:attr:`~br.ok.core.stkobjects.Star.reference_frame`
              - Return a reference frame.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import Star


Property detail
---------------

.. py:property:: access_constraints
    :canonical: br.ok.core.stkobjects.Star.access_constraints
    :type: AccessConstraintCollection

    Get the constraints imposed on the star.

.. py:property:: chain_analysis_options
    :canonical: br.ok.core.stkobjects.Star.chain_analysis_options
    :type: ChainAnalysisOptions

    Get the star's chain analysis options.

.. py:property:: epoch
    :canonical: br.ok.core.stkobjects.Star.epoch
    :type: str

    Epoch of the star position information as a Julian epoch (yyyy.yy). The Julian epoch is related to the Julian date by the expression JD = 2451545.0 + (yyyy.yy - 2000.0) x 365.25, where 2451545.0 (TT) represents the standard J2000 epoch.

.. py:property:: graphics
    :canonical: br.ok.core.stkobjects.Star.graphics
    :type: StarGraphics

    Get the star's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: br.ok.core.stkobjects.Star.graphics_3d
    :type: StarGraphics3D

    Get the star's 3D Graphics properties.

.. py:property:: location_declination
    :canonical: br.ok.core.stkobjects.Star.location_declination
    :type: typing.Any

    The star's declination: the angle from the inertial equator measured toward the inertial positive Z-axis. Uses Angle Dimension.

.. py:property:: location_right_ascension
    :canonical: br.ok.core.stkobjects.Star.location_right_ascension
    :type: typing.Any

    The star's right ascension: the angle in the equatorial plane measured in a right-handed sense about the inertial Z-axis from the inertial X-axis. Uses Angle Dimension.

.. py:property:: magnitude
    :canonical: br.ok.core.stkobjects.Star.magnitude
    :type: float

    Magnitude, the visual brightness of the star. Dimensionless.

.. py:property:: parallax
    :canonical: br.ok.core.stkobjects.Star.parallax
    :type: typing.Any

    Annual parallax: motion of a star due to changes in the Earth's position relative to the solar system barycenter. Uses Angle Dimension.

.. py:property:: proper_motion_declination
    :canonical: br.ok.core.stkobjects.Star.proper_motion_declination
    :type: float

    Motion of the star relative to the solar system barycenter expressed in arc seconds per year. Here, declination refers to motion from the inertial equator measured towards the inertial positive Z-axis. Uses AngleRate Dimension.

.. py:property:: proper_motion_right_ascension
    :canonical: br.ok.core.stkobjects.Star.proper_motion_right_ascension
    :type: float

    Motion of star relative to solar system barycenter expressed in arc seconds per year. Here, right ascension refers to motion in equatorial plane measured in a right-handed sense about the inertial Z-axis from inertial X-axis. Uses AngleRate Dimension.

.. py:property:: radial_velocity
    :canonical: br.ok.core.stkobjects.Star.radial_velocity
    :type: float

    The star's radial velocity relative to the solar system barycenter. Uses Rate dimension.

.. py:property:: reference_frame
    :canonical: br.ok.core.stkobjects.Star.reference_frame
    :type: StarReferenceFrame

    Return a reference frame.


