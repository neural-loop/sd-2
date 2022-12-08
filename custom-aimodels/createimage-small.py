import subprocess
import sys

model_name = sys.argv[1]

script_args = '--steps 50 '\
  ' --prompt "a professional photograph of an astronaut riding a triceratops" '\
 f' --ckpt /var/meadowrun/machine_cache/{model_name} '\
  ' --config configs/stable-diffusion/v2-inference-v.yaml'\
  ' --outdir /tmp/outputs '

subprocess.check_output('python scripts/txt2img.py ' + script_args, shell=True).decode('utf-8')

