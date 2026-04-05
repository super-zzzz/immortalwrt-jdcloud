import os
import subprocess
import shutil

print("Checking out base branch...")
subprocess.run(['git', 'checkout', '-f', '-B', 're-ss-01-nss-v25.12.0-rc1', 'v25.12.0-rc1'])

print("Removing old directories to avoid ghost files...")
for d in [
    'target/linux/qualcommax',
    'package/firmware/ipq-wifi',
    'package/kernel/qca-nss-dp',
    'package/kernel/qca-ssdk'
]:
    d = d.replace('/', os.sep)
    if os.path.exists(d):
        shutil.rmtree(d, ignore_errors=True)

print("Checking out corresponding directories from main...")
subprocess.run([
    'git', 'checkout', 'main', '--',
    'target/linux/qualcommax',
    'package/firmware/ipq-wifi',
    'package/kernel/qca-nss-dp',
    'package/kernel/qca-ssdk',
    'package/boot/uboot-envtools',
    'package/boot/uboot-tools'
])

print("Committing the ported NSS driver and JDCloud support...")
subprocess.run(['git', 'add', '-A'])
subprocess.run(['git', 'commit', '-m', 'Port VIKINGYFY full NSS driver and JDCloud support (re-ss-01/etc)'])
print("Done!")
