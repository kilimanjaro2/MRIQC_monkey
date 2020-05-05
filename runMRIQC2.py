import os.path as op

from mriqc.workflows.anatomical import anat_qc_workflow
from mriqc.testing import mock_config

datadir = '/home/kilimanjaro2/Research/monkeyStuff/bidsData/' 

with mock_config():
    wf = anat_qc_workflow([op.join(datadir, 'sub-002/anat/sub-002_T1w.nii.gz')])
    wf.run()
        
