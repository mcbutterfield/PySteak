Cartesian2Vector
================

.. py:class:: br.ok.core.stkutil.Cartesian2Vector

   A 2-D cartesian vector.

.. py:currentmodule:: Cartesian2Vector

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkutil.Cartesian2Vector.get`
              - Return cartesian vector.
            * - :py:attr:`~br.ok.core.stkutil.Cartesian2Vector.set`
              - Set cartesian vector.
            * - :py:attr:`~br.ok.core.stkutil.Cartesian2Vector.to_array`
              - Return coordinates as an array.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkutil.Cartesian2Vector.x`
              - X coordinate.
            * - :py:attr:`~br.ok.core.stkutil.Cartesian2Vector.y`
              - Y coordinate.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkutil import Cartesian2Vector


Property detail
---------------

.. py:property:: x
    :canonical: br.ok.core.stkutil.Cartesian2Vector.x
    :type: float

    X coordinate.

.. py:property:: y
    :canonical: br.ok.core.stkutil.Cartesian2Vector.y
    :type: float

    Y coordinate.


Method detail
-------------

.. py:method:: get(self) -> typing.Tuple[float, float]
    :canonical: br.ok.core.stkutil.Cartesian2Vector.get

    Return cartesian vector.

    :Returns:

        :obj:`~typing.Tuple[float, float]`

.. py:method:: set(self, x: float, y: float) -> None
    :canonical: br.ok.core.stkutil.Cartesian2Vector.set

    Set cartesian vector.

    :Parameters:

        **x** : :obj:`~float`

        **y** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: to_array(self) -> list
    :canonical: br.ok.core.stkutil.Cartesian2Vector.to_array

    Return coordinates as an array.

    :Returns:

        :obj:`~list`





