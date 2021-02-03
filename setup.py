from setuptools import setup

setup(name='src', version='1.0.0', packages=['src'],
      entry_points={
          'console_scripts': ['src = src.__main__:main']
      })
