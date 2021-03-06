from setuptools import setup, find_packages
#import neo_pynq
from distutils.dir_util import copy_tree
import os
import shutil

# global variables
board = os.environ['BOARD']
repo_board_folder = f'boards/{board}/lepton'
board_notebooks_dir = os.environ['PYNQ_JUPYTER_NOTEBOOKS']
hw_data_files = []
ovl_dest = 'lepton'


# check whether board is supported
def check_env():
    if not os.path.isdir(repo_board_folder):
        raise ValueError("Board {} is not supported.".format(board))
    if not os.path.isdir(board_notebooks_dir):
        raise ValueError("Directory {} does not exist.".format(board_notebooks_dir))


# copy overlays to python package
def copy_overlays():
    src_ol_dir = os.path.join(repo_board_folder, 'bitstream')
    dst_ol_dir = os.path.join(ovl_dest, 'bitstream')
    print("install", dst_ol_dir)
    copy_tree(src_ol_dir, dst_ol_dir)
    hw_data_files.extend([os.path.join("..", dst_ol_dir, f) for f in os.listdir(dst_ol_dir)])


# copy notebooks to jupyter home
def copy_notebooks():
    src_nb_dir = os.path.join(repo_board_folder, 'notebook')
    dst_nb_dir = os.path.join(board_notebooks_dir, 'FLIR_Lepton')
    if os.path.exists(dst_nb_dir):
        shutil.rmtree(dst_nb_dir)
    copy_tree(src_nb_dir, dst_nb_dir)

print("installing")
check_env()
copy_overlays()
copy_notebooks()

setup(
	name= "lepton",
	version= "1.2",
	url= 'https://github.com/ATaylorCEngFIET/FLIR_LEPTON_PYNQ',
	license = 'Apache Software License',
	author= "Adam Taylor",
	author_email= "adam@adiuvoengineering.com",
	packages= find_packages(),
	package_data= {
	 '': hw_data_files,
	},
	description= "FLIR Lepton",
)