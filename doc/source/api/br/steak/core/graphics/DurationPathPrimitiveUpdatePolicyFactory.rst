DurationPathPrimitiveUpdatePolicyFactory
========================================

.. py:class:: br.steak.core.graphics.DurationPathPrimitiveUpdatePolicyFactory

   path primitive update policy that removes points from remove location after a given duration.

.. py:currentmodule:: DurationPathPrimitiveUpdatePolicyFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.graphics.DurationPathPrimitiveUpdatePolicyFactory.initialize`
              - Construct a default update policy. This is equivalent to constructing a policy with duration set to 0 and a remove location of Front.
            * - :py:attr:`~br.steak.core.graphics.DurationPathPrimitiveUpdatePolicyFactory.initialize_with_parameters`
              - Initialize a policy with the specified duration and removeLocation.


Import detail
-------------

.. code-block:: python

    from br.steak.core.graphics import DurationPathPrimitiveUpdatePolicyFactory



Method detail
-------------

.. py:method:: initialize(self) -> DurationPathPrimitiveUpdatePolicy
    :canonical: br.steak.core.graphics.DurationPathPrimitiveUpdatePolicyFactory.initialize

    Construct a default update policy. This is equivalent to constructing a policy with duration set to 0 and a remove location of Front.

    :Returns:

        :obj:`~DurationPathPrimitiveUpdatePolicy`

.. py:method:: initialize_with_parameters(self, duration: float, remove_location: PathPrimitiveRemoveLocation) -> DurationPathPrimitiveUpdatePolicy
    :canonical: br.steak.core.graphics.DurationPathPrimitiveUpdatePolicyFactory.initialize_with_parameters

    Initialize a policy with the specified duration and removeLocation.

    :Parameters:

        **duration** : :obj:`~float`

        **remove_location** : :obj:`~PathPrimitiveRemoveLocation`


    :Returns:

        :obj:`~DurationPathPrimitiveUpdatePolicy`

