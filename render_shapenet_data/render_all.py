# Copyright (c) 2022, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.
#
# NVIDIA CORPORATION & AFFILIATES and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION & AFFILIATES is strictly prohibited.

import os
import argparse

# python render_all.py --save_folder PATH_TO_SAVE_IMAGE --dataset_folder PATH_TO_3D_OBJ --blender_root PATH_TO_BLENDER

parser = argparse.ArgumentParser(description='Renders given obj file by rotation a camera around it.')
parser.add_argument(
    '--save_folder', type=str, default='/data1/miyan/ShapeNetRender/03001627',
    help='path for saving rendered image')
parser.add_argument(
    '--dataset_folder', type=str, default='/data1/miyan/ShapeNetCore.v2',
    help='path for downloaded 3d dataset folder')
parser.add_argument(
    '--blender_root', type=str, default='/home/miyan/blender-2.93.3-linux-x64/blender',
    help='path for blender')
parser.add_argument(
    '--split', type=int)
args = parser.parse_args()

save_folder = args.save_folder
dataset_folder = args.dataset_folder
blender_root = args.blender_root

synset_list = [
    # '02958343',  # Car
    '03001627',  # Chair
    # '03790512'  # Motorbike
]
scale_list = [
    # 0.9,
    0.7,
    # 0.9
]

for synset, obj_scale in zip(synset_list, scale_list):
    file_list = sorted(os.listdir(os.path.join(dataset_folder, synset)))
    file_list = file_list[args.split::8]

    for idx, file in enumerate(file_list):
        render_cmd = '%s -b -P render_shapenet.py -- --output %s %s  --scale %f --views 24 --resolution 1024' % (
            blender_root, save_folder, os.path.join(dataset_folder, synset, file, 'models/model_normalized.obj'), obj_scale
        )
        os.system(render_cmd)
