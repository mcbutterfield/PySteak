AntennaControl
==============

.. py:class:: br.steak.core.stkobjects.AntennaControl

   Class defining the properties for a antenna control.

.. py:currentmodule:: AntennaControl

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AntennaControl.embedded_model_component_linking`
              - Get the link/embed controller for managing the embedded antenna model component.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaControl.embedded_model_orientation`
              - Get or set the antenna orientation.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaControl.linked_antenna_object`
              - Get or set the linked antenna object.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaControl.reference_type`
              - Get or set the antenna control reference type.
            * - :py:attr:`~br.steak.core.stkobjects.AntennaControl.supported_linked_antenna_objects`
              - Get an array of available antenna objects that this object can link to and use.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AntennaControl


Property detail
---------------

.. py:property:: embedded_model_component_linking
    :canonical: br.steak.core.stkobjects.AntennaControl.embedded_model_component_linking
    :type: IComponentLinkEmbedControl

    Get the link/embed controller for managing the embedded antenna model component.

.. py:property:: embedded_model_orientation
    :canonical: br.steak.core.stkobjects.AntennaControl.embedded_model_orientation
    :type: IOrientation

    Get or set the antenna orientation.

.. py:property:: linked_antenna_object
    :canonical: br.steak.core.stkobjects.AntennaControl.linked_antenna_object
    :type: str

    Get or set the linked antenna object.

.. py:property:: reference_type
    :canonical: br.steak.core.stkobjects.AntennaControl.reference_type
    :type: AntennaControlReferenceType

    Get or set the antenna control reference type.

.. py:property:: supported_linked_antenna_objects
    :canonical: br.steak.core.stkobjects.AntennaControl.supported_linked_antenna_objects
    :type: list

    Get an array of available antenna objects that this object can link to and use.


