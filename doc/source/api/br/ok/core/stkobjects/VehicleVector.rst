VehicleVector
=============

.. py:class:: br.ok.core.stkobjects.VehicleVector

   Aligned and Constrained attitude profile.

.. py:currentmodule:: VehicleVector

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.stkobjects.VehicleVector.available_reference_vectors`
              - Return the available reference vectors.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleVector.body`
              - Get the body-fixed vector that is aligned or constrained with respect to the reference vector.
            * - :py:attr:`~br.ok.core.stkobjects.VehicleVector.reference_vector`
              - Get or set the reference vector with respect to which the body-fixed vector is aligned or constrained.



Import detail
-------------

.. code-block:: python

    from br.ok.core.stkobjects import VehicleVector


Property detail
---------------

.. py:property:: available_reference_vectors
    :canonical: br.ok.core.stkobjects.VehicleVector.available_reference_vectors
    :type: list

    Return the available reference vectors.

.. py:property:: body
    :canonical: br.ok.core.stkobjects.VehicleVector.body
    :type: IDirection

    Get the body-fixed vector that is aligned or constrained with respect to the reference vector.

.. py:property:: reference_vector
    :canonical: br.ok.core.stkobjects.VehicleVector.reference_vector
    :type: str

    Get or set the reference vector with respect to which the body-fixed vector is aligned or constrained.


