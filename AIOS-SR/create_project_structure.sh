#!/bin/bash

# Define your project name
project="AIOS-SR Project"

# Define the folder structure in an array
folders=(
    "Documentation/User Guide"
    "Documentation/Developer Guide"
    "Documentation/Tool Documentation"
    "Source Code/Boot Environment"
    "Source Code/User Interface"
    "Source Code/Tool Integration Scripts"
    "Tools/Recovery Tools"
    "Tools/Diagnostic Tools"
    "Tools/Data Recovery Tools"
    "Tests/Unit Tests"
    "Tests/Integration Tests"
    "Tests/System Tests"
    "Resources/Logos and Branding"
    "Resources/Licenses"
    "Build/Build Scripts"
    "Build/Output"
    "Releases/AIOS-SR v1.0"
    "Releases/AIOS-SR v1.1"
)

# Create directories
for folder in "${folders[@]}"; do
    mkdir -p "$project/$folder"
done

# Create empty README.md and LICENSE files
touch "$project/README.md"
touch "$project/LICENSE"

echo "Project structure created for $project"
