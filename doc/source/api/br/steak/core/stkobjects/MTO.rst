MTO
===

.. py:class:: br.steak.core.stkobjects.MTO

   Bases: :py:class:`~br.steak.core.stkobjects.ISTKObject`, :py:class:`~br.steak.core.stkobjects.ILifetimeInformation`

   Multi-Track Object (MTO).

.. py:currentmodule:: MTO

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.MTO.analysis`
              - Get the MTO's spatial state.
            * - :py:attr:`~br.steak.core.stkobjects.MTO.default_track`
              - Get the default MTO track.
            * - :py:attr:`~br.steak.core.stkobjects.MTO.global_track_options`
              - Get the global MTO track options.
            * - :py:attr:`~br.steak.core.stkobjects.MTO.graphics`
              - Get the MTO's 2D Graphics properties.
            * - :py:attr:`~br.steak.core.stkobjects.MTO.graphics_3d`
              - Get the MTO's 3D Graphics properties.
            * - :py:attr:`~br.steak.core.stkobjects.MTO.tracks`
              - Get the collection of MTO tracks.



Examples
--------

Load multi-track object (MTO) track points from a file

.. code-block:: python

    # load_points expects the path an Ephemeris file path
    # MTO mto: MTO Object
    track2 = mto.tracks.add(2)
    installPath = r"C:\Program Files\AGI\STK_ODTK 13" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    track2.points.load_points(
        os.path.join(installPath, "Data", "Resources", "stktraining", "text", "EphemerisLLATimePosVel_Example.e")
    )
    track2.interpolate = True


Create a New MTO (on the current scenario central body)

.. code-block:: python

    # Scenario scenario: Scenario object
    mto = scenario.children.new(STKObjectType.MTO, "MyMTO")

    root.units_preferences.set_current_unit("DateFormat", "EpSec")

    mtoTimes = [[0], [7200]]
    mtoLats = [[36.77], [34.80]]
    mtoLons = [[-77.25], [-78.37]]
    mtoAlts = [[5], [5]]

    track1 = mto.tracks.add_track(1, mtoTimes, mtoLats, mtoLons, mtoAlts)
    track1.interpolate = True
    # Change the color of the track
    mto.graphics.tracks.get_track_from_identifier(1).color = Colors.Red


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import MTO


Property detail
---------------

.. py:property:: analysis
    :canonical: br.steak.core.stkobjects.MTO.analysis
    :type: MTOAnalysis

    Get the MTO's spatial state.

.. py:property:: default_track
    :canonical: br.steak.core.stkobjects.MTO.default_track
    :type: MTODefaultTrack

    Get the default MTO track.

.. py:property:: global_track_options
    :canonical: br.steak.core.stkobjects.MTO.global_track_options
    :type: MTOGlobalTrackOptions

    Get the global MTO track options.

.. py:property:: graphics
    :canonical: br.steak.core.stkobjects.MTO.graphics
    :type: MTOGraphics

    Get the MTO's 2D Graphics properties.

.. py:property:: graphics_3d
    :canonical: br.steak.core.stkobjects.MTO.graphics_3d
    :type: MTOGraphics3D

    Get the MTO's 3D Graphics properties.

.. py:property:: tracks
    :canonical: br.steak.core.stkobjects.MTO.tracks
    :type: MTOTrackCollection

    Get the collection of MTO tracks.


