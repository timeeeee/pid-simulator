from time import time


class Blackbox(object):
    """Model the state and behavior of a blackbox we are trying to control."""
    pass


class Controller(object):
    """Determine a control variable to manage the blackbox."""
    pass


class View(object):
    """Display the state of the blackbox and controller to the user."""
    pass


def run(blackbox, controller, view):
    prev_time = time()  # First dt will be basically 0
    
    while True:
        # Calculate time since last step
        current_time = time()
        dt = current_time - prev_time
        prev_time = current_time

        # Call update function on Controller

        # Call update function on Blackbox

        # Send data to view
        


if __name__ == "__main__":
    run(0, 0, 0)
