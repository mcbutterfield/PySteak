IProfile
========

.. py:class:: br.steak.core.stkobjects.astrogator.IProfile

   General properties for target sequence profiles.

.. py:currentmodule:: IProfile

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.IProfile.copy`
              - Make a copy of the profile.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkobjects.astrogator.IProfile.mode`
              - Get or set the profile's mode.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.IProfile.name`
              - Get or set the name of the profile.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.IProfile.status`
              - Get or set the status of the profile.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.IProfile.type`
              - Return the current profile type.
            * - :py:attr:`~br.steak.core.stkobjects.astrogator.IProfile.user_comment`
              - A user comment.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkobjects.astrogator import IProfile


Property detail
---------------

.. py:property:: mode
    :canonical: br.steak.core.stkobjects.astrogator.IProfile.mode
    :type: ProfileMode

    Get or set the profile's mode.

.. py:property:: name
    :canonical: br.steak.core.stkobjects.astrogator.IProfile.name
    :type: str

    Get or set the name of the profile.

.. py:property:: status
    :canonical: br.steak.core.stkobjects.astrogator.IProfile.status
    :type: str

    Get or set the status of the profile.

.. py:property:: type
    :canonical: br.steak.core.stkobjects.astrogator.IProfile.type
    :type: Profile

    Return the current profile type.

.. py:property:: user_comment
    :canonical: br.steak.core.stkobjects.astrogator.IProfile.user_comment
    :type: str

    A user comment.


Method detail
-------------

.. py:method:: copy(self) -> IProfile
    :canonical: br.steak.core.stkobjects.astrogator.IProfile.copy

    Make a copy of the profile.

    :Returns:

        :obj:`~IProfile`









