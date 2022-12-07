import asyncio
import meadowrun

def main():
    s3_bucket_name = "visioninit-sd"  # replace this with your own bucket name!
    folder_name = "plaintest"
    prompt = "a professional illustration of a steampunk computer floating in the clouds, high-quality"
    ckpt_name = "768-v-ema.ckpt"

    asyncio.run(
        meadowrun.run_command(
            'bash -c \''
            f'aws s3 sync s3://{s3_bucket_name} /var/meadowrun/machine_cache --exclude "*" '
            f'--include {ckpt_name} '
            f'&& python scripts/txt2img.py --prompt "{prompt}"  '
            f'--ckpt /var/meadowrun/machine_cache/{ckpt_name} --outdir /tmp/outputs '
            '--config configs/stable-diffusion/v2-inference.yaml '
            f'&& aws s3 sync /tmp/outputs s3://{s3_bucket_name}/{folder_name}\'',
            meadowrun.AllocCloudInstance("EC2"),
            meadowrun.Resources(
                logical_cpu=1, memory_gb=32, max_eviction_rate=80,
                gpu_memory=16, flags="nvidia"
            ),
            meadowrun.Deployment.git_repo(
                "https://github.com/Stability-AI/stablediffusion",
                interpreter=meadowrun.CondaEnvironmentYmlFile(
                    "environment.yaml", additional_software=["awscli", "libgl1"]
                ),
                environment_variables={
                    "TRANSFORMERS_CACHE": "/var/meadowrun/machine_cache/transformers"
                }
            )
        )
    )

if __name__ == "__main__":
    main()