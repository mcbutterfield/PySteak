ConstantDisplayCondition
========================

.. py:class:: br.steak.core.graphics.ConstantDisplayCondition

   Bases: :py:class:`~br.steak.core.graphics.IDisplayCondition`

   A display condition that evaluates to a user-defined value. This is commonly used to hide primitives by assigning to a primitive a display condition that always returns false.

.. py:currentmodule:: ConstantDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.ConstantDisplayCondition.display`
              - Get or set the value the display condition evaluates to.



Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import ConstantDisplayCondition


Property detail
---------------

.. py:property:: display
    :canonical: br.steak.core.graphics.ConstantDisplayCondition.display
    :type: bool

    Get or set the value the display condition evaluates to.


