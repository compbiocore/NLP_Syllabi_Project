# Use Ubuntu operating system as base
FROM ubuntu

# Create /app folder on docker container
WORKDIR /app

# Copy all the files from current host folder to /app folder
COPY . /app

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Install Python dependancies from your requirements.txt file    
RUN pip3 install -r requirements.txt

# Expose port so user can access it 
EXPOSE 8866

# Run voila when the container is launched
CMD voila web.ipynb


