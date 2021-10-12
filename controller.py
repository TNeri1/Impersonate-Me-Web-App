import demo.motion_imitate as imitate
import time

def convertor(src_path = "path=/content/Impersonate-Me-Web-App/assets/samples/sources/donald_trump_2/00000.PNG", ref_path = "path=/content/Impersonate-Me-Web-App/assets/samples/references/mabaoguo_short.mp4, pose_fc=400", gpu_ids = 0, image_size = 512, num_source = 2, output_dir="./results", assets_dir = "./assets"):
    model_id = "model_" + str(time.time())
    ref_id = "ref_" + str(time.time())
    src_path += "name=" + model_id
    ref_path += "name=" + ref_id
    imitate.main(src_path, ref_path, model_id, gpu_ids, image_size, num_source, output_dir, assets_dir)
    
    productpath = "./results/primitives/"+ model_id+"/synthesis/imitations/"+ model_id +"-"+ ref_id +".mp4"
    
    return productpath