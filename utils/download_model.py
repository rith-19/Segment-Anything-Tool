import os

def download_model(model_type):
    """
    model_type: str, A string representing the model type. It can be 'vit_h', 'vit_l', or 'vit_b'.
    """

    # Check if the model file already exists
    filename = f"{model_type}.pth"
    if os.path.exists(filename):
        print(f"{model_type} model already exists as '{filename}'. Using existing model file.")
    else:
        raise FileNotFoundError(f"{model_type} model file '{filename}' not found in the root directory.")

    return filename

# Example usage:
model_type = "vit_h"
model_file = download_model(model_type)
print("Model file path:", model_file)
