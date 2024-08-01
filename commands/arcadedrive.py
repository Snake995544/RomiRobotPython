from subsystems.drivetrain import Drivetrain
import typing
import commands2

class ArcadeDrive(commands2.Command):
    def __init__(self, drive:Drivetrain, forward: typing.Callable[[], float], rotation: typing.Callable[[], float]):
        super().__init__()
        self.drive = drive
        self.forward = forward
        self.rotation = rotation
        self.addRequirements(self.drive)
    def execute(self) -> None:
        self.drive.drive(self.forward(), self.rotation())