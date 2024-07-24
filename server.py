import logging

# Set up logging
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_server_event(event, level=logging.INFO):
    logging.log(level, event)

# Example usage
log_server_event("User logged in successfully", level=logging.INFO)
log_server_event("Error: Unable to translate Python code to Z-Lang", level=logging.ERROR)
log_server_event("User completed tutorial 3", level=logging.INFO)sudo netstat -a | grep :8080