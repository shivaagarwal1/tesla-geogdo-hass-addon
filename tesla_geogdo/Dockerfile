# Use Home Assistant base image (adjust version as needed)
FROM ghcr.io/hassio-addons/base:12.2.7

# Copy script
COPY run.sh /run.sh
RUN chmod +x /run.sh

# Start
CMD [ "/run.sh" ]
