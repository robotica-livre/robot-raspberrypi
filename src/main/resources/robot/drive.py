
class SimpleDrive(object):

    def __init__(self):
        self.board = RaspiRobot()

    def forward(self):
        self.board.forward()

    def backward(self):
        self.board.reverse()

    def left(self):
        self.board.left()

    def right(self):
        self.board.right()

    def stop(self):
        self.board.stop()

class PidDriver(object):

    def __init__(self):
        self.board = RaspiRobot()

    def lineFollowing(self):
        # TODO: Implement PID
        pass
