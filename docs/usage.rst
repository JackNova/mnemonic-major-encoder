=====
Usage
=====

To use Mnemonic Major Encoder in a project::

    import mnemonic_major_encoder


>>> from mnemonic_major_encoder import encoder
>>> encoder.encode("dario")
'14'

>>> from mnemonic_major_encoder import decoder
>>> decoder.decode("23095")
['inammissibile', 'inammissibili', 'inammissible']
