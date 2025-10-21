# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 22:34:57 2021

@author: penglu
"""

from __future__ import absolute_import
from setuptools import setup, find_packages

setup(name='IMC_Denoise',
      packages=find_packages(),
      install_requires=[
          "numpy==1.21.0",
          "scipy=1.4.1",
          "matplotlib=3.3.4",
          "scikit-learn==0.24.2",
          "tensorflow==2.6.0",
          "keras==2.6.0",
          "tifffile==2023.7.10",
          "protobuf==3.20.3"
        ]
      )
