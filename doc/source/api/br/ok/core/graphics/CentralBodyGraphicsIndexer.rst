CentralBodyGraphicsIndexer
==========================

.. py:class:: br.ok.core.graphics.CentralBodyGraphicsIndexer

   An indexer into the central body graphics for a particular central body, which provides graphical properties such as showing or hiding the central body in the scene, and working with terrain and imagery for the specified central body.

.. py:currentmodule:: CentralBodyGraphicsIndexer

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.CentralBodyGraphicsIndexer.get_by_name`
              - Return the central body graphics for the central body with the given name.
            * - :py:attr:`~br.ok.core.graphics.CentralBodyGraphicsIndexer.item`
              - Get the central body graphics for the specified central body.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.CentralBodyGraphicsIndexer.earth`
              - Get the central body graphics for the planet Earth. This is equivalent to passing a central body equal to an instance of earth central body to the indexer.
            * - :py:attr:`~br.ok.core.graphics.CentralBodyGraphicsIndexer.moon`
              - Get the central body graphics for the Moon.
            * - :py:attr:`~br.ok.core.graphics.CentralBodyGraphicsIndexer.sun`
              - Get the central body graphics for the Sun.



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import CentralBodyGraphicsIndexer


Property detail
---------------

.. py:property:: earth
    :canonical: br.ok.core.graphics.CentralBodyGraphicsIndexer.earth
    :type: CentralBodyGraphics

    Get the central body graphics for the planet Earth. This is equivalent to passing a central body equal to an instance of earth central body to the indexer.

.. py:property:: moon
    :canonical: br.ok.core.graphics.CentralBodyGraphicsIndexer.moon
    :type: CentralBodyGraphics

    Get the central body graphics for the Moon.

.. py:property:: sun
    :canonical: br.ok.core.graphics.CentralBodyGraphicsIndexer.sun
    :type: CentralBodyGraphics

    Get the central body graphics for the Sun.


Method detail
-------------


.. py:method:: get_by_name(self, name: str) -> CentralBodyGraphics
    :canonical: br.ok.core.graphics.CentralBodyGraphicsIndexer.get_by_name

    Return the central body graphics for the central body with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~CentralBodyGraphics`

.. py:method:: item(self, central_body: str) -> CentralBodyGraphics
    :canonical: br.ok.core.graphics.CentralBodyGraphicsIndexer.item

    Get the central body graphics for the specified central body.

    :Parameters:

        **central_body** : :obj:`~str`


    :Returns:

        :obj:`~CentralBodyGraphics`



