class View(object):
    """Display blackbox and controller interaction"""
    def update(self, time, control_variable, blackbox_output):
        """Update view for a time step"""
        raise NotImplementedError(
            "update function not implemented for view class {}".format(
                self.__class__.__name__))


class PrintView(View):
    """Print blackbox and controller interaction to terminal"""
    def __init__(self):
        pass

    def update(self, time, control_variable, blackbox_output):
        print "t = {}, control variable = {}, blackbox output = {}".format(
            time, control_variable, blackbox_output)
