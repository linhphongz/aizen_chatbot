from llama_cpp import Llama
from llama_cpp.llama_chat_format import Llava15ChatHandler
import base64


# This function loads the Llama model and sets up the chat handler for the model.
def initialize_model():
    chat_format_handler = Llava15ChatHandler(clip_model_path="./models/mmproj-model-f16.gguf")
    model = Llama(
        model_path="./models/ggml-model-q4_k.gguf",
        chat_handler=chat_format_handler,
        logits_all=True,
        n_ctx=1024 
    )
    return model

# This function converts a byte array of an image to a base64 encoded string and returns it as a data URL format.
def encode_image_to_base64(image_data):
    base64_string = base64.b64encode(image_data).decode("utf-8")
    return "data:image/jpeg;base64," + base64_string

# This function takes image content in bytes and a user message, then generates a descriptive response about the image using the Llama model.
def describe_image(image_data, user_input):
    llama_model = initialize_model()  # Load the model
    base64_image = encode_image_to_base64(image_data)  # Convert the image to base64 format

    # Generate a response from the model with the user's message and image
    response = llama_model.create_chat_completion(
        messages=[
            {"role": "system", "content": "You are an assistant who perfectly describes images."},
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": base64_image}},
                    {"type": "text", "text": user_input}
                ]
            }
        ]
    )
    return response["choices"][0]["message"]["content"]  # Return the content of the model's response
