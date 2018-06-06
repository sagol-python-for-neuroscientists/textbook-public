# Homework Assignment #5

### Date: 06-05-2018
### Due date: 20-05-2018

## Rat Visual Stimulus Experiment Database

You're measuring the potential of neurons in a rat's brain over time in response to flashes of light
using a multi-electrode array surgically inserted into the rat's skull. Each trial is two seconds
long, and one second into the trial a short, 100 ms, bright light is flashed at the animal. After 30 seconds
the experiment is replicated, for a total of 4 repetitions. The relevant parameters are the following:

- Rat ID.
- Room temp.
- Room humidity.
- Experimenter name.
- Rat gender.
- Measured voltage (10 electrode, 10k samples representing two seconds).
- Stimulus index (mark differently the pre-, during- and post-stimulus time).
- Repetition number.

Mock data and model it, you can add more parameters if you feel so. You'll use this model for your homework as well,
where we will expand and work with it further, so try to build good foundations.

Experimental timeline:
```bob
       1s          100ms             0.9s             30s
Start -----> Flash -----> End flash -----> End trial -----> New trial
|                                                                    |
|--------------------------------------------------------------------|
                                   x4
```

### Methods and functions to implement:

1. There should be a class holding this data table, `VisualStimData`, alongside
several methods for the analysis of the data. The class should have a `data`
attribute containing the data table, in a `xarray.DataArray` or a `xarray.Dataset`.

2. Write a function (not a method) that returns an instance of the class with mock data.
    ```python
    def mock_stim_data() -> VisualStimData:
        """ Creates a new VisualStimData instance with mock data """
    ```

    When simulating the recorded voltage, it's completely fine to not model spikes precisely,
    with leaky integration and so forth - randoming numbers and treating them as the recorded
    neural potential is fine. There are quite a few ways to model _real_ neurons,
    if so you wish, [brian](http://brian2.readthedocs.io/en/stable/index.html) being one
    of them. If your own research will benefit from knowing how to use these tools, this
    exercise is a great place to start familiarizing yourself with them.

3. Write a method that receives a repetition number, rat ID, and a list of electrode numbers,
and plots the voltage recorded from these electrodes. The single figure should be
divided into however many plots needed, depending on the length of the list of electrode
numbers.

    ```python
    def plot_electrode(self, rep_number: int, rat_id: int, elec_number: tuple=(0,)):
        """
        Plots the voltage of the electrodes in "elec_number" for the rat "rat_id" in the repetition
        "rep_number". Shows a single figure with subplots.
        """
    ```

4. To see if the different experimenters influence the measurements, write a method that
calculates the mean, standard deviation and median of the average voltage trace across all
repetitions, for each experimenter, and shows a bar plot of it.

    ```python
    def experimenter_bias(self):
        """ Shows the statistics of the average recording across all experimenters """
    ```


## Submission

A couple of things differ in this submission from the previous ones.

1. No a are supplied, since I wanted this assignment's implementation to be completely up
to your own judgement. The code will be checked for correctness using internal a I wrote
and following a review of the code. _A detailed docstring for all functions and class methods is mandatory._

2. The submission will be done via a _pull request_ to my repository. A pull request is a common
action when using Git and GitHub. This operation pings the owner of the repository, presenting
changes that you think should be done to the code inside that repository. Contributions to most open-source
projects, from tiny command-line utilities to the Linux operating systems, are done using pull requests.

To start off, _fork_ the `hw5` repository by clicking the button on the top right-hand side. This will
create a "snapshot" of the main repository, by copying its current state into a new repository under your
control. You should clone this new repo into your computer, and work as usual - add files, commit and push as
you normally would. When you're done you should create the pull request by following the instructions
written [here](https://help.github.com/articles/creating-a-pull-request-from-a-fork/). You can update
the pull request after it was created by simply pushing new updates to your own original fork, so
starting a pull request doesn't forbid you from updating your code.

The submission will be the latest pull request submitted by you, obviously no later than the due date.