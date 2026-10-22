LabelNoteCollection
===================

.. py:class:: br.steak.core.stkobjects.LabelNoteCollection

   Collection representing label notes list.

.. py:currentmodule:: LabelNoteCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.LabelNoteCollection.add`
              - Add a label note to the collection.
            * - :py:attr:`~br.steak.core.stkobjects.LabelNoteCollection.item`
              - Get a LabelNote.
            * - :py:attr:`~br.steak.core.stkobjects.LabelNoteCollection.remove`
              - Remove an item given an index.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.LabelNoteCollection._new_enum`
              - Enumerates through the LabelNotes.
            * - :py:attr:`~br.steak.core.stkobjects.LabelNoteCollection.count`
              - Number of label notes.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import LabelNoteCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: br.steak.core.stkobjects.LabelNoteCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the LabelNotes.

.. py:property:: count
    :canonical: br.steak.core.stkobjects.LabelNoteCollection.count
    :type: int

    Number of label notes.


Method detail
-------------

.. py:method:: add(self, msg: str) -> LabelNote
    :canonical: br.steak.core.stkobjects.LabelNoteCollection.add

    Add a label note to the collection.

    :Parameters:

        **msg** : :obj:`~str`


    :Returns:

        :obj:`~LabelNote`


.. py:method:: item(self, index: int) -> LabelNote
    :canonical: br.steak.core.stkobjects.LabelNoteCollection.item

    Get a LabelNote.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~LabelNote`

.. py:method:: remove(self, index: int) -> None
    :canonical: br.steak.core.stkobjects.LabelNoteCollection.remove

    Remove an item given an index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`


