from typing import Tuple

import matplotlib.cm as cm
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import BoundaryNorm, ListedColormap
from sklearn.neighbors import KNeighborsClassifier

# Create color maps
CMAP_LIGHT = ListedColormap(["#FFAAAA", "#AAFFAA", "#AAAAFF", "#AFAFAF"])
CMAP_BOLD = ListedColormap(["#FF0000", "#00FF00", "#0000FF", "#AFAFAF"])


def plot_knn_decision_boundary(
    X: pd.DataFrame,
    y: pd.Series,
    feature_names: Tuple[str, str] = ("height", "width"),
    n_neighbors: int = 5,
    weights: str = "uniform",
    step_size: float = 0.01,
    scatter_size: int = 50,
):
    feature_values = X[list(feature_names)].values
    target_values = y.values
    clf = KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(feature_values, target_values)

    # Generate a grid of coordinates in the provided data range
    x_range = (
        feature_values[:, 0].min() - 1,
        feature_values[:, 0].max() + 1,
    )
    y_range = (
        feature_values[:, 1].min() - 1,
        feature_values[:, 1].max() + 1,
    )
    xx, yy = np.meshgrid(
        np.arange(*x_range, step_size),
        np.arange(*y_range, step_size),
    )
    # Plot the decision boundary by assigning a color in the color map
    # to each mesh point.
    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    z = z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, z, cmap=CMAP_LIGHT, shading="auto")
    # Plot training points
    plt.scatter(
        feature_values[:, 0],
        feature_values[:, 1],
        s=scatter_size,
        c=y,
        cmap=CMAP_BOLD,
        edgecolor="black",
    )
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    patch0 = mpatches.Patch(color="#FF0000", label="apple")
    patch1 = mpatches.Patch(color="#00FF00", label="mandarin")
    patch2 = mpatches.Patch(color="#0000FF", label="orange")
    patch3 = mpatches.Patch(color="#AFAFAF", label="lemon")
    plt.legend(handles=[patch0, patch1, patch2, patch3])
