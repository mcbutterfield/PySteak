DurationPathPrimitiveUpdatePolicy
=================================

.. py:class:: br.ok.core.graphics.DurationPathPrimitiveUpdatePolicy

   Bases: :py:class:`~br.ok.core.graphics.IPathPrimitiveUpdatePolicy`

   path primitive update policy that removes points from remove location after a given duration.

.. py:currentmodule:: DurationPathPrimitiveUpdatePolicy

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.DurationPathPrimitiveUpdatePolicy.duration`
              - Get or set the maximum duration that a point will lie on the line.
            * - :py:attr:`~br.ok.core.graphics.DurationPathPrimitiveUpdatePolicy.remove_location`
              - Get or set where the positions on the path are removed from.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import DurationPathPrimitiveUpdatePolicy


Property detail
---------------

.. py:property:: duration
    :canonical: br.ok.core.graphics.DurationPathPrimitiveUpdatePolicy.duration
    :type: float

    Get or set the maximum duration that a point will lie on the line.

.. py:property:: remove_location
    :canonical: br.ok.core.graphics.DurationPathPrimitiveUpdatePolicy.remove_location
    :type: PathPrimitiveRemoveLocation

    Get or set where the positions on the path are removed from.


