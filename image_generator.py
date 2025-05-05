from diffusers import StableDiffusionPipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from io import BytesIO
import base64
import warnings
from PIL import Image

class StoryImageGenerator:
    def __init__(self):
        # Load image generation model
        self.pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5").to("cpu")

        # Load story generation model
        self.tokenizer = AutoTokenizer.from_pretrained("pranavpsv/gpt2-genre-story-generator")
        self.model = AutoModelForCausalLM.from_pretrained("pranavpsv/gpt2-genre-story-generator")

    def generate_story(self, prompt):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        output = self.model.generate(
            input_ids,
            max_length=150,  # Adjust the length of the output
            temperature=0.9,  # Allow more creativity
            top_p=0.95,
            top_k=50,
            do_sample=True,
            pad_token_id=self.tokenizer.eos_token_id
        )
        story = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return story.strip()

    def split_story_into_parts(self, story, max_sentences_per_part=2):
        sentences = story.split(".")
        parts = [".".join(sentences[i:i + max_sentences_per_part]).strip() 
                 for i in range(0, len(sentences), max_sentences_per_part)]
        return [p for p in parts if p]

    def generate_story_and_images(self, prompt):
        story = self.generate_story(prompt)
        story_parts = self.split_story_into_parts(story)

        images = []
        for idx, part in enumerate(story_parts[:2]):  # Only 2 images max
            try:
                image = self.pipe(prompt=part, num_inference_steps=50).images[0]  # Faster generation
                buffered = BytesIO()
                image.save(buffered, format="PNG")
                image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
                images.append(image_base64)
            except Exception as e:
                warnings.warn(f"Image generation failed for part {idx}: {e}")

        return story, images
