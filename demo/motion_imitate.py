# Copyright (c) 2020-2021 impersonator.org authors (Wen Liu and Zhixin Piao). All rights reserved.
import os
import os.path as osp
import platform
import subprocess
import sys
import time

from iPERCore.services.options.options_setup import setup
from iPERCore.services.run_imitator import run_imitator


###############################################################################################
##                   Setting
###############################################################################################

def main(src_path, ref_path, model_id, gpu_ids, image_size, num_source, output_dir, assets_dir):
    work_asserts_dir = os.path.join("./assets")
    if not os.path.exists(work_asserts_dir):
        os.symlink(osp.abspath(assets_dir), osp.abspath(work_asserts_dir),
                target_is_directory=(platform.system() == "Windows"))

    cfg_path = osp.join(work_asserts_dir, "configs", "deploy.toml")

    cmd = [
        sys.executable, "-m", "iPERCore.services.run_imitator",
        "--cfg_path", cfg_path,
        "--gpu_ids", gpu_ids,
        "--image_size", str(image_size),
        "--num_source", str(num_source),
        "--output_dir", output_dir,
        "--model_id", model_id,
        "--src_path", src_path,
        "--ref_path", ref_path
    ]

    subprocess.call(cmd)

