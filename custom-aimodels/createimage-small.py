import subprocess
import sys

model_name = sys.argv[1]

script_args = '--steps 50 '\
  ' --from-file custom-aimodels/prompts.txt '\
  ' --n_samples 1 '\
  ' --n_iter 1 '\
 f' --ckpt /var/meadowrun/machine_cache/{model_name} '\
  ' --config configs/stable-diffusion/v2-inference-v.yaml'\
  ' --outdir /tmp/outputs '

subprocess.check_output('python scripts/txt2img.py ' + script_args, shell=True).decode('utf-8')

