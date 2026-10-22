IOrientationQuaternion
======================

.. py:class:: br.steak.core.stkutil.IOrientationQuaternion

   Bases: IOrientation

   Quaternion representing orientation between two sets of axes.

.. py:currentmodule:: IOrientationQuaternion

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~br.steak.core.stkutil.IOrientationQuaternion.qs`
              - Get or set the scalar component of the quaternion. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QS = cos(A/2). Dimensionless.
            * - :py:attr:`~br.steak.core.stkutil.IOrientationQuaternion.qx`
              - Get or set the first element of the vector component of the quaternion. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QX = nx sin(A/2). Dimensionless.
            * - :py:attr:`~br.steak.core.stkutil.IOrientationQuaternion.qy`
              - Get or set the second element of the vector component of the quaternion. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QY = ny sin(A/2). Dimensionless.
            * - :py:attr:`~br.steak.core.stkutil.IOrientationQuaternion.qz`
              - Get or set the third element of the vector component of the quaternion. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QZ = nz sin(A/2). Dimensionless.


Import detail
-------------

.. code-block:: python

    from br.steak.core.stkutil import IOrientationQuaternion


Property detail
---------------

.. py:property:: qs
    :canonical: br.steak.core.stkutil.IOrientationQuaternion.qs
    :type: float

    Get or set the scalar component of the quaternion. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QS = cos(A/2). Dimensionless.

.. py:property:: qx
    :canonical: br.steak.core.stkutil.IOrientationQuaternion.qx
    :type: float

    Get or set the first element of the vector component of the quaternion. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QX = nx sin(A/2). Dimensionless.

.. py:property:: qy
    :canonical: br.steak.core.stkutil.IOrientationQuaternion.qy
    :type: float

    Get or set the second element of the vector component of the quaternion. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QY = ny sin(A/2). Dimensionless.

.. py:property:: qz
    :canonical: br.steak.core.stkutil.IOrientationQuaternion.qz
    :type: float

    Get or set the third element of the vector component of the quaternion. This quaternion is from the reference axes to the body frame; if n and A are the axis and angle of rotation, respectively, then QZ = nz sin(A/2). Dimensionless.


