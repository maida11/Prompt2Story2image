from diffusers import StableDiffusionPipeline
import torch


# Load model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
).to("cuda")  # Use "cpu" if no GPU

# Generate image
prompt = "ok "
image = pipe(prompt).images[0]

# Save or show image
image.save("generated_image.png")
image.show()