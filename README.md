The code for our paper Kernel-based attention network for point cloud compression
## setup
The environment can be setup with docker or anaconda.
In the 103server, our anaconda environment "KPA" can be reference for establishing the environment. You can download the anaconda package for runing the code.
## dataset
Our compression datasets can be found in the 103 server which located at /Datasets/submaps 
## train 
For training a network we first have to create the config file with all the parameters. An example of this can be found in /depoco/config/depoco.yaml. Make sure to give each config file a unique experiment_id: ... to not override previous models. To train the network simply run
python3 trainer.py -cfg <path-to-your-config>
## test 
Evaluating the network on the test set can be done by:
python3 test.py -cfg <path-to-your-config>

All results will be saved in a dictonary.
## visulize 
We can plot the quantitative results e.g. by using Jupyter-Lab. An example of this is provided in depoco/notebooks/visualize.ipynb. Jupyter-Lab can be started in the Docker container by:
python3 visuliaze .py
