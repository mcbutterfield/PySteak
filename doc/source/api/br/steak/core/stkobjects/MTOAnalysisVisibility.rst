MTOAnalysisVisibility
=====================

.. py:class:: br.steak.core.stkobjects.MTOAnalysisVisibility

   MTO Visibility Computation.

.. py:currentmodule:: MTOAnalysisVisibility

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.MTOAnalysisVisibility.are_all_tracks_visible`
              - Return true if all tracks are visible to the object.
            * - :py:attr:`~br.steak.core.stkobjects.MTOAnalysisVisibility.are_tracks_visible`
              - Return true if any track in the array is visible to the object.
            * - :py:attr:`~br.steak.core.stkobjects.MTOAnalysisVisibility.compute_all_tracks`
              - Return an array of track ids with a bool value indicating if it's visible to the specified object.
            * - :py:attr:`~br.steak.core.stkobjects.MTOAnalysisVisibility.compute_tracks`
              - Return an array of track ids with a bool value indicating if it's visible to the specified object.
            * - :py:attr:`~br.steak.core.stkobjects.MTOAnalysisVisibility.show_any_track`
              - Return true if any track is visible to the object.
            * - :py:attr:`~br.steak.core.stkobjects.MTOAnalysisVisibility.show_track`
              - Return true is the track is visible to the object.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.MTOAnalysisVisibility.entirety`
              - Visibility Entirety.
            * - :py:attr:`~br.steak.core.stkobjects.MTOAnalysisVisibility.object_data`
              - If the Object to which range will be computed is an MTO, use this option to specify the track that will be used to compute that range. By default the MTO's ComputeTrack will be used.
            * - :py:attr:`~br.steak.core.stkobjects.MTOAnalysisVisibility.object_interval`
              - Use Extended to use the last point of the ephemeris span of the object for times past the last point. Default is Normal.
            * - :py:attr:`~br.steak.core.stkobjects.MTOAnalysisVisibility.object_path`
              - Get or set the object used for the visibility computation.
            * - :py:attr:`~br.steak.core.stkobjects.MTOAnalysisVisibility.use_terrain`
              - Indicate whether to use terrain instead of line of sight. Default is Terrain Off.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import MTOAnalysisVisibility


Property detail
---------------

.. py:property:: entirety
    :canonical: br.steak.core.stkobjects.MTOAnalysisVisibility.entirety
    :type: MTOEntirety

    Visibility Entirety.

.. py:property:: object_data
    :canonical: br.steak.core.stkobjects.MTOAnalysisVisibility.object_data
    :type: int

    If the Object to which range will be computed is an MTO, use this option to specify the track that will be used to compute that range. By default the MTO's ComputeTrack will be used.

.. py:property:: object_interval
    :canonical: br.steak.core.stkobjects.MTOAnalysisVisibility.object_interval
    :type: MTOObjectInterval

    Use Extended to use the last point of the ephemeris span of the object for times past the last point. Default is Normal.

.. py:property:: object_path
    :canonical: br.steak.core.stkobjects.MTOAnalysisVisibility.object_path
    :type: str

    Get or set the object used for the visibility computation.

.. py:property:: use_terrain
    :canonical: br.steak.core.stkobjects.MTOAnalysisVisibility.use_terrain
    :type: bool

    Indicate whether to use terrain instead of line of sight. Default is Terrain Off.


Method detail
-------------

.. py:method:: are_all_tracks_visible(self, time: typing.Any) -> bool
    :canonical: br.steak.core.stkobjects.MTOAnalysisVisibility.are_all_tracks_visible

    Return true if all tracks are visible to the object.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~bool`

.. py:method:: are_tracks_visible(self, eval: MTOTrackEvaluationType, track_ids: list, time: typing.Any) -> bool
    :canonical: br.steak.core.stkobjects.MTOAnalysisVisibility.are_tracks_visible

    Return true if any track in the array is visible to the object.

    :Parameters:

        **eval** : :obj:`~MTOTrackEvaluationType`

        **track_ids** : :obj:`~list`

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~bool`

.. py:method:: compute_all_tracks(self, mode: MTOVisibilityMode, time: typing.Any) -> list
    :canonical: br.steak.core.stkobjects.MTOAnalysisVisibility.compute_all_tracks

    Return an array of track ids with a bool value indicating if it's visible to the specified object.

    :Parameters:

        **mode** : :obj:`~MTOVisibilityMode`

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`

.. py:method:: compute_tracks(self, mode: MTOVisibilityMode, track_ids: list, time: typing.Any) -> list
    :canonical: br.steak.core.stkobjects.MTOAnalysisVisibility.compute_tracks

    Return an array of track ids with a bool value indicating if it's visible to the specified object.

    :Parameters:

        **mode** : :obj:`~MTOVisibilityMode`

        **track_ids** : :obj:`~list`

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~list`



.. py:method:: show_any_track(self, time: typing.Any) -> bool
    :canonical: br.steak.core.stkobjects.MTOAnalysisVisibility.show_any_track

    Return true if any track is visible to the object.

    :Parameters:

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~bool`

.. py:method:: show_track(self, track_id: int, time: typing.Any) -> bool
    :canonical: br.steak.core.stkobjects.MTOAnalysisVisibility.show_track

    Return true is the track is visible to the object.

    :Parameters:

        **track_id** : :obj:`~int`

        **time** : :obj:`~typing.Any`


    :Returns:

        :obj:`~bool`









