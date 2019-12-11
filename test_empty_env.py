import time
import subprocess

start = time.time()

for i in range(1, 6):
    subprocess.call("./python_package_analyze empty_env.py output.json; \
                     ./python_package_create output.json venv{}; \
                     ./python_package_run venv{} \"python3 empty_env.py\";".format(i, i), shell=True)

end = time.time()

print("Average runtime: {:2f} seconds".format((end - start) / 5))
