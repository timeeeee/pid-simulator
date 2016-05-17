class Blackbox(object):
    """Model a process with an input, output, and state"""
    def set_input(self, value):
        """Tell the blackbox a control variable"""
        raise NotImplementedError(
            "set_input not implemented in blackbox class {}".format(
                self.__class__.__name__))

    def get_output(self):
        """Get current output state"""
        raise NotImplementedError(
            "get_output not implemented in blackbox class {}".format(
                self.__class__.__name__))

    def update(self, dt):
        """Calculate new values after time passes"""
        raise NotImplementedError(
            "update not implemented in blackbox class {}".format(
                self.__class__.__name__))


class FactorBlackbox(Blackbox):
    """Output is equal to the input times a factor, with no time delay"""
    def __init__(self, factor):
        """Initialize a 'Factor' blackbox with factor"""
        self.factor = factor
        self.input_ = 0
        self.output = 0

    def set_input(self, value):
        """Tell the blackbox a control variable"""
        self.input_ = value

    def get_output(self):
        """Get current blackbox output"""
        return self.output

    def update(self, dt):
        """Ignore time passed, just update output value"""
        self.output = self.input_ * self.factor
