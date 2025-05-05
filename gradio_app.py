import gradio as gr
import base64
from PIL import Image
import io
from image_generator import StoryImageGenerator

# Create StoryImageGenerator instance
generator = StoryImageGenerator()

# Gradio interface function
def generate_story_and_images(prompt):
    story, images_base64 = generator.generate_story_and_images(prompt)
    
    # Decode base64 images to PIL images
    images = [Image.open(io.BytesIO(base64.b64decode(img))) for img in images_base64]

    return story, images

# Fancy CSS to beautify everything in pink and dreamy style
custom_css = """
body {
    background: linear-gradient(135deg, #f7f0ff, #e6f2ff);
    font-family: 'Segoe UI', sans-serif;
    color: #333;
}

.gradio-container {
    padding: 40px;
    max-width: 900px;
    margin: auto;
}

textarea {
    background-color: #ffffff !important;
    border: 1.5px solid #cccccc !important;
    border-radius: 10px !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    font-size: 16px;
    padding: 12px;
}

button {
    background-color: #4a90e2 !important;
    color: white !important;
    font-weight: 600;
    border: none !important;
    padding: 12px 24px;
    border-radius: 8px !important;
    box-shadow: 0 4px 12px rgba(74, 144, 226, 0.2);
    transition: background 0.3s ease;
    font-size: 16px;
}

button:hover {
    background-color: #357ABD !important;
}

h1, h2, .title, .description {
    color: #2d2d2d !important;
    text-align: center;
    font-weight: 600;
}

.output-image {
    border: 2px solid #ddd !important;
    border-radius: 12px !important;
    box-shadow: 0 2px 12px rgba(0,0,0,0.08);
    transition: transform 0.2s ease;
}

.output-image:hover {
    transform: scale(1.02);
}
"""


iface = gr.Interface(
    fn=generate_story_and_images,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Enter your story prompt (e.g., 'A forest full of talking animals...')",
        label="📘 Enter a Story Prompt"
    ),
    outputs=[
        gr.Textbox(label="📝 Generated Story"),
        gr.Gallery(label="🖼️ Illustrations", elem_classes=["output-image"], columns=2)
    ],
    title="📚 StoryBook Generator",
    description="Turn a short text prompt into a creative story with accompanying AI-generated illustrations.",
    css=custom_css
)

if __name__ == "__main__":
    iface.launch()
