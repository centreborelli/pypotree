import os
import subprocess
from codecs import open
from setuptools import setup
from setuptools.command import develop, build_py


def readme():
    with open('README.md', 'r', 'utf-8') as f:
        return f.read()


class CustomDevelop(develop.develop, object):
    """
    Class needed for "pip install -e ."
    """
    def run(self):
        subprocess.check_call("make", shell=True)
        super(CustomDevelop, self).run()


class CustomBuildPy(build_py.build_py, object):
    """
    Class needed for "pip install srtm4"
    """
    def run(self):
        super(CustomBuildPy, self).run()
        subprocess.check_call("make", shell=True)
        subprocess.check_call("cp -r bin build/lib/", shell=True)


requirements = [ 'numpy',
                ]


setup(name="pypotree",
      version="1.0.0",
      description='Potree visualization for jypyter notebooks',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/cmla/pypotree',
      author='Gabriele Facciolo',
      author_email='gfacciol@gmail.com',
      py_modules=['pypotree'],
      install_requires=requirements,
      cmdclass={'develop': CustomDevelop,
                'build_py': CustomBuildPy},
      include_package_data=True,
      python_requires='>=2.7',
      zip_safe=False)
