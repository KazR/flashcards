from setuptools import setup

setup(
    name='flashcard',
    version='0.1',
    description='A flashcard application',
    author='KazR, kiiroisenko786',
    packages=['flashcard'],
    install_requires=[
        'pandas',
        'tk',
    ],
    entry_points={
        'console_scripts': [
            'flashcard=flashcard.__main__:main'
        ]
    }
)
