#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#
import constants

import typing

import commands2
import commands2.button
import wpilib

from commands.arcadedrive import ArcadeDrive
#from commands.autonomous_distance import AutonomousDistance
#from commands.autonomous_time import AutonomousTime

from subsystems.drivetrain import Drivetrain


class RobotContainer:
    """
    This class is where the bulk of the robot should be declared. Since Command-based is a
    "declarative" paradigm, very little robot logic should actually be handled in the :class:`.Robot`
    periodic methods (other than the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self) -> None:
        # The robot's subsystems and commands are defined here...

        # Assumes a gamepad plugged into channnel 0
        self.controller = wpilib.Joystick(constants.DRIVE_JOYSTICK_PORT)

        # Create SmartDashboard chooser for autonomous routines
        self.chooser = wpilib.SendableChooser()
        self.drivetrain = Drivetrain()
        self.drivetrain.setDefaultCommand(self.getDrive())
        
        # NOTE: The I/O pin functionality of the 5 exposed I/O pins depends on the hardware "overlay"
        # that is specified when launching the wpilib-ws server on the Romi raspberry pi.
        # By default, the following are available (listed in order from inside of the board to outside):
        # - DIO 8 (mapped to Arduino pin 11, closest to the inside of the board)
        # - Analog In 0 (mapped to Analog Channel 6 / Arduino Pin 4)
        # - Analog In 1 (mapped to Analog Channel 2 / Arduino Pin 20)
        # - PWM 2 (mapped to Arduino Pin 21)
        # - PWM 3 (mapped to Arduino Pin 22)
        #
        # Your subsystem configuration should take the overlays into account

        self._configureButtonBindings()

    def getDrive(self):
        return ArcadeDrive(self.drivetrain, lambda: -self.controller.getY(), lambda: -self.controller.getX())

    def _configureButtonBindings(self):
        """Use this method to define your button->command mappings. Buttons can be created by
        instantiating a :class:`.GenericHID` or one of its subclasses (:class`.Joystick or
        :class:`.XboxController`), and then passing it to a :class:`.JoystickButton`.
        """

        # Setup SmartDashboard options
        #self.chooser.setDefaultOption(
        #    "Auto Routine Distance", AutonomousDistance(self.drivetrain)
        #)
        #self.chooser.addOption("Auto Routine Time", AutonomousTime(self.drivetrain))
        #wpilib.SmartDashboard.putData(self.chooser)

    def getAutonomousCommand(self) -> typing.Optional[commands2.Command]:
        return self.chooser.getSelected()
