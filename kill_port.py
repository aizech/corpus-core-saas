import subprocess
import sys
import os

def kill_port_process(port):
    """Kill any process running on the specified port"""
    try:
        # Check if any process is running on the port (both IPv4 and IPv6)
        result = subprocess.run(
            ["powershell", "-Command", f"Get-NetTCPConnection -LocalPort {port} | Select-Object -ExpandProperty OwningProcess"],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0 and result.stdout.strip():
            # Get unique process IDs
            pids = list(set(result.stdout.strip().split('\n')))
            print(f"Found processes running on port {port}: {pids}")
            
            # Kill each process
            for pid in pids:
                if pid.strip() and pid.strip() != 'OwningProcess':
                    try:
                        subprocess.run(
                            ["powershell", "-Command", f"Stop-Process -Id {pid.strip()} -Force"],
                            check=True,
                            timeout=10
                        )
                        print(f"Successfully killed process with PID {pid.strip()}")
                    except subprocess.CalledProcessError as e:
                        print(f"Failed to kill process with PID {pid.strip()}: {e}")
                    except Exception as e:
                        print(f"Error killing process with PID {pid.strip()}: {e}")
        else:
            print(f"No processes found running on port {port}")
    except subprocess.TimeoutExpired:
        print(f"Timeout while checking processes on port {port}")
    except Exception as e:
        print(f"Error checking/killing processes on port {port}: {e}")

if __name__ == "__main__":
    # Read port from config.toml
    config_path = os.path.join(os.path.dirname(__file__), ".streamlit", "config.toml")
    
    try:
        with open(config_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip().startswith("port ="):
                    port = int(line.split("=")[1].strip())
                    print(f"Killing processes on port {port}...")
                    kill_port_process(port)
                    break
            else:
                # Default Streamlit port
                print("Port not found in config.toml, using default port 8501...")
                kill_port_process(8501)
    except FileNotFoundError:
        print("config.toml not found, using default port 8501...")
        kill_port_process(8501)
    except Exception as e:
        print(f"Error reading config.toml: {e}")
        kill_port_process(8501)
