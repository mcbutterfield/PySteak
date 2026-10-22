Graphics3DLabelSwapDistance
===========================

.. py:class:: br.ok.core.stkobjects.Graphics3DLabelSwapDistance

   Control the level of detail in labels and other screen objects at specified distances.

.. py:currentmodule:: Graphics3DLabelSwapDistance

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DLabelSwapDistance.set_distance_level`
              - Select the screen object(s) for which swapping occurs at the specified distance.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DLabelSwapDistance.distance_level`
              - Get Distance Level.
            * - :py:attr:`~br.ok.core.stkobjects.Graphics3DLabelSwapDistance.distance_value`
              - Distance at which one level of detail is swapped for another. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import Graphics3DLabelSwapDistance


Property detail
---------------

.. py:property:: distance_level
    :canonical: br.ok.core.stkobjects.Graphics3DLabelSwapDistance.distance_level
    :type: Graphics3DLabelSwapDistanceType

    Get Distance Level.

.. py:property:: distance_value
    :canonical: br.ok.core.stkobjects.Graphics3DLabelSwapDistance.distance_value
    :type: float

    Distance at which one level of detail is swapped for another. Uses Distance Dimension.


Method detail
-------------




.. py:method:: set_distance_level(self, value: Graphics3DLabelSwapDistanceType) -> None
    :canonical: br.ok.core.stkobjects.Graphics3DLabelSwapDistance.set_distance_level

    Select the screen object(s) for which swapping occurs at the specified distance.

    :Parameters:

        **value** : :obj:`~Graphics3DLabelSwapDistanceType`


    :Returns:

        :obj:`~None`

