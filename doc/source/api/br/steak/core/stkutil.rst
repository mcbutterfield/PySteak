
The ``stkutil`` module
======================


.. py:module:: br.steak.core.stkutil


Summary
-------

.. tab-set::


    .. tab-item:: Interfaces

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~br.steak.core.stkutil.ICartesian3Vector`
              - Represents a cartesian 3-D vector.

            * - :py:class:`~br.steak.core.stkutil.IDirection`
              - Interface to set and retrieve direction options for aligned and constrained vectors.

            * - :py:class:`~br.steak.core.stkutil.ILocationData`
              - Base interface ILocationData. IPosition derives from this interface.

            * - :py:class:`~br.steak.core.stkutil.IOrbitState`
              - Interface to set and retrieve the coordinate type used to specify the orbit state.

            * - :py:class:`~br.steak.core.stkutil.IOrientation`
              - Interface to set and retrieve the orientation method.

            * - :py:class:`~br.steak.core.stkutil.IOrientationAzEl`
              - Interface for AzEl orientation method.

            * - :py:class:`~br.steak.core.stkutil.IOrientationEulerAngles`
              - Interface for Euler Angles orientation method.

            * - :py:class:`~br.steak.core.stkutil.IOrientationPositionOffset`
              - Interface for defining the orientation origin position offset relative to the parent object.

            * - :py:class:`~br.steak.core.stkutil.IOrientationQuaternion`
              - Quaternion representing orientation between two sets of axes.

            * - :py:class:`~br.steak.core.stkutil.IOrientationYPRAngles`
              - Interface for Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :py:class:`~br.steak.core.stkutil.IPosition`
              - IPosition provides access to the position of the object.

            * - :py:class:`~br.steak.core.stkutil.IRuntimeTypeInfoProvider`
              - Access point for RuntimeTypeInfo.


    .. tab-item:: Classes

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~br.steak.core.stkutil.Cartesian`
              - Class used to access a position using Cartesian Coordinates.

            * - :py:class:`~br.steak.core.stkutil.Cartesian2Vector`
              - A 2-D cartesian vector.

            * - :py:class:`~br.steak.core.stkutil.Cartesian3Vector`
              - A 3-D cartesian vector.

            * - :py:class:`~br.steak.core.stkutil.CommRadOrientationAzEl`
              - AzEl orientation method.

            * - :py:class:`~br.steak.core.stkutil.CommRadOrientationEulerAngles`
              - Euler Angles orientation method.

            * - :py:class:`~br.steak.core.stkutil.CommRadOrientationOffsetCart`
              - Orientation offset cartesian.

            * - :py:class:`~br.steak.core.stkutil.CommRadOrientationQuaternion`
              - Quaternion orientation method.

            * - :py:class:`~br.steak.core.stkutil.CommRadOrientationYPRAngles`
              - Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :py:class:`~br.steak.core.stkutil.ConversionUtility`
              - Object that contains a unit conversion utility.

            * - :py:class:`~br.steak.core.stkutil.Cylindrical`
              - Class defining cylindrical position.

            * - :py:class:`~br.steak.core.stkutil.Date`
              - Object that contains a date.

            * - :py:class:`~br.steak.core.stkutil.Direction`
              - Class defining direction options for aligned and constrained vectors.

            * - :py:class:`~br.steak.core.stkutil.DirectionEuler`
              - Euler direction sequence.

            * - :py:class:`~br.steak.core.stkutil.DirectionPR`
              - Pitch-Roll (PR) direction sequence.

            * - :py:class:`~br.steak.core.stkutil.DirectionRADec`
              - Spherical direction (Right Ascension and Declination).

            * - :py:class:`~br.steak.core.stkutil.DirectionXYZ`
              - Cartesian direction.

            * - :py:class:`~br.steak.core.stkutil.DoublesCollection`
              - A collection of doubles.

            * - :py:class:`~br.steak.core.stkutil.ExecuteCommandResult`
              - Collection of strings returned by the ExecuteCommand.

            * - :py:class:`~br.steak.core.stkutil.ExecuteMultipleCommandsResult`
              - Collection of objects returned by the ExecuteMultipleCommands.

            * - :py:class:`~br.steak.core.stkutil.Geocentric`
              - Class defining Geocentric position.

            * - :py:class:`~br.steak.core.stkutil.Geodetic`
              - Class defining Geodetic position.

            * - :py:class:`~br.steak.core.stkutil.Orientation`
              - Class defining the orientation of an orbit.

            * - :py:class:`~br.steak.core.stkutil.OrientationAzEl`
              - AzEl orientation method.

            * - :py:class:`~br.steak.core.stkutil.OrientationEulerAngles`
              - Euler Angles orientation method.

            * - :py:class:`~br.steak.core.stkutil.OrientationQuaternion`
              - Quaternion orientation method.

            * - :py:class:`~br.steak.core.stkutil.OrientationYPRAngles`
              - Yaw-Pitch Roll (YPR) Angles orientation system.

            * - :py:class:`~br.steak.core.stkutil.Planetocentric`
              - Class defining Planetocentric position.

            * - :py:class:`~br.steak.core.stkutil.Planetodetic`
              - Class defining Planetodetic position.

            * - :py:class:`~br.steak.core.stkutil.Position`
              - The Position class.

            * - :py:class:`~br.steak.core.stkutil.PropertyInfo`
              - Property Information coclass.

            * - :py:class:`~br.steak.core.stkutil.PropertyInfoCollection`
              - Property Information Collection coclass.

            * - :py:class:`~br.steak.core.stkutil.Quantity`
              - Object that contains a quantity.

            * - :py:class:`~br.steak.core.stkutil.RuntimeTypeInfo`
              - Runtime Type info coclass.

            * - :py:class:`~br.steak.core.stkutil.Spherical`
              - Class defining spherical position.

            * - :py:class:`~br.steak.core.stkutil.UnitPreferencesDimension`
              - Object that contains info on the Dimension.

            * - :py:class:`~br.steak.core.stkutil.UnitPreferencesDimensionCollection`
              - Object that contains a collection of dimensions.

            * - :py:class:`~br.steak.core.stkutil.UnitPreferencesUnit`
              - Object that contains info on the unit.

            * - :py:class:`~br.steak.core.stkutil.UnitPreferencesUnitCollection`
              - Object that contains a collection of UnitPreferencesUnit.


    .. tab-item:: Enums

        .. list-table::
            :header-rows: 0
            :widths: auto


            * - :py:class:`~br.steak.core.stkutil.AzElAboutBoresight`
              - About Boresight options for AzEl orientation method.

            * - :py:class:`~br.steak.core.stkutil.CoordinateSystem`
              - Earth-centered coordinate systems for defining certain propagators.

            * - :py:class:`~br.steak.core.stkutil.DirectionType`
              - Direction options for aligned and constrained vectors.

            * - :py:class:`~br.steak.core.stkutil.EulerDirectionSequence`
              - Euler direction sequences.

            * - :py:class:`~br.steak.core.stkutil.EulerOrientationSequenceType`
              - Euler rotation sequence options:.

            * - :py:class:`~br.steak.core.stkutil.ExecuteMultipleCommandsMode`
              - Enumeration defines a set of actions when an error occurs while executing a command batch.

            * - :py:class:`~br.steak.core.stkutil.FillStyle`
              - Fill Style.

            * - :py:class:`~br.steak.core.stkutil.LineStyle`
              - Line Style.

            * - :py:class:`~br.steak.core.stkutil.LogMessageDisplayID`
              - Log message destination options.

            * - :py:class:`~br.steak.core.stkutil.LogMessageType`
              - Log message types.

            * - :py:class:`~br.steak.core.stkutil.OrbitStateType`
              - Coordinate types used in specifying orbit state.

            * - :py:class:`~br.steak.core.stkutil.OrientationType`
              - Orientation methods.

            * - :py:class:`~br.steak.core.stkutil.PositionType`
              - Facility/place/target position types.

            * - :py:class:`~br.steak.core.stkutil.PropertyInfoValueType`
              - The enumeration used to determine what type of property is being used.

            * - :py:class:`~br.steak.core.stkutil.PRSequence`
              - Pitch-Roll (PR) direction sequences.

            * - :py:class:`~br.steak.core.stkutil.YPRAnglesSequence`
              - Yaw-Pitch-Roll (YPR) sequences.



