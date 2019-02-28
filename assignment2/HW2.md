# Homework Assignment #2

## Date: 18-03-2018
## Due date: 5-4-2018

### Link to GitHub repo:

1. _The Bicycle Class:_
    * Write a definition for a class named ``Bicycle``:
        * It must contain the following attributes: `cadence`, `speed`, `gear`.
        * It must contain a `__str__` method which prints its state (like the ShoppingList in class).
        * The bicycle should be able speed up, brake, change gear and cadence. However, the `speed`
        attribute should be calculated from the two other attributes, since it depends directly
        on the pedal cadence and gear.
        * Write a `change_speed_to` method that increases\decreases the speed by changing the cadence and gear as necessary.
            - Note: You might want to add more methods to the class that will help you to implement this behavior.
            - The maximal speed of our bicycle should be 1000 KPH.
        * Make sure the bicycle can't reach a speed below 0 when breaking, or slow the pedal cadence below 0 rotations.
        * Our bicycle only has 7 gears, enforce this limit on the method that controls the change of gears.


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
    This question will deal with the concept of a basic API - application programming interface -
    for a "NeuralNetwork" class. This class represents a network of different types of neurons
    that may fire one after the other. The user should only deal with the methods available
    to this class, without "caring" which exact cells compose the network. In other words, the implementation
    of the network should be agnostic to the type, and order, of neurons it contains.

    * Define the Neuron class:
    ```python
    class PyramidalNeuron(Cell):
        """
        A very coarse model of a neuron.
        Mandatory attributes: cell_id, potential, synaptic_strength
        Mandatory methods: fire  # fires a spike, raising the cell's electric potential.
        """
    ```
    * Neurons should inherit at least one attribute from a `Cell` base class which you should define.
    * The `fire` method should only raise the cell's potential if a random number you roll exceeds
    the `synaptic_strength` value.
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
    * Write another neuron class, this time `InhibitoryNeuron(Cell)`. It should have similar
    features to the `PyramidalNeuron` we already have. On top of that, make it so when it does fire,
    it has an increased chance to fire a second spike.
    * Don't forget that it should also be able to integrate seamlessly into the NeuralNetwork.
    * Start up the network and see that it fires correctly.
    * Again - the goal is to separate the "user interface", i.e. the call
    to `NeuralNetwork.start_firing()` method, from the actual existing neurons.

## Submission:
This assignment and all others to follow will be submitted via GitHub Classroom, a special interface of GitHub.
The link above will create a new repository with your name and the due date listed above. Clone the repository to your computer and solve the exercise.
Don't forget to commit your code once in a while, normally before and after major changes. You can also push your codebase
to the online repo.

In the repo you cloned, you will also find test classes for the two first questions. These classes contain
unit tests, and will determine your grade for these questions. Unit tests are a very common procedure
when writing error prone code, and should be a part of any script you write. The two unit test classes
I added serve as a good example of how to write these.

When you're done, push the code to the repo and verify that it indeed contains your latest updates. Right at the deadline I will
read the contents of your repository, downloading the latest version of the code that's in there. This will be the version I'll
check and grade. Commits that occur after the deadline will not count.

Good luck, and don't hesitate to contact me if Google doesn't solve your technical issues :)