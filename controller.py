class Controller(object):
    """Set a control variable to manage a blackbox's behavior"""
    def set_input(self, value):
        """Tell controller the current blackbox state"""
        raise NotImplementedError(
            "set_input not implemented in controller class {}".format(
                self.__class__.__name__))

    def get_output(self):
        """Get control variable"""
        raise NotImplementedError(
            "get_output not implemented in controller class {}".format(
                self.__class__.__name__))

    def update(self, dt):
        """Calculate new values after time passes"""
        raise NotImplementedError(
            "update not implemented in controller class {}".format(
                self.__class__.__name__))


class PIController(Controller):
    """Use proportional and integral functions of error to control blackbox"""
    def __init__(self, K_p, K_i, target):
        """Instantiate PI controller with parameters K_p, K_i, target"""
        self.K_p = float(K_p)
        self.K_i = float(K_i)
        self.target = float(target)
        self.control_variable = 0.0

        self.blackbox_state = 0.0
        self.prev_error = 0.0
        self.integral = 0.0

    def set_input(self, value):
        """Tell controller the current blackbox state"""
        self.blackbox_state = value

    def get_output(self):
        """Get control variable"""
        return self.control_variable

    def update(self, dt):
        """Update controller for new time step, dt, in ms"""
        error = self.target - self.blackbox_state
        self.integral += (error + self.prev_error) * dt / 2
        prev_error = error

        self.control_variable = self.K_p * error + self.K_i * self.integral
