CompositePrimitiveFactory
=========================

.. py:class:: br.ok.core.graphics.CompositePrimitiveFactory

   A primitive that is composed of multiple other primitives. Since composites can contain other composites, they are commonly used to build hierarchies of primitives to efficiently evaluate display conditions...

.. py:currentmodule:: CompositePrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.CompositePrimitiveFactory.initialize`
              - Initialize a default composite primitive.


Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import CompositePrimitiveFactory



Method detail
-------------

.. py:method:: initialize(self) -> CompositePrimitive
    :canonical: br.ok.core.graphics.CompositePrimitiveFactory.initialize

    Initialize a default composite primitive.

    :Returns:

        :obj:`~CompositePrimitive`

