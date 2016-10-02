from setuptools import setup, find_packages

def get_version():
    with open('ding/ding.py') as f:
        version = next(line for line in f.read().splitlines() if 'VERSION' in line)
        version = version.split(' = ')[-1].strip("'")
    return version

setup(
    name='ding-ding',
    description='Quick organisation via the commandline',
    url='https://github.com/liviu-/ding',
    version=get_version(),
    license='MIT',
    packages=find_packages(),
    entry_points = {
        "console_scripts": ['ding = ding.ding:main']
        },
    )
