COMObject
=========

.. py:class:: br.ok.core.utilities.comobject.COMObject

   object

   Holds a raw COM pointer.

   May be returned from if the return argument is not part of the Object Model.

.. py:currentmodule:: COMObject


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.utilities.comobject.COMObject.get_pointer`
              - Return the COM object pointer as a ctypes.c_void_p.

Import detail
-------------

.. code-block:: python

    from br.ok.core.utilities.comobject import COMObject


Method detail
-------------

.. py:method:: get_pointer(self) -> c_void_p
    :canonical: br.ok.core.utilities.comobject.COMObject.get_pointer

    Return the COM object pointer as a ctypes.c_void_p.

    :Returns:

        :obj:`~c_void_p`


