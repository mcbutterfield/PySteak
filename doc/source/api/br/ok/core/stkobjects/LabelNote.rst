LabelNote
=========

.. py:class:: br.ok.core.stkobjects.LabelNote

   Class defining label notes.

.. py:currentmodule:: LabelNote

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.LabelNote.intervals`
              - Intervals during which the note is displayed. This property is used if the corresponding value is selected for the NoteVisible property.
            * - :py:attr:`~br.ok.core.stkobjects.LabelNote.note`
              - Note property.
            * - :py:attr:`~br.ok.core.stkobjects.LabelNote.show_label`
              - Property specifying whether the label is displayed.
            * - :py:attr:`~br.ok.core.stkobjects.LabelNote.show_note`
              - Property specifying when the note is displayed. A member of the NoteShowType enumeration.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import LabelNote


Property detail
---------------

.. py:property:: intervals
    :canonical: br.ok.core.stkobjects.LabelNote.intervals
    :type: TimeIntervalCollection

    Intervals during which the note is displayed. This property is used if the corresponding value is selected for the NoteVisible property.

.. py:property:: note
    :canonical: br.ok.core.stkobjects.LabelNote.note
    :type: str

    Note property.

.. py:property:: show_label
    :canonical: br.ok.core.stkobjects.LabelNote.show_label
    :type: bool

    Property specifying whether the label is displayed.

.. py:property:: show_note
    :canonical: br.ok.core.stkobjects.LabelNote.show_note
    :type: NoteShowType

    Property specifying when the note is displayed. A member of the NoteShowType enumeration.


