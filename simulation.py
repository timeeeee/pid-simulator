from time import time


def simulate(blackbox, controller, view):
    start_time = time()
    prev_time = 0.0  # First dt will be basically 0
    
    while True:
        # Calculate time since last step
        current_time = time() - start_time
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
