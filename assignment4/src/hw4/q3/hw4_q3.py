import pathlib

from .data_loading import load_data


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
    data = load_data(fname)
    complaint_counts = data["Complaint Type"].value_counts()
    return complaint_counts.index[0], complaint_counts[0]


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
    data = load_data(fname)
    illegal_parks = data.loc[data.loc[:, "Complaint Type"] == "Illegal Parking", :]
    return illegal_parks.Borough.value_counts().index[0]


if __name__ == "__main__":
    fname = pathlib.Path("311_service_requests.zip")
    d = common_complaint(fname)
    c = parking_borough(fname)
