import os.path as op

from mriqc.workflows.anatomical import anat_qc_workflow
from mriqc.testing import mock_config

datadir = '/home/kilimanjaro2/Research/monkeyStuff/bidsData/' 

with mock_config():
    wf = anat_qc_workflow([op.join(datadir, 'sub-103/anat/sub-103_T1w.nii.gz')])
    wf.run()
    wf = anat_qc_workflow([op.join(datadir, 'sub-104/anat/sub-104_T1w.nii.gz')])
    wf.run()

