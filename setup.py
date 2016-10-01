from setuptools import setup, find_packages

setup(
    name='ding',
    description='Quick organisation via the commandline',
    url='https://github.com/liviu-/ding',
    license='MIT',
    packages=find_packages(),
    entry_points = {
        "console_scripts": ['ding = ding.ding:main']
        },
    )
