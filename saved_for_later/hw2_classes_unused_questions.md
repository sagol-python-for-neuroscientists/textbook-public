2. _The Time Class:_
    * Define the `Time` class:

    ```python
    class Time:
        """
        Represents the time of the day.
        Attributes: hour, minute, second
        """
    ```

    * Give default values to the `__init__` function.
    * Validate that the input fits a 24 hour clock. Think of as many edge-cases as you can. If the input
    isn't valid reset that value to 0.
    * Override the `__str__` method so that when you print a Time instance it prints out nicely.
    * Define a `Time().is_after(other_time)` method. that returns `True` if the first `Time()` is later
    than the `other_time` instance, and `False` otherwise. `00:00:00` is the earliest, `23:59:59` is the latest.
    * Overload the `__add__` operator to allow the addition of two `Time` instances.
        - Make sure you deal with all possible cases - "overflow" of minutes
        and seconds, and that after `23:59:59` comes `00:00:00`.


3. _Basic API Design:_
    This question will deal with the concept of a basic API - application programming interface - for a "NeuralNetwork" class. This class represents a network of different types of neurons that may fire one after the other. The user should only deal with the methods available to this class, without "caring" which exact cells compose the network. In other words, the implementation of the network should be agnostic to the type, and order, of neurons it contains.

    * Define the `PyramidalNeuron` class:

    ```python
    class PyramidalNeuron(Neuron):
        """
        A very coarse model of a neuron.
        Mandatory attributes: neuron_id, potential, synaptic_strength
        Mandatory methods: fire  # fires a spike, raising the cell's electric potential.
        """
    ```
    * `PyramidalNeuron`s should inherit at least one attribute from a `Neuron` base class which you should define.
    * The `fire` method should only raise the cell's potential if a random number you roll exceeds the `synaptic_strength` value.
    * Write a NeuralNetwork class that models the connectivity of a given list of PyramidalNeuron instances.

    ```python
    class NeuralNetwork:
    """
    Models a neural network of types of Neuron instances.
    Mandatory attributes: neurons (iterable)
    """
    ```

    * Write a `show_neural_network` method for the `NeuralNetwork` class that shows the connectivity of the cells.
    * Write a `start_firing` method that orders the first cell to fire and tracks the firing inside
    the network. If the `fire` was successful, it should make the next cell in line try to fire.
    * Write another neuron class, this time `InhibitoryNeuron(Neuron)`. It should have similar features to the `PyramidalNeuron` we already have. On top of that, make it so when it does fire, it has an increased chance to fire a second spike.
    * Don't forget that it should also be able to integrate seamlessly into the NeuralNetwork.
    * Start up the network and see that it fires correctly.
    * Again - the goal is to separate the "user interface", i.e. the call
    to `NeuralNetwork.start_firing()` method, from the actual existing neurons.
