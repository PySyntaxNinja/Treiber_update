# مسیرهای لاگ‌ها را تعریف کنید
lsbsetup_log_path = "LSBSetup_ Log.txt"  # توجه کنید که یک فاصله بعد از LSBSetup_ وجود دارد
system_update_log_path = "System_Update_Log.txt"

# دو لیست برای ذخیره مسیرهای پیدا شده
lsbsetup_paths = []
system_update_paths = []

# خواندن لاگ LSBSetup
with open(lsbsetup_log_path, "r") as file:
    for line in file:
        if "Found: " in line:
            path = line.split("Found: ")[1].strip()
            lsbsetup_paths.append(path)

# خواندن لاگ System_Update
with open(system_update_log_path, "r") as file:
    for line in file:
        if "Found: " in line:
            path = line.split("Found: ")[1].strip()
            system_update_paths.append(path)

# پیدا کردن مسیرهایی که LSBSetup وجود دارد ولی System_Update وجود ندارد
missing_system_update = [path for path in lsbsetup_paths if path.replace("LSBSetup.exe", "System_Update.exe") not in system_update_paths]

# نمایش مسیرهایی که مشکل دارند
if missing_system_update:
    print("Paths where LSBSetup.exe exists but System_Update.exe is missing:")
    for path in missing_system_update:
        print(path)
else:
    print("No paths found where LSBSetup.exe exists and System_Update.exe is missing.")
