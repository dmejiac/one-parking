from setuptools import setup

setup(name='modules', version='1.0.0', packages=['modules'],
      entry_points={
          'console_scripts': ['modules = src.modules.__main__:main']
      })
