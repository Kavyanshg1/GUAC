import logging

# Set up logging
logging.basicConfig(filename='output.log', level=logging.INFO, format='%(message)s')

def log_output(output):
    logging.info(output)

# Example usage
log_output("Hello, World!")
log_output("The answer is: 42")