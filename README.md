The code for our paper Kernel-based attention network for point cloud compression
## setup
The environment can be setup with docker or anaconda.
In the 103server, our anaconda environment "KPA" can be reference for establishing the environment. You can download the anaconda package for runing the code.
## dataset
Our compression datasets can be found in the 103 server which located at /Datasets/submaps 
## train 
python3 trainer.py -cfg <path-to-your-config>
## test 
python3 test.py -cfg <path-to-your-config>
## visulize 
python3 visuliaze .py
