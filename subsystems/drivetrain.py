# This is the drivetrain
import commands2
import wpilib
import wpilib.drive
import typing
class Drivetrain(commands2.Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.leftMotor = wpilib.PWMSparkMax(0)
        self.rightMotor = wpilib.PWMSparkMax(1)
        self.rightMotor.setInverted(True)
        self.robotDrive = wpilib.drive._drive.DifferentialDrive(self.leftMotor, self.rightMotor)
    def arcade_drive(self, forward_speed: float, rotation: float) -> None:
        self.robotDrive.arcadeDrive(forward_speed, rotation)
