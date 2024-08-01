# Drivetrain class
import wpilib
import wpilib.drive
import commands2
class Drivetrain(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        self.leftDrive = wpilib.PWMSparkMax(0)
        self.rightDrive = wpilib.PWMSparkMax(1)
        self.robotDrive = wpilib.drive.DifferentialDrive(
            self.leftDrive, self.rightDrive
        )
    def drive(self, controllerX, controllerY):
        self.robotDrive.arcadeDrive(controllerX, controllerY)