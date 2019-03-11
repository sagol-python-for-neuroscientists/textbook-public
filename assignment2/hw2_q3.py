"""
__author__ = Hagai Har-Gil
HW2 Question 3 Solution
"""
import random
import time

class Neuron:
    """
    Abstract neuron.
    Attributes: cell_id (int), na_conc (float), number_of_axons (int)
    Methods: fire(), check_na()
    """

    def __init__(self, cell_id, potential, synaptic_strength=0.7):
        self.cell_id = int(cell_id)
        self.potential = potential
        self.synaptic_strength = float(synaptic_strength)

    def fire(self):
        """ Try to evoke a spike if the synaptic strength allows for it """
        if random.random() > self.synaptic_strength:
            self.potential = 40  # mV
            print(f"Neuron {self.cell_id} fired!")
            self.potential = -70
            return True
        print(f"Neuron {self.cell_id} didn't fire.")
        return False

    def reset_synaptic_strength(self, strength=0.7):
        """
        Changes synaptic strength back to
        baseline levels. Useful when you want to just
        forget.
        """
        self.synaptic_strength = strength


class PyramidalNeuron(Neuron):
    """
    A very coarse model of a pyramidal neuron.
    Mandatory attributes: cell_id, potential, synaptic_strength
    Added attribute: is_layer_five - True if the neuron
    is located in layer five.
    Mandatory methods: fire  # fires a spike

    The fire method is _inherited_ from the Neuron class,
    and so we don't need to redefine it.
    """

    def __init__(self, cell_id, potential, is_layer_five=True, synaptic_strength=0.7):
        super().__init__(cell_id, potential, synaptic_strength)
        self.is_layer_five = is_layer_five


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
                print(f"Neuron {neuron.cell_id} didn't fire")
                break
        else:  # for loop completed without a break
            print("All cells in network fired successfully.")
            self.is_active_firing = False

        for neuron in self.neurons:
            neuron.reset_synaptic_strength()


class InhibitoryNeuron(Neuron):
    """ Similar to a PyramidalNeuron, but has an ability to
    fire twice in a row """

    def __init__(self, cell_id, potential, main_receptor='vip', synaptic_strength=0.7):
        super().__init__(cell_id, potential, synaptic_strength)
        self.main_receptor = main_receptor

    def fire(self):
        """
        Try to evoke a spike if the synaptic strength allows for it
        This method is different from the standard fire() method
        since it has an option for a secondary spike.
        """
        if random.random() > self.synaptic_strength:
            self.potential = 40  # mV
            print(f"InhibitoryNeuron {self.cell_id} fired!")

            # If one spike was triggered, there's a large chance a second will follow
            if random.random() > self.synaptic_strength / 10:
                print(f"InhibitoryNeuron {self.cell_id} fired again!")

            self.potential = -70
            return True
        else:
            print(f"InhibitoryNeuron {self.cell_id} didn't fire.")
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