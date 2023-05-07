import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-regex',
    version='0.1.0',
    author='Tyler Reddy',
    author_email='tyler.je.reddy@gmail.com',
    maintainer='Tyler Reddy',
    maintainer_email='tyler.je.reddy@gmail.com',
    license='MIT',
    url='https://github.com/tylerjereddy/pytest-regex',
    description='Select tests with Python regex',
    long_description=read('README.md'),
    py_modules=['pytest_regex'],
    python_requires='>=3.9',
    install_requires=['pytest>=3.5.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'regex = pytest_regex',
        ],
    },
)
