import paramiko
import datetime
import time


def measure_ssh_latency(hostname, username, key_filename):
    start_time = time.time()

    # Create an SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Load the private key
        private_key = paramiko.Ed25519Key.from_private_key_file(key_filename)

        # Connect to the remote host using key-based authentication
        client.connect(hostname, username=username, pkey=private_key)

        # Measure the time taken for the SSH handshake
        latency = time.time() - start_time
        return latency

    except paramiko.AuthenticationException:
        print("Authentication failed.")
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {str(e)}")
    finally:
        # Close the SSH connection
        client.close()


# Usage example
lat = measure_ssh_latency("35.192.74.88", "mlewis", "/home/tau/.ssh/gbc-oberon")
# Get the time theconnection was closed
end_time = datetime.datetime.now()
dt_string = end_time.strftime("%m/%d/%Y %H:%M:%S")
# Log the time stamp and the latency to a csv file
log_file = open("ssh_latency.log", "a")  # append mode
log_file.write(f"{dt_string}, {lat}\n")
log_file.close()
# Print the latency
print(f"SSH latency: {lat:.2f} seconds")
# Use a crontab to run this script every 5 minutes and log errors, and latency to a file
# */5 * * * * /usr/bin/python3 /home/USER/gbc_ssh_latency.py >> /home/USER/cron.log 2>&1
