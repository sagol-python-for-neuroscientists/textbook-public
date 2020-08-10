# Homework Assignment #4

## Date: 20-04-2020
## Due date: 04-05-2020, 15:00

**Do not change the signature (definition) of the functions in the exercise.**

**Tests are run with `pytest`. It's time to learn how to use it :)**

**Read below to see how to structure your files for this project. You should start working on the HW from there.**

1. _Mandelbrot Set:_

    A number is a part of the [Mandelbrot set](https://www.youtube.com/watch?v=FFftmWSzgmk) if `|z| < thresh`,
    where `z(n+1) = z(n) ** 2 + c`, `c = x + jy` is an arbitrary "2D" complex number and `n` is the index of iteration.
    Write a function that computes a 2D binary mask of the numbers that belong to the set, in the
    grid [-2, 1], [-1.5, 1.5], after `n` iterations.
    The correctness is checked qualitatively with the resulting 2D image, easily generated with `matplotlib` - an example is attached.
    Use the `extent` keyword for the `imshow` function to show image with the right boundaries. Save the resulting image
    in the `results` folder under the name `mandelbrot.png`.

    ```python
    def mandel(
        n: int,
        thresh: float = 50.0,
        xlims: np.ndarray = np.array([-2, 1]),
        nx: int = 1500,
        ylims: np.ndarray = np.array([-1.5, 1.5]),
        ny: int = 1500,
    ) -> np.ndarray:
        """Computes the Mandelbrot fractal on some given set of numbers.

        Parameters
        ----------
        n : int
            Number of iterations.
        thresh : float
            Threshold which decides if a number is a part of the set.
        xlims, ylims : np.ndarray
            Limits for the computation of the fractal.
        nx, ny : int
            Number of points between xlims.min() and xlims.max() to calculate the set on.

        Returns
        -------
        img : np.ndarray
            A binary image with a value of 1 if the point belongs to the set.
            The shape of the resulting image is (nx, ny).
        Also saves "mandelbrot.png" to the "results" folder.
        """
    ```

In the following two questions you should use `pandas` to solve the given
problems. Using it correctly, the resulting solution shouldn't be longer
than 3-4 lines. However, points will not be deducted for longer, convoluted,
solutions.

2. _Basic Data Manipulation:_

    The repo contains `data/populations.txt`, a small data file containing a table with observations
    of the number of individual animals each year. Create `hw4/q2/data_loading.py` which contains
    (at least) one function called `load_data` which receives the filename and returns a dataframe.
    All functions which are defined below should use this `load_data` function to load their data by
    `import`ing it from `data_loading`.

    i. Which species has the largest population in each year? Write the following function:

    ```python
    def largest_species(fname: pathlib.Path) -> pd.Series:
    """Returns the name of the most widespread species per year.

    Parameters
    ----------
    fname : pathlib.Path
        Filename for the columnar data containing the population numbers.

    Returns
    -------
    largest_by_year : pd.Series
        Name of most common species per year
    """
    ```

    The function should return a pandas Series object, each row containing the name
    of the animal with the highest population for that year.

    ii. Return a `Series` with the number of lynxes, only in the years in which
    the population of hares outgrew that of the foxes.

    ```python
    def lynxes_when_hares(fname: pathlib.Path) -> pd.Series:
        """Returns the number of lynxes when hares > foxes.

        Parameters
        ----------
        fname : pathlib.Path
            Filename for the columnar data containing the population numbers.

        Returns
        -------
        lynxes : pd.Series
            Number of lynxes when hares > foxes
        """
    ```

    iii. Add a column to the `DataFrame` called `mean_animals` with the normalized mean number
    of all animals in each year. Meaning that the year with the most lynxes, hares and foxes
    combined should have a `mean_animals` value of 1, and the rest should have a value between 0 and 1.

    ```python
    def mean_animals(fname: pathlib.Path) -> pd.DataFrame:
        """Adds a column with the normalized mean number of animals in each year.

        This means that in the year with most animals, this column will have the value of 1,
        and in the rest of the years the value will be between [0, 1).

        Parameters
        ----------
        fname : pathlib.Path
            Filename for the columnar data containing the population numbers.

        Returns
        -------
        data : pd.DataFrame
            Original dataset with the new "mean_animals" column.
        """
    ```

3. _More Data Munching:_

    Download the NYC 311 service requests data from [here](https://osf.io/3a6qs) to the `data` folder, and read it with pandas by creating `hw4/q3/data_loading.py` which should contain
    (at least) one function called `load_data` which receives the filename and returns a dataframe.
    All functions which are defined below should use this `load_data` function to load their data by
    `import`ing it from `data_loading`.


    i. What is the most common complaint? Write a function that returns a tuple
    with the complaint name and number of occasions it was reported.

    ```python
    def common_complaint(fname: pathlib.Path):
        """Finds and returns the most common complaint as (complaint_name, num).

        Parameters
        ----------
        fname : pathlib.Path
            Filename for the NYC data.

        Returns
        -------
        common_complaint : tuple
            (Complaint name, number of occasions)
        """
    ```

    ii. Which borough has the most complaints of type `Illegal Parking`?
    Return its name.

    ```python
    def parking_borough(fname: pathlib.Path) -> str:
        """Finds and returns the name of the NYC borough that has the
        most complaints of type 'Illegal Parking'.

        Parameters
        ----------
        fname : pathlib.Path
            Filename for the NYC data.

        Returns
        -------
        borough_name : str
            Name of the relevant NYC borough.
        """
    ```

    Please don't push the `.zip` (or `.csv`) file into your repository for the submission.


## More Submission Instructions

One of the goals of this HW is to show an example of how a real Python project is constructed. "Real" in this sense means that we're not writing a few "loosely connected" files for some insignificant homework assignment. Instead we're emulating the way in which a major Python application will be built in terms of the folder structure and the usability aspect. Accordingly some of the tests in the repo don't test the actual performance of your code, but instead test whether it was structured correctly.

The folder structure for this project, which we'll call `hw4`, should be as follows:

```
SagolPythonHW4
|   README.md
|   setup.py
|   LICENSE
|   .gitignore
└--- src
|    └--- hw4
|    |    |    __init__.py
|    |    └--- q1
|    |    |    |   __init__.py
|    |    |    |   hw4_q1.py
|    |    └--- q2
|    |    |    |    __init__.py
|    |    |    |    data_loading.py
|    |    |    |    hw4_q2.py
|    |    └--- q3
|    |    |    |    __init__.py
|    |    |    |    data_loading.py
|    |    |    |    hw4_q3.py
└--- tests
|    └--- tests_data
|    |    |    q3_largest.csv
|    |    |    q3_lynx.csv
|    |    |    q3_mean.csv
|    |    test_folder_structure.py
|    |    test_q2.py
|    |    test_q3.py
└--- data
|    |    311_service_requests.zip
|    |    populations.txt
└--- results
|    |    mandelbrot.png
```

### Notes:

1. The name of the top folder, `SagolPythonHW4` is not important. You may call it however you'd like.
2. When we `import` this project, the name is determined by what will be written inside `setup.py` and by the name of the folder under `src`, which is `hw4` in this case. This is the __project's name__ - `numpy` for Numpy, `pandas` for Pandas, etc.
3. Each folder which contains Python code inside it, or in one of its subfolders, should include a `__init__.py` file. We have four of these in this project.
4. The filenames themselves (e.g. `hw4_q2.py`) don't have to have the project's name (`hw4`) in their filename in general. It's done here for clarity.
5. Again, this is a bit of an overkill for a simple home assignment. The goal here is to show you how to build your real-life, research-focused project.

Once you have this tree set up, you should start filling in the files with actual content:

1. Follow the steps in the file `create_and_publish_package.ipynb` which can be found in the course's website. The project there is named `parse_stuff` and here we called it `hw4`, so make sure to swap these two names. Besides that, it should help you populate `setup.py`, `LICENSE`, `.gitignore` and `src/hw4/__init__.py`.
2. Follow the steps up to and including `pip install -e .`.
3. Check that you can indeed import your new package. Start a Python instance (`python`) and try to `import hw4`. It should Just Work™.

Now you're ready to work on the code itself. A few additional points:

1. Question 1 should output the `mandelbrot.png` file to the `results` folder.
2. Questions 2 & 3 require you to read some data. This function should live inside `data_loading.py`, in the respective `q2`/`q3` folder, and the code in `q2/hw4_q2.py` or `q3/hw4_q3.py` should import it.
3. The tests will only run if the installation step was successful, since they treat this package as an "external" package (look for the `from hw4.q2.hw4_q2 import *` line, for example). It means that they import it much like they would any other package. It also means that you won't be able to test anything before you actually finish installing the project correctly.


