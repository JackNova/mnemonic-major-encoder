======================
Mnemonic Major Encoder
======================


.. image:: https://img.shields.io/pypi/v/mnemonic-major-encoder.svg
        :target: https://pypi.python.org/pypi/mnemonic-major-encoder

.. image:: https://img.shields.io/travis/JackNova/mnemonic-major-encoder.svg
        :target: https://travis-ci.org/JackNova/mnemonic-major-encoder

.. image:: https://readthedocs.org/projects/mnemonic-major-encoder/badge/?version=latest
        :target: https://mnemonic-major-encoder.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Encode and Decode text by the Major System


* Free software: MIT license
* Documentation: https://mnemonic-major-encoder.readthedocs.io.


Features
--------

* encode text by the mnemonic major system
* decode a number into a word according to the mnemonic major system

Usage
-----

>>> from mnemonic_major_encoder import encoder
>>> encoder.encode("dario")
'14'

>>> from mnemonic_major_encoder import decoder
>>> decoder.decode("23095")
['inammissibile', 'inammissibili', 'inammissible']


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
