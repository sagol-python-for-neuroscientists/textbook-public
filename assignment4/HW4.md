# Homework Assignment #4

## Date: 22-04-2018
## Due date: 06-05-2018, 15:00

3. _Mandelbrot Set (20 point bonus):_

    Assuming `n` iterations, a number is a part of the Mandelbrot set `if |z| < thresh`,
    where `z(n+1) = z(n) ** 2 + c` and `c = x + jy` ("2D" complex number).
    Write a function that computes a 2D binary mask of the numbers that belong to the set, in the
    grid [-2, 1], [-1.5, 1.5], after `n` iterations.
    You may show the resulting 2D image using `matplotlib` - an example is attached.

    ```python
    def mandel(n: int, thresh: float=50.,
               xlims: np.ndarray=np.array([-2, 1]), nx: int=600,
               ylims: np.ndarray=np.array([-1.5, 1.5]), ny: int=600):
        """
        Creates a grid of numbers between xlims and ylims and computes the mandlebrot
        fractal. Shows an image of the points in the grid that belong to that set.
        """
    ```

3. _Basic Data Manipulation:_

    The repo contains `populations.txt`, a small data file containing a table with observations
    of the number of individual animals each year.

    i. Which species has the largest population in each year? Write the following function:

    ```python
    def largest_species(fname: str) -> pd.Series:
    """ Return largest column by year from the text file """
    ```

    The function should return a pandas Series object, each row containing the name
    of the animal with the highest population for that year.

    ii. Return a `Series` with the number of lynxes, only in the years in which
    the population of hares outgrew that of the foxes.

    ```python
    def lynxes_when_hares(fname: str) -> pd.Series:
        """ Returns the number of lynxes when hares > fox """
    ```

    iii. Add a column to the `DataFrame` called `mean_animals` with the normalized mean number
    of all animals in each year. Meaning that the year with the most lynxes, hares and foxes
    combined should have a `mean_animals` value of 1, and the rest should have a value between 0 and 1.

    ```python
    def mean_animals(fname: str) -> pd.DataFrame:
        """ Add a fourth column with the normalized mean number of animals in each year """
    ```

4. _More Data Munching:_

    Download the NYC 311 service requests data from [here](https://osf.io/3a6qs), unzip it into a
    standard CSV file, and load it into pandas (you can do it all, together, with pandas).

    i. What is the most common complaint type? Write a function that returns a tuple
    with the complaint tag and number of occasions it was reported.

    ```python
    def common_complaint(fname: str):
        """
        Finds and returns the most common complaint as a tuple:
        (complaint_name, num)
        """
    ```

    ii. Which borough has the most complaints of type `Illegal Parking`?
    Return its name.

    ```python
    def parking_borough(fname: str) -> str:
    """
    Finds and returns the name of the NYC borough that has the
    most complaints of type 'Illegal Parking'.
    """
    ```

    You don't need to push the `.zip` (or `.csv`) file into your repository for the submission.