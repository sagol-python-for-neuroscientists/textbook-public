"""
__author__ = Hagai Har-Gil
HW2 Question 3 Solution
"""
import random
import time


class Cell:
    """
    Abstract biological cell.
    Attributes: cell_id, cur_division_phase
    Methods: next_division_step
    """
    cell_division_phases = ['None', 'Interphase', 'Prophase',
                            'Metaphase', 'Anaphase', 'Telophase']  # this is a class variable,
                                                                   # available to all class instances

    def __init__(self, cell_id: str, cur_division_phase: str):
        self.cell_id = str(cell_id)
        assert isinstance(cur_division_phase, str)
        assert cur_division_phase in self.cell_division_phases
        self.cur_division_phase = cur_division_phase

    def next_division_step(self):
        """ Take the next step in the cell division process """
        cur_index = self.cell_division_phases.index(self.cur_division_phase)
        next_index = (cur_index + 1) % len(self.cell_division_phases)
        self.cur_division_phase = self.cell_division_phases[next_index]


class PyramidalNeuron(Cell):
    """
    A very coarse model of a pyramidal neuron.
    Mandatory attributes: cell_id, potential, synaptic_strength
    Mandatory methods: fire  # fires a spike
    """

    def __init__(self, cell_id, cur_division_phase, potential, synaptic_strength):
        super().__init__(cell_id, cur_division_phase)
        self.potential = potential
        self.synaptic_strength = synaptic_strength

    def fire(self):
        """ Try to evoke a spike if the synaptic strength allows for it """
        if random.random() > self.synaptic_strength:
            self.potential = 40  # mV
            print(f"PyramidalNeuron {self.cell_id} fired!")
            self.potential = -70
            return True
        else:
            print(f"PyramidalNeuron {self.cell_id} didn't fire.")
            return False


class NeuralNetwork:
    """
    Models a neural network of Neuron instances.
    Attributes: neurons - list of Neuron objects
    """
    def __init__(self, neurons):
        self.neurons = neurons
        self.is_active_firing = False

    def show_neural_network(self):
        print("Network structure:")
        for neuron in self.neurons:
            print(f"( {neuron.cell_id} )\n   \u2193")
        print("  End")

    def start_firing(self):
        """ Create an 'event loop' that triggers the spiking """
        print("Starting spiking chain:")
        self.is_active_firing = True
        for neuron in self.neurons:
            if neuron.fire():
                time.sleep(1)
                print("NeuralNetwork moving to the next cell.")
            else:
                self.is_active_firing = False
                break
        else:  # for loop completed without a break
            print("All cells in network fired successfully.")
            self.is_active_firing = False


class InhibitoryNeuron(Cell):
    """ Similar to a PyramidalNeuron """

    def __init__(self, cell_id, cur_division_phase, potential, synaptic_strength):
        super().__init__(cell_id, cur_division_phase)
        self.potential = potential
        self.synaptic_strength = synaptic_strength

    def fire(self):
        """ Try to evoke a spike if the synaptic strength allows for it """
        if random.random() > self.synaptic_strength:
            self.potential = 40  # mV
            print(f"InhibitoryNeuron {self.cell_id} fired!")

            # If one spike was triggered, there's a large chance a second will follow
            if random.random() > self.synaptic_strength / 10:
                print(f"InhibitoryNeuron {self.cell_id} fired again!")

            self.potential = -70
            return True
        else:
            print(f"PyramidalNeuron {self.cell_id} didn't fire.")
            return False


if __name__ == '__main__':
    # Check that the firing of a single neuron works:
    pyr1 = PyramidalNeuron('pyr1', 'None', -70, 0.3)
    pyr1.fire()

    # Create more and connect between them
    pyr2 = PyramidalNeuron('pyr2', 'None', -65, 0.2)
    pyr3 = PyramidalNeuron('pyr3', 'None', -75, 0.1)
    pyr4 = PyramidalNeuron('pyr4', 'None', -70, 0.4)
    network = NeuralNetwork((pyr1, pyr2, pyr3, pyr4))
    network.show_neural_network()

    # Now we're ready to fire
    network.start_firing()

    # Create a new network with a couple of inhibitory neurons.
    # It's important to note how the call to the method stays the same.
    inhib1 = InhibitoryNeuron('inhib1', 'None', -80, 0.1)
    inhib2 = InhibitoryNeuron('inhib2', 'None', -65, 0.2)
    network2 = NeuralNetwork((pyr1, inhib1, inhib2,
                              pyr4, pyr3, pyr2))
    network2.show_neural_network()
    network2.start_firing()