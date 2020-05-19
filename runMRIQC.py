import os.path as op

from mriqc.workflows.anatomical import anat_qc_workflow
from mriqc.testing import mock_config

datadir = '/home/kilimanjaro2/Research/monkeyStuff/bidsData/' 

with mock_config():
    wf = anat_qc_workflow([op.join(datadir, 'sub-100/anat/sub-100_T1w.nii.gz')])
    wf.run()
    wf = anat_qc_workflow([op.join(datadir, 'sub-101/anat/sub-101_T1w.nii.gz')])
    wf.run()
    wf = anat_qc_workflow([op.join(datadir, 'sub-102/anat/sub-102_T1w.nii.gz')])
    wf.run()
#    wf = anat_qc_workflow([op.join(datadir, 'sub-152/anat/sub-152_T1w.nii.gz')])
#   wf.run()
#    wf = anat_qc_workflow([op.join(datadir, 'sub-154/anat/sub-154_T1w.nii.gz')])
#    wf.run()
#    wf = anat_qc_workflow([op.join(datadir, 'sub-156/anat/sub-156_T1w.nii.gz')])
#    wf.run()
#    wf = anat_qc_workflow([op.join(datadir, 'sub-158/anat/sub-158_T1w.nii.gz')])
#    wf.run()
#    wf = anat_qc_workflow([op.join(datadir, 'sub-160/anat/sub-160_T1w.nii.gz')])
#    wf.run()
#    wf = anat_qc_workflow([op.join(datadir, 'sub-162/anat/sub-162_T1w.nii.gz')])
#    wf.run()
#    wf = anat_qc_workflow([op.join(datadir, 'sub-164/anat/sub-164_T1w.nii.gz')])
#    wf.run()
        
