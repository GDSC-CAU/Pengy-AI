import argparse
from ultralytics import YOLO

def export_model(model_path, export_format):
    # Load the specified YOLO model
    model = YOLO(model_path)

    # Validate export format
    if export_format not in ['tflite', 'onnx', 'torchscript']:
        raise ValueError("Unsupported export format. Please choose from 'tflite', 'onnx', 'torchscript'.")

    # Export the model to the specified format
    model.export(format=export_format)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Export a YOLO model to a specified format.")
    parser.add_argument("model", type=str, help="Path to the model file.")
    parser.add_argument("format", type=str, choices=['tflite', 'onnx', 'torchscript'], help="The format to export the model to.")

    # Parse arguments
    args = parser.parse_args()

    # Call the export function with the model path and format
    export_model(args.model, args.format)