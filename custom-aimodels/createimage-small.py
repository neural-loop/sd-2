import subprocess
import sys

model_name = sys.argv[1]

script_args = ' --steps 500 '\
  ' --H 512 '\
  ' --W 896 '\
  ' --dpm'\
  ' --n_samples 1 '\
  ' --n_iter 1 '\
  ' --scale 8 '\
  ' --from-file custom-aimodels/prompts.txt '\
 f' --ckpt /var/meadowrun/machine_cache/{model_name} '\
  ' --seed 1330 '\
  ' --config configs/stable-diffusion/v2-inference.yaml'\
  ' --precision autocast '\
  ' --outdir /tmp/outputs '

subprocess.check_output('python scripts/txt2img.py ' + script_args, shell=True).decode('utf-8')

