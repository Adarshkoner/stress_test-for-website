import subprocess
import argparse
import time
import requests

def check_page(url):
    """
    Check if the given page is responding with HTTP 200.
    """
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except Exception:
        return False

def run_locust(target_url, check_url, start_users, step, max_users, spawn_rate, duration_per_step):
    current_users = start_users
    while current_users <= max_users:
        print(f"\n🚀 Running test with {current_users} users...")
        cmd = [
            "locust",
            "-f", "locustfile.py",
            "--headless",
            "-u", str(current_users),
            "-r", str(spawn_rate),
            "-t", duration_per_step,
            "--host", target_url
        ]
        subprocess.run(cmd)

        # After each round, check chosen page
        if not check_page(check_url):
            print("⚠️ Website performance limit reached or site unavailable.")
            break

        current_users += step
        time.sleep(5)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Website Stress Test CLI with Auto-Ramp and Page Check")
    parser.add_argument("url", help="Target website base URL (e.g., https://example.com)")
    parser.add_argument("--check", help="Page to check (e.g., https://example.com/)", required=True)
    parser.add_argument("-s", "--start", type=int, default=100, help="Starting number of users")
    parser.add_argument("-p", "--step", type=int, default=100, help="Increase users by this step each round")
    parser.add_argument("-m", "--max", type=int, default=2000, help="Maximum number of users")
    parser.add_argument("-r", "--rate", type=int, default=50, help="Spawn rate (users/sec)")
    parser.add_argument("-d", "--duration", default="5m", help="Duration per step (e.g., 5m, 10m)")

    args = parser.parse_args()
    run_locust(args.url, args.check, args.start, args.step, args.max, args.rate, args.duration)
