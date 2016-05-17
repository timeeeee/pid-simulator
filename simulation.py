from time import time


def simulate(blackbox, controller, view):
    prev_time = time()  # First dt will be basically 0
    
    while True:
        # Calculate time since last step
        current_time = time()
        dt = current_time - prev_time
        prev_time = current_time

        # Tick controller and blackbox
        controller.update(dt)
        blackbox.update(dt)

        # Get state
        control_variable = controller.get_output()
        blackbox_output = blackbox.get_output()

        controller.set_input(blackbox_output)
        blackbox.set_input(control_variable)

        # Send data to view
        view.update(current_time, control_variable, blackbox_output)
