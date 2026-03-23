import os
import shutil

# for i in range(3):
#     print("checking disk usases...")
#     #os.system("df -h") only works on the linux/ubuntu
#     data = os.system("wmic logicaldisk get size,freespace,caption")

    




# print("Checking disk usage...\n")

# drives = ["C:\\", "D:\\", "E:\\"]

# for drive in drives:
#     total, used, free = shutil.disk_usage(drive)

#     total_gb = total // (2**30)
#     used_gb = used // (2**30)
#     free_gb = free // (2**30)

#     print(f"Drive: {drive}")
#     print(f"Total: {total_gb} GB")
#     print(f"Used : {used_gb} GB")
#     print(f"Free : {free_gb} GB")

#     if free_gb < 10:
#         print("CRITICAL")
#     elif free_gb < 20:
#         print("WARNING")
#     else:
#         print("helthy!")        

#     print("----------------------")

    

import shutil

print("Checking disk usage...\n")

drives = ["C:\\", "D:\\", "E:\\"]

for drive in drives:
    total, used, free = shutil.disk_usage(drive)

    # Convert bytes to GB
    total_gb = total // (2**30)
    used_gb = used // (2**30)
    free_gb = free // (2**30)

    # Print disk info
    print(f"Drive: {drive}")
    print(f"Total: {total_gb} GB")
    print(f"Used : {used_gb} GB")
    print(f"Free : {free_gb} GB")

    # Status logic
    if free_gb < 10:
        print("🔴 CRITICAL")
    elif free_gb < 20:
        print("🟡 WARNING")
    else:
        print("🟢 HEALTHY")        

    print("----------------------")    