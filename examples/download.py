import tempfile

from ..nexradaws.nexradawsinterface import NexradAwsInterface

templocation = tempfile.mkdtemp()
conn = NexradAwsInterface()
scans = conn.get_avail_scans("2024", "05", "09", "KILN")

localfiles = conn.download(scans[0:12], templocation)
print(localfiles.success)
print(localfiles.success[0].filepath)
