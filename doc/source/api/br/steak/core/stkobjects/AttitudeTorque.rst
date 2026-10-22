AttitudeTorque
==============

.. py:class:: br.steak.core.stkobjects.AttitudeTorque

   Torque file to use in defining integrated attitude.

.. py:currentmodule:: AttitudeTorque

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.AttitudeTorque.torque_filename`
              - Name of external torque (.tq) file. Torque files define a time-ordered list of body-fixed torques to be applied to the satellite.
            * - :py:attr:`~br.steak.core.stkobjects.AttitudeTorque.use_torque_file`
              - Opt whether to use an external torque file.



Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects import AttitudeTorque


Property detail
---------------

.. py:property:: torque_filename
    :canonical: br.steak.core.stkobjects.AttitudeTorque.torque_filename
    :type: str

    Name of external torque (.tq) file. Torque files define a time-ordered list of body-fixed torques to be applied to the satellite.

.. py:property:: use_torque_file
    :canonical: br.steak.core.stkobjects.AttitudeTorque.use_torque_file
    :type: bool

    Opt whether to use an external torque file.


