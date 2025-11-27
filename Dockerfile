FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && \
    apt-get install -y unzip bash && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Working directory
WORKDIR /opt/app

# Copy the one ZIP file inside installer/ into /opt/app
COPY installer/*.zip /opt/app/

# Unzip the installer and set permissions
RUN unzip *.zip && \
    chmod +x install.sh

# Build argument for service user
ARG SERVICE_USER=USER

# Run the installer
RUN ./install.sh

# Expose required port
EXPOSE 5618

CMD ["/bin/bash", "run.sh"]
