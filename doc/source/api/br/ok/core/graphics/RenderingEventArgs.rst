RenderingEventArgs
==================

.. py:class:: br.ok.core.graphics.RenderingEventArgs

   The event is raised when the scene is rendered.

.. py:currentmodule:: RenderingEventArgs

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.ok.core.graphics.RenderingEventArgs.time`
              - The time of the rendering event.
            * - :py:attr:`~br.ok.core.graphics.RenderingEventArgs.time_in_ep_secs`
              - The time of the rendering event (in STK's scenario epoch units).



Import detail
-------------

.. code-block:: python

    from br.ok.core.graphics import RenderingEventArgs


Property detail
---------------

.. py:property:: time
    :canonical: br.ok.core.graphics.RenderingEventArgs.time
    :type: Date

    The time of the rendering event.

.. py:property:: time_in_ep_secs
    :canonical: br.ok.core.graphics.RenderingEventArgs.time_in_ep_secs
    :type: float

    The time of the rendering event (in STK's scenario epoch units).


