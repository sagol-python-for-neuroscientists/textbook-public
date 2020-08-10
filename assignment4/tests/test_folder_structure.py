import pathlib

import pytest


@pytest.fixture
def subfolders_list():
    return [x.name for x in pathlib.Path(__file__).parents[1].iterdir() if x.is_dir()]


@pytest.fixture
def python_files():
    return [file.name for file in pathlib.Path("src").glob("**/*.py")]


def test_src_in_folder(subfolders_list):
    assert "src" in subfolders_list


def test_tests_in_folder(subfolders_list):
    assert "tests" in subfolders_list


def test_results_in_folder(subfolders_list):
    assert "results" in subfolders_list


def test_data_in_folder(subfolders_list):
    assert "data" in subfolders_list


def test_hw4_folder_in_src():
    assert pathlib.Path("src/hw4") in list((pathlib.Path(".") / "src").iterdir())


def test_qx_folder_in_hw4():
    folder = [x.name for x in pathlib.Path("src/hw4").iterdir() if x.is_dir()]
    assert "q1" in folder
    assert "q2" in folder
    assert "q3" in folder


def test_four_init_in_folders(python_files):
    assert python_files.count("__init__.py") == 4


def test_two_data_loadings(python_files):
    assert python_files.count("data_loading.py") == 2


def test_hw_files_in_correct_dirs():
    """Constructs a dict with the Python filenames as keys and the
    name of the parent directory as values, and makes sure that
    the files are in the correct folders."""
    python_files_with_parents = {
        file.name: str(file.relative_to("src/hw4").parent)
        for file in pathlib.Path("src").glob("**/*.py")
    }
    print(python_files_with_parents)
    for name, parent in python_files_with_parents.items():
        if "hw4" not in name:
            continue
        if "q1" in name:
            assert parent == "q1"
            continue
        if "q2" in name:
            assert parent == "q2"
            continue
        if "q3" in name:
            assert parent == "q3"
            continue


def test_data_loading_contains_load_data_function():
    try:
        from hw4.q2.data_loading import load_data
        from hw4.q3.data_loading import load_data
    except ImportError:
        assert (
            False
        ), "ImportError, missing load_data function or package isn't installed with 'pip install -e .'"
    else:
        assert True


def test_results_folder_contains_mandelbrot_png():
    assert pathlib.Path("results/mandelbrot.png").exists()
