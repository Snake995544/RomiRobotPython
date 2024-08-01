from subsystems.drivetrain import Drivetrain
import typing
import commands2

class ArcadeDrive(commands2.Command):
    def __init__(self, drive:Drivetrain):
        super().__init__()
        self.drive = drive
        self.forward = typing.Callable[[], float]
        self.rotation = typing.Callable[[], float]
        self.addRequirements(self.drive)
    def execute(self) -> None:
        self.drive.drive(self.forward, self.rotation)