# PYPOTREE (potree for jupyter notebooks)

Allows to insert potree cells into jupyter and colab notebooks

[Gabriele Facciolo](mailto:gfacciol@gmail.com), Gabriele Facciolo, CMLA 2019

# Installation and dependencies

The main source code repository for this project is https://github.com/cmla/pypotree
It is written in Python and contains Potree and PotreeConverter. It was tested with Python 3.5 and 3.6.

`pypotree` requires C and C++ developement tools.

`pypotree` can be installed with `pip`:

    pip install pypotree

# Usage

In a Python interpreter:

    >>> import pypotree 
    >>> import numpy as np
    >>> xyz = np.random.random((100000,3))
    >>> cloudpath = pypotree.generate_cloud_for_display(xyz)
    >>> pypotree.display_cloud_colab(cloudpath)

