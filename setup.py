from setuptools import setup, find_packages

setup(
    name="openGL",
    extras_require=dict(tests=['pytest'], interface=['glumpy'], game_interface=['pygame']),
    packages=find_packages(where='src'),
    packages_dir={"": "src"},
)