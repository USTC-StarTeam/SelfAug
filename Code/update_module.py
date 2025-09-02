import os

base_path = '/usr/local/lib/python3.10/dist-packages'
module_map = {
   "modeling_qwen2.py":"transformers/models/qwen2/modeling_qwen2.py",
   "layer.py":"peft/tuners/lora/layer.py",
    }
for k,v in module_map.items():
    v = os.path.join(base_path, v)
    cmd = f'cp {k} {v}'
    print(cmd)
    os.system(cmd)
