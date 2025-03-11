#!/bin/bash

echo "Starting Ollama server..."
ollama serve &  # Start Ollama in the background

echo "Ollama is ready, creating the model..."

ollama create retail-assistant -f model_files/Modelfile
ollama run retail-assistant