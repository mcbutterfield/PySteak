AttitudeControlImpulsiveFile
============================

.. py:class:: br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveFile

   Bases: :py:class:`~br.ok.core.stkobjects.astrogator.IAttitudeControlImpulsive`, :py:class:`~br.ok.core.stkobjects.astrogator.IAttitudeControl`, :py:class:`~br.ok.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The file attitude control for an impulsive maneuver.

.. py:currentmodule:: AttitudeControlImpulsiveFile

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.delta_v_magnitude`
              - Get or set the size of the delta-V to be applied to the orbit along the specified direction. Uses Rate Dimension.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.file_time_offset`
              - Get or set the time offset can be used to adjust the time stored in the attitude file. Dimensionless.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.filename`
              - Get or set the attitude file to use.
            * - :py:attr:`~br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.full_filename`
              - Get the full path and name of the attitude file to use.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects.astrogator import AttitudeControlImpulsiveFile


Property detail
---------------

.. py:property:: delta_v_magnitude
    :canonical: br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.delta_v_magnitude
    :type: float

    Get or set the size of the delta-V to be applied to the orbit along the specified direction. Uses Rate Dimension.

.. py:property:: file_time_offset
    :canonical: br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.file_time_offset
    :type: float

    Get or set the time offset can be used to adjust the time stored in the attitude file. Dimensionless.

.. py:property:: filename
    :canonical: br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.filename
    :type: str

    Get or set the attitude file to use.

.. py:property:: full_filename
    :canonical: br.ok.core.stkobjects.astrogator.AttitudeControlImpulsiveFile.full_filename
    :type: str

    Get the full path and name of the attitude file to use.


