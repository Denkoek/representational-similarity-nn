# representational-similarity-nn
This repository will soon be updated with the code to reproduce the results from "Finding Structure in Neural Network Activation Patterns via Representational Similarity and Convolutional Kernels".

The main code used for this thesis is Computing Final-Cleaned.ipynb. This file was cleaned but might still contain a little noise. If you have any questions, please let me know. 

# Dependencies
This code is written in python. To use it you will need:
- A recent version of NumPy and SciPy
- [Spacy](https://spacy.io/)
- [Skip-thoughts model](https://github.com/ryankiros/skip-thoughts)
- [Dependency kernel](https://github.com/fkunneman/DiscoSumo/blob/master/naacl/models/depkernel.py)
- [Smatch](https://github.com/snowblink14/smatch)
- [The data](https://amr.isi.edu/download/amr-bank-struct-v1.6-training.txt)

# Instructions
I've calculated almost everything in the main code. If you've installed everything above and run my code, you should be able to get the same results. The AMR evaluations using smatch took quite some time to run, so I used python scripts for that and calculated them outside the Jupyter Notebook. I've saved the computed AMRs and later in the main code loaded them back. I've included the python files for computing AMRs in the folder AMRs. 
