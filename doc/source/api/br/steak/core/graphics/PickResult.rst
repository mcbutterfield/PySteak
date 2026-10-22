PickResult
==========

.. py:class:: br.steak.core.graphics.PickResult

   A single result from Pick.

.. py:currentmodule:: PickResult

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.PickResult.depth`
              - Get the depth of the picked location in the 3D scene.
            * - :py:attr:`~br.steak.core.graphics.PickResult.objects`
              - Get a collection of objects that were on the pick stack for the picked object.
            * - :py:attr:`~br.steak.core.graphics.PickResult.position`
              - Get the position of the picked location in the central body's fixed reference frame. The array contains the components of the position arranged in the order x, y, z.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import PickResult


Property detail
---------------

.. py:property:: depth
    :canonical: br.steak.core.graphics.PickResult.depth
    :type: float

    Get the depth of the picked location in the 3D scene.

.. py:property:: objects
    :canonical: br.steak.core.graphics.PickResult.objects
    :type: ObjectCollection

    Get a collection of objects that were on the pick stack for the picked object.

.. py:property:: position
    :canonical: br.steak.core.graphics.PickResult.position
    :type: list

    Get the position of the picked location in the central body's fixed reference frame. The array contains the components of the position arranged in the order x, y, z.