Description
-----------

Objects and enumerations shared by the STK X and STK Objects libraries.

The
types provided by STK Util are used indirectly through methods and properties
in the STK X and STK Objects libraries.


.. py:currentmodule:: br.steak.core.stkutil


.. TABLE OF CONTENTS

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     ICartesian3Vector<stkutil/ICartesian3Vector>
     IDirection<stkutil/IDirection>
     ILocationData<stkutil/ILocationData>
     IOrbitState<stkutil/IOrbitState>
     IOrientation<stkutil/IOrientation>
     IOrientationAzEl<stkutil/IOrientationAzEl>
     IOrientationEulerAngles<stkutil/IOrientationEulerAngles>
     IOrientationPositionOffset<stkutil/IOrientationPositionOffset>
     IOrientationQuaternion<stkutil/IOrientationQuaternion>
     IOrientationYPRAngles<stkutil/IOrientationYPRAngles>
     IPosition<stkutil/IPosition>
     IRuntimeTypeInfoProvider<stkutil/IRuntimeTypeInfoProvider>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

     Cartesian<stkutil/Cartesian>
     Cartesian2Vector<stkutil/Cartesian2Vector>
     Cartesian3Vector<stkutil/Cartesian3Vector>
     CommRadOrientationAzEl<stkutil/CommRadOrientationAzEl>
     CommRadOrientationEulerAngles<stkutil/CommRadOrientationEulerAngles>
     CommRadOrientationOffsetCart<stkutil/CommRadOrientationOffsetCart>
     CommRadOrientationQuaternion<stkutil/CommRadOrientationQuaternion>
     CommRadOrientationYPRAngles<stkutil/CommRadOrientationYPRAngles>
     ConversionUtility<stkutil/ConversionUtility>
     Cylindrical<stkutil/Cylindrical>
     Date<stkutil/Date>
     Direction<stkutil/Direction>
     DirectionEuler<stkutil/DirectionEuler>
     DirectionPR<stkutil/DirectionPR>
     DirectionRADec<stkutil/DirectionRADec>
     DirectionXYZ<stkutil/DirectionXYZ>
     DoublesCollection<stkutil/DoublesCollection>
     ExecuteCommandResult<stkutil/ExecuteCommandResult>
     ExecuteMultipleCommandsResult<stkutil/ExecuteMultipleCommandsResult>
     Geocentric<stkutil/Geocentric>
     Geodetic<stkutil/Geodetic>
     Orientation<stkutil/Orientation>
     OrientationAzEl<stkutil/OrientationAzEl>
     OrientationEulerAngles<stkutil/OrientationEulerAngles>
     OrientationQuaternion<stkutil/OrientationQuaternion>
     OrientationYPRAngles<stkutil/OrientationYPRAngles>
     Planetocentric<stkutil/Planetocentric>
     Planetodetic<stkutil/Planetodetic>
     Position<stkutil/Position>
     PropertyInfo<stkutil/PropertyInfo>
     PropertyInfoCollection<stkutil/PropertyInfoCollection>
     Quantity<stkutil/Quantity>
     RuntimeTypeInfo<stkutil/RuntimeTypeInfo>
     Spherical<stkutil/Spherical>
     UnitPreferencesDimension<stkutil/UnitPreferencesDimension>
     UnitPreferencesDimensionCollection<stkutil/UnitPreferencesDimensionCollection>
     UnitPreferencesUnit<stkutil/UnitPreferencesUnit>
     UnitPreferencesUnitCollection<stkutil/UnitPreferencesUnitCollection>

.. toctree::
    :titlesonly:
    :maxdepth: 1
    :hidden:

    ≔ AzElAboutBoresight<stkutil/AzElAboutBoresight>
    ≔ CoordinateSystem<stkutil/CoordinateSystem>
    ≔ DirectionType<stkutil/DirectionType>
    ≔ EulerDirectionSequence<stkutil/EulerDirectionSequence>
    ≔ EulerOrientationSequenceType<stkutil/EulerOrientationSequenceType>
    ≔ ExecuteMultipleCommandsMode<stkutil/ExecuteMultipleCommandsMode>
    ≔ FillStyle<stkutil/FillStyle>
    ≔ LineStyle<stkutil/LineStyle>
    ≔ LogMessageDisplayID<stkutil/LogMessageDisplayID>
    ≔ LogMessageType<stkutil/LogMessageType>
    ≔ OrbitStateType<stkutil/OrbitStateType>
    ≔ OrientationType<stkutil/OrientationType>
    ≔ PositionType<stkutil/PositionType>
    ≔ PropertyInfoValueType<stkutil/PropertyInfoValueType>
    ≔ PRSequence<stkutil/PRSequence>
    ≔ YPRAnglesSequence<stkutil/YPRAnglesSequence>

