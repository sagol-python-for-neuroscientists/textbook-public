import xarray as xr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class VisualStimData:
    """
    Data and methods for the visual stimulus ePhys experiment.
    The data table itself is held in self.data, an `xarray` object.
    Inputs:
        data: xr.DataArray or xr.Dataset
    Methods:
         ...
    """
    def __init__(self, data: xr.Dataset, ):
        assert isinstance(data, xr.Dataset)
        self.data = data


    def plot_electrode(self, rep_number: int, rat_id: int, elec_number: tuple=(0,)):
        """
        Plots the voltage of the electrodes in "elec_number" for the rat "rat_id" in the repetition
        "rep_number". Shows a single figure with two subplots, for male and female rats.
        """
        fig, axes = plt.subplots(len(elec_number), 1)
        axes = np.array([axes]) if isinstance(axes, plt.Axes) else axes
        time = self.data['time']
        for ax, elec in zip(axes, elec_number):
            to_plot = self.data.sel(rep=rep_number, rat_id=rat_id, elec=elec)['volt'].values
            ax.plot(time, to_plot)
            ax.set_xlabel('Time [s]')
            ax.set_ylabel('Voltage [V]')
            ax.set_title(f'Electrode {elec}')

        fig.tight_layout()

    def experimenter_bias(self):
        """ Shows the statistics of the average recording across all experimenters """
        names = np.unique(self.data.coords['exp_name'].values)
        means = []
        stds = []
        medians = []
        for experimenter in names:
            data = self.data.sel(exp_name=experimenter)['volt'].values
            means.append(np.abs(data.mean()))
            stds.append(np.abs(data.std()))
            medians.append(np.abs(np.median(data)))

        # Plotting
        fig, ax = plt.subplots()
        x_locs = np.arange(len(names))
        width = 0.3
        rect0 = ax.bar(x_locs, means, width, color='C0')
        rect1 = ax.bar(x_locs + width, stds, width, color='C1')
        rect2 = ax.bar(x_locs - width, medians, width, color='C2')

        ax.set_xticks(x_locs)
        ax.set_xticklabels(names)
        ax.legend((rect0[0], rect1[0], rect2[0]), ('Mean', 'STD', 'Median'))
        ax.set_title('Experimenter Bias (absolute values)')
        ax.set_ylabel('Volts [V]')


def mock_stim_data() -> VisualStimData:
    """ Creates a new VisualStimData instance with mock data """
    num_of_animals = 20
    num_of_reps = 4
    total_num_of_exp = num_of_animals * num_of_reps
    exp_number = np.arange(total_num_of_exp, dtype=np.uint32)

    # Unique rat IDs
    rat_id_ints = np.random.choice(np.arange(100, 900), size=300, replace=False)
    rat_id = np.random.choice(rat_id_ints, size=num_of_animals, replace=False)

    # Room temperature and humidity values
    room_temp = np.random.random(total_num_of_exp) * 3 + 23  # between 23 and 26 C
    room_humid = np.random.randint(30, 70, size=total_num_of_exp)

    # Experimenter names
    names = ['Dana', 'Motti', 'Sam', 'Daria']
    experimenters = np.random.choice(names, size=num_of_animals, replace=True)
    experimenters = np.tile(experimenters, num_of_reps)

    # Rat gender
    sex = ['F', 'M']
    rat_sex = np.random.choice(sex, size=num_of_animals, replace=True)
    rat_sex = np.tile(rat_sex, num_of_reps)

    # Voltage and stimulus vector
    pre_stim = 1  # seconds
    stim_time = 0.1  # seconds
    post_stim = 0.9  # seconds
    sampling_rate = 5000  # Hz
    freq = 1 / sampling_rate
    experiment_length = int(pre_stim + stim_time + post_stim)
    electrodes = 10
    samples = sampling_rate * experiment_length

    # Random voltage values from N(0.068, 0.0004)
    volt = 0.02 * np.random.randn(electrodes, samples, num_of_animals,
                                 num_of_reps).astype(np.float32) - 0.068  # in volts, not millivolts
    volt[volt > -0.02] = 0.04  # "spikes"
    time = pd.date_range(start=pd.to_datetime('today'), periods=experiment_length * sampling_rate,
                         freq=f'{freq}S')
    electrode_array = np.arange(electrodes, dtype=np.uint16)

    # Stim index - -1 is pre, 0 is stim, 1 is post
    stim = np.zeros(int(samples), dtype=np.int8)
    stim[:int(pre_stim*sampling_rate)] = -1
    stim[int((pre_stim + stim_time)*sampling_rate):] += 1

    # Repetition
    reps = np.arange(num_of_reps, dtype=np.uint8)

    # Construct the Dataset - this could be done with a pd.MultiIndex as well
    ds = xr.Dataset({'temp': (['num'], room_temp),
                     'humid': (['num'], room_humid),
                     'volt': (['elec', 'time', 'rat_id', 'rep'], volt),
                     'stim': (['time'], stim)},
                    coords={'elec': electrode_array,
                            'time': time,
                            'rat_id': rat_id,
                            'rep': reps,
                            'exp_name': experimenters,
                            'sex': rat_sex,
                            'num': exp_number,
                            })

    ds.attrs['exp_date'] = pd.to_datetime('today')
    ds.attrs['rat_strain'] = 'Sprague Dawley'

    return VisualStimData(ds)


if __name__ == '__main__':
    stim_data = mock_stim_data()
    ids = stim_data.data['rat_id']
    arr = stim_data.plot_electrode(rep_number=2, rat_id=ids[0], elec_number=(1, 6))
    stim_data.experimenter_bias()
