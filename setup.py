from setuptools import setup, find_packages

setup(
    name='simplot',
    version='0.0.1',
    description='Draw graph simply use matplotlib.',
    author='Ryota Nishi',
    author_email='ryota0312@s.okayama-u.ac.jp',
    install_requires=['matplotlib'],
    url='https://github.com/Ryota0312/simplot',
    license=license,
    packages = find_packages(),
    test_suite = 'test'
)
