from os.path import join, dirname, abspath
import json

from auditwheel import policy

policies = None

#with open(join(dirname(abspath(policy.__file__)), "policy.json")) as f:
with open(join(dirname(abspath(policy.__file__)), "manylinux-policy.json")) as f:
    policies = json.load(f)

for p in policies:
#    if p["name"] == "manylinux2014":
#        p["lib_whitelist"].append("libxcb.so.1")
#    p["lib_whitelist"].append("")
    p["lib_whitelist"].append("libxcb.so.1")
#    p["lib_whitelist"].append("libQt5Core.so.5")
#    p["lib_whitelist"].append("libQt5Gui.so.5")
#    p["lib_whitelist"].append("libxcb.so.1.1.0")
#    p["lib_whitelist"].append("libxcb-shm.so.0.0.0")
#    p["lib_whitelist"].append("libxcb-render.so.0.0.0")
#    p["lib_whitelist"].append("libxcb-keysyms.so.1.0.0")
#    p["lib_whitelist"].append("libxcb-xkb.so.1.0.0")
#    p["lib_whitelist"].append("libQt5XcbQpa.so.5")
#    p["lib_whitelist"].append("libxcb-image.so.0.0.0")
#    p["lib_whitelist"].append("libgfortran.so.3")
#    p["lib_whitelist"].append("libxkbcommon-x11.so.0.0.0")
#    p["lib_whitelist"].append("libxcb-image.so.0.0.0")
#    p["lib_whitelist"].append("libX11-xcb.so.1.0.0")
#    p["lib_whitelist"].append("")
#    p["lib_whitelist"].append("")
#    p["lib_whitelist"].append("")
#    p["lib_whitelist"].append("")
#    p["lib_whitelist"].append("")
#    p["lib_whitelist"].append("")
#    p["lib_whitelist"].append("")
#    p["lib_whitelist"].append("")
#    p["lib_whitelist"].append("")
#    p["lib_whitelist"].append("")
#    p["lib_whitelist"].append("")
#    p["lib_whitelist"].append("")
#    p["lib_whitelist"].append("")


#with open(join(dirname(abspath(policy.__file__)), "policy.json"), "w") as f:
with open(join(dirname(abspath(policy.__file__)), "manylinux-policy.json"), "w") as f:
    f.write(json.dumps(policies))
