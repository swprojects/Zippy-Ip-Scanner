"""A setuptools based setup module for Zippy-Ip-Scanner"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages
import setuptools.command.build_py

from zippyipscanner.version import __version__

def on_windows():
    """Returns True if OS is Windows."""
    return os.name == "nt"

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

test_requirements = [
    # TODO: put package test requirements here
]

package_data = {
    'sample': ['package_data.dat'],
}

class InstallDependencies(setuptools.command.build_py.build_py):

  def run(self):
    system("chmod u+x install_dependencies.sh")
    system("./install_dependencies.sh")

setup(
    name='zippy-ip-scanner',
    version=__version__,
    description="IP Scanner",
    long_description=readme + '\n\n' + history,

    # Author details
    author="Simon Wu",
    author_email='swprojects@runbox.com',

    # The project's main homepage.
    url='https://github.com/swprojects/zippy-ip-scanner',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['docs', 'resources', 'snap', 'tests*']),

    package_data = {
        '': ["images/*.png", "splash.png", "zippyipscanner.ico"],
    },

    data_files = [
        ('share/applications', ['data/ZippyIpScanner.desktop']),
        ('share/zippyipscanner', ['zippyipscanner/zippyipscanner.ico']),
    ],

    # https://packaging.python.org/en/latest/requirements.html
    install_requires =  [
        "wxPython",
        "requests",
    ],

    license="GPLv2",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # 'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Internet',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    test_suite='tests',
    tests_require=test_requirements,
    cmdclass={'install_deps': InstallDependencies},
    entry_points={
          'gui_scripts': [
              'zippyscan = zippyipscanner.zippyipscanner:main'
          ]
      },
)
