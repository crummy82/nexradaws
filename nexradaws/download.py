import tempfile

import nexradawsinterface

bucket = "noaa-nexrad-level2"
num_files = 2
templocation = tempfile.mkdtemp()
conn = nexradawsinterface.NexradAwsInterface()
scans = conn.get_avail_scans(bucket, "2024", "05", "09", "KILN")

localfiles = conn.download(scans[-2:], templocation)
print(localfiles.success)
print(localfiles.success[0].filepath)
