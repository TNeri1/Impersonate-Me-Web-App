import os
import os.path as osp
import platform
import subprocess
import sys
import random

from iPERCore.services.options.options_setup import setup



###############################################################################################
##                   Setting
###############################################################################################
pc_id = random.randrange(1,1000)

# the gpu ids
gpu_ids = "0"

# the image size
image_size = 512

# the default number of source images, it will be updated if the actual number of sources <= num_source
num_source = 1

# the assets directory. This is very important, please download it from `one_drive_url` firstly.
assets_dir = "/assets"

# the output directory.
output_dir = "./media/products"

work_asserts_dir = os.path.join("./assets")
if not os.path.exists(work_asserts_dir):
    os.symlink(osp.abspath(assets_dir), osp.abspath(work_asserts_dir),
            target_is_directory=(platform.system() == "Windows"))

cfg_path = osp.join(work_asserts_dir, "configs", "deploy.toml")

model_id = "donald_trump_2"
pic_path = ""
videopath = ""
if (pic_path == ""):
    # the source input information, here \" is escape character of double duote "
    src_path = "\"media/samples/sources/donald_trump_2/00000.PNG,name?=donald_trump_2\""
else:
    src_path = "\""+ pic_path +",name?=donald_trump_\""

if (videopath == ""):
    ref_path = "\"path?=/media/samples/references/mabaoguo_short.mp4," \
                "name?=mabaoguo_short," \
                "pose_fc?=400"
else:
    ref_path = "\"path?="+ videopath +"," \
                "pose_fc?=400"


# # run imitator
# cfg = setup(args)
# run_imitator(cfg) 
# or use the system call wrapper
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

# This is a specific model name, and it will be used if you do not change it. This is the case of `trump`
resultpath = "./media/products/" + str(model_id) + "-" + str(pc_id) + ".mp4"

print(resultpath)
