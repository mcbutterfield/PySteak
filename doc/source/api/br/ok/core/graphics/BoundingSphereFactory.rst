BoundingSphereFactory
=====================

.. py:class:: br.ok.core.graphics.BoundingSphereFactory

   Create bounding spheres.

.. py:currentmodule:: BoundingSphereFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.BoundingSphereFactory.initialize`
              - Create instances of BoundingSphere.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.BoundingSphereFactory.maximum_radius_bounding_sphere`
              - Get the bounding sphere of maximum possible radius.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import BoundingSphereFactory


Property detail
---------------

.. py:property:: maximum_radius_bounding_sphere
    :canonical: br.ok.core.graphics.BoundingSphereFactory.maximum_radius_bounding_sphere
    :type: BoundingSphere

    Get the bounding sphere of maximum possible radius.


Method detail
-------------

.. py:method:: initialize(self, center: list, radius: float) -> BoundingSphere
    :canonical: br.ok.core.graphics.BoundingSphereFactory.initialize

    Create instances of BoundingSphere.

    :Parameters:

        **center** : :obj:`~list`

        **radius** : :obj:`~float`


    :Returns:

        :obj:`~BoundingSphere`


