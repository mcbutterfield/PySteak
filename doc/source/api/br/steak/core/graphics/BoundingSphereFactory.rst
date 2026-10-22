BoundingSphereFactory
=====================

.. py:class:: br.steak.core.graphics.BoundingSphereFactory

   Create bounding spheres.

.. py:currentmodule:: BoundingSphereFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.BoundingSphereFactory.initialize`
              - Create instances of BoundingSphere.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.BoundingSphereFactory.maximum_radius_bounding_sphere`
              - Get the bounding sphere of maximum possible radius.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import BoundingSphereFactory


Property detail
---------------

.. py:property:: maximum_radius_bounding_sphere
    :canonical: br.steak.core.graphics.BoundingSphereFactory.maximum_radius_bounding_sphere
    :type: BoundingSphere

    Get the bounding sphere of maximum possible radius.


Method detail
-------------

.. py:method:: initialize(self, center: list, radius: float) -> BoundingSphere
    :canonical: br.steak.core.graphics.BoundingSphereFactory.initialize

    Create instances of BoundingSphere.

    :Parameters:

        **center** : :obj:`~list`

        **radius** : :obj:`~float`


    :Returns:

        :obj:`~BoundingSphere`


