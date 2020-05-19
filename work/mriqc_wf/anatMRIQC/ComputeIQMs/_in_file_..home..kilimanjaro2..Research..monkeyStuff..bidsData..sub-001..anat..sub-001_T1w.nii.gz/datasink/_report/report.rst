Node: anatMRIQC (ComputeIQMs (datasink (bids)
=============================================


 Hierarchy : mriqc_wf.anatMRIQC.ComputeIQMs.datasink
 Exec ID : datasink.a0


Original Inputs
---------------


* _outputs : {'qi_2': 0.0008084858429067759}
* acq_id : <undefined>
* dataset : <unset>
* in_file : /home/kilimanjaro2/Research/monkeyStuff/bidsData/sub-001/anat/sub-001_T1w.nii.gz
* metadata : {'AcquisitionMatrixPE': 128, 'AcquisitionNumber': 1, 'AcquisitionTime': '08:31:11.347500', 'BaseResolution': 128, 'ConversionSoftware': 'dcm2niix', 'ConversionSoftwareVersion': 'v1.0.20171215 GCC4.8.4', 'DeviceSerialNumber': '35302', 'DwellTime': 3e-05, 'EchoTime': 0.00338, 'FlipAngle': 15, 'ImageOrientationPatientDICOM': [1, 0, 0, 0, 0, -1], 'ImageType': ['ORIGINAL', 'PRIMARY', 'M', 'ND', 'NORM'], 'InPlanePhaseEncodingDirectionDICOM': 'ROW', 'InstitutionAddress': 'ZHONG_SHAN_BEI_3663_SHANGHAI_f87c9c_District_CN_200062', 'InstitutionName': 'East_China_Normal_University', 'InstitutionalDepartmentName': 'Department', 'InversionTime': 0.9, 'MRAcquisitionType': '3D', 'MagneticFieldStrength': 3, 'Manufacturer': 'Siemens', 'ManufacturersModelName': 'TrioTim', 'Modality': 'MR', 'PartialFourier': 1, 'PatientPosition': 'HFS', 'PercentPhaseFOV': 100, 'PhaseEncodingSteps': 128, 'PhaseResolution': 1, 'PixelBandwidth': 130, 'ProcedureStepDescription': 'zhangmiao_20150320_ACC', 'ProtocolName': 't1_mpr_cor_p2_serface_coil', 'PulseSequenceDetails': '%SiemensSeq%_tfl', 'ReceiveCoilName': 'Loop_11', 'ReconMatrixPE': 128, 'RepetitionTime': 2.2, 'SAR': 0.215444, 'ScanOptions': 'IR', 'ScanningSequence': 'GR_IR', 'SequenceName': 'tfl3d1', 'SequenceVariant': 'SP_MP', 'SeriesDescription': 't1_mpr_cor_p2_serface_coil', 'SeriesNumber': 8, 'ShimSetting': [5896, -5442, 1687, 162, -213, -6, -62, 146], 'SliceThickness': 1, 'SoftwareVersions': 'syngo_MR_B17', 'StationName': 'MRC35302', 'TxRefAmp': 353.861}
* modality : T1w
* out_dir : /home/kilimanjaro2/Research/monkeyStuff/outputReports
* provenance : {'md5sum': 'f6709f4c73ea023053e3fdd9fccbf26b', 'version': '0+untagged.2628.g289cee2.dirty', 'software': 'mriqc', 'webapi_url': 'https://mriqc.nimh.nih.gov/api/v1', 'webapi_port': None, 'settings': {'testing': False}, 'warnings': {'small_air_mask': False, 'large_rot_frame': False}}
* rec_id : <undefined>
* root : {'summary_csf_mean': 160.07443237304688, 'summary_csf_stdv': 77.0881576538086, 'summary_csf_median': 154.7310791015625, 'summary_csf_mad': 77.04991157425815, 'summary_csf_p95': 298.0826416015625, 'summary_csf_p05': 40.92225646972656, 'summary_csf_k': -0.02692215661326136, 'summary_csf_n': 6701.0, 'summary_gm_mean': 646.5322265625, 'summary_gm_stdv': 45.28156661987305, 'summary_gm_median': 646.431884765625, 'summary_gm_mad': 49.40153840609348, 'summary_gm_p95': 719.0096649169922, 'summary_gm_p05': 573.9876983642578, 'summary_gm_k': -0.3710872673977037, 'summary_gm_n': 61002.0, 'summary_wm_mean': 1009.0335083007812, 'summary_wm_stdv': 89.6391830444336, 'summary_wm_median': 1000.0402221679688, 'summary_wm_mad': 95.3646051875058, 'summary_wm_p95': 1168.7696533203125, 'summary_wm_p05': 880.848876953125, 'summary_wm_k': -0.1618253438955204, 'summary_wm_n': 127551.0, 'summary_bg_mean': 32.51543045043945, 'summary_bg_stdv': 67.88570404052734, 'summary_bg_median': 20.438499450683594, 'summary_bg_mad': 11.754944858030662, 'summary_bg_p95': 73.21625862121581, 'summary_bg_p05': 6.532280969619752, 'summary_bg_k': 121.25339907502631, 'summary_bg_n': 690932.0, 'snr_csf': 2.0070467112906507, 'snr_wm': 11.15624069784611, 'snr_gm': 14.275711609587335, 'snr_total': 9.146333006241365, 'snrd_csf': 8.623601376539755, 'snrd_wm': 55.73507459882849, 'snrd_gm': 36.027480217112625, 'snrd_total': 33.46205206416029, 'cnr': 2.9171006309128025, 'fber': 600.0811157226562, 'efc': 0.7152571509595217, 'wm2max': 0.6270423168185647, 'qi_1': 0.00011091593929955452, 'cjv': 0.4093968616720737, 'fwhm_x': 5.98956, 'fwhm_y': 7.19652, 'fwhm_z': 5.49306, 'fwhm_avg': 6.22638, 'icvs_csf': 0.1470790702932391, 'icvs_gm': 0.46728560816356113, 'icvs_wm': 0.38563532154319974, 'rpve_csf': 15.348087429230825, 'rpve_gm': 5.015182490164974, 'rpve_wm': 6.161822194315344, 'size_x': 138, 'size_y': 195, 'size_z': 128, 'spacing_x': 0.5, 'spacing_y': 0.5, 'spacing_z': 0.5, 'inu_range': 0.34940123558044434, 'inu_med': 1.15684175491333, 'tpm_overlap_csf': 0.10775530338287354, 'tpm_overlap_gm': 0.4644337296485901, 'tpm_overlap_wm': 0.46268269419670105, 'qi_2': 0.0008084858429067759, 'bids_meta': {'subject_id': '001', 'modality': 'T1w', 'AcquisitionMatrixPE': 128, 'AcquisitionNumber': 1, 'AcquisitionTime': '08:31:11.347500', 'BaseResolution': 128, 'ConversionSoftware': 'dcm2niix', 'ConversionSoftwareVersion': 'v1.0.20171215 GCC4.8.4', 'DeviceSerialNumber': '35302', 'DwellTime': 3e-05, 'EchoTime': 0.00338, 'FlipAngle': 15, 'ImageOrientationPatientDICOM': [1, 0, 0, 0, 0, -1], 'ImageType': ['ORIGINAL', 'PRIMARY', 'M', 'ND', 'NORM'], 'InPlanePhaseEncodingDirectionDICOM': 'ROW', 'InstitutionAddress': 'ZHONG_SHAN_BEI_3663_SHANGHAI_f87c9c_District_CN_200062', 'InstitutionName': 'East_China_Normal_University', 'InstitutionalDepartmentName': 'Department', 'InversionTime': 0.9, 'MRAcquisitionType': '3D', 'MagneticFieldStrength': 3, 'Manufacturer': 'Siemens', 'ManufacturersModelName': 'TrioTim', 'Modality': 'MR', 'PartialFourier': 1, 'PatientPosition': 'HFS', 'PercentPhaseFOV': 100, 'PhaseEncodingSteps': 128, 'PhaseResolution': 1, 'PixelBandwidth': 130, 'ProcedureStepDescription': 'zhangmiao_20150320_ACC', 'ProtocolName': 't1_mpr_cor_p2_serface_coil', 'PulseSequenceDetails': '%SiemensSeq%_tfl', 'ReceiveCoilName': 'Loop_11', 'ReconMatrixPE': 128, 'RepetitionTime': 2.2, 'SAR': 0.215444, 'ScanOptions': 'IR', 'ScanningSequence': 'GR_IR', 'SequenceName': 'tfl3d1', 'SequenceVariant': 'SP_MP', 'SeriesDescription': 't1_mpr_cor_p2_serface_coil', 'SeriesNumber': 8, 'ShimSetting': [5896, -5442, 1687, 162, -213, -6, -62, 146], 'SliceThickness': 1, 'SoftwareVersions': 'syngo_MR_B17', 'StationName': 'MRC35302', 'TxRefAmp': 353.861, 'dataset': '<unset>'}, 'provenance': {'md5sum': 'f6709f4c73ea023053e3fdd9fccbf26b', 'version': '0+untagged.2628.g289cee2.dirty', 'software': 'mriqc', 'webapi_url': 'https://mriqc.nimh.nih.gov/api/v1', 'webapi_port': None, 'settings': {'testing': False}, 'warnings': {'small_air_mask': False, 'large_rot_frame': False}}}
* run_id : <undefined>
* session_id : <undefined>
* subject_id : 001
* task_id : <undefined>


Execution Inputs
----------------


* _outputs : {'qi_2': 0.0008084858429067759}
* acq_id : <undefined>
* dataset : <unset>
* in_file : /home/kilimanjaro2/Research/monkeyStuff/bidsData/sub-001/anat/sub-001_T1w.nii.gz
* metadata : {'AcquisitionMatrixPE': 128, 'AcquisitionNumber': 1, 'AcquisitionTime': '08:31:11.347500', 'BaseResolution': 128, 'ConversionSoftware': 'dcm2niix', 'ConversionSoftwareVersion': 'v1.0.20171215 GCC4.8.4', 'DeviceSerialNumber': '35302', 'DwellTime': 3e-05, 'EchoTime': 0.00338, 'FlipAngle': 15, 'ImageOrientationPatientDICOM': [1, 0, 0, 0, 0, -1], 'ImageType': ['ORIGINAL', 'PRIMARY', 'M', 'ND', 'NORM'], 'InPlanePhaseEncodingDirectionDICOM': 'ROW', 'InstitutionAddress': 'ZHONG_SHAN_BEI_3663_SHANGHAI_f87c9c_District_CN_200062', 'InstitutionName': 'East_China_Normal_University', 'InstitutionalDepartmentName': 'Department', 'InversionTime': 0.9, 'MRAcquisitionType': '3D', 'MagneticFieldStrength': 3, 'Manufacturer': 'Siemens', 'ManufacturersModelName': 'TrioTim', 'Modality': 'MR', 'PartialFourier': 1, 'PatientPosition': 'HFS', 'PercentPhaseFOV': 100, 'PhaseEncodingSteps': 128, 'PhaseResolution': 1, 'PixelBandwidth': 130, 'ProcedureStepDescription': 'zhangmiao_20150320_ACC', 'ProtocolName': 't1_mpr_cor_p2_serface_coil', 'PulseSequenceDetails': '%SiemensSeq%_tfl', 'ReceiveCoilName': 'Loop_11', 'ReconMatrixPE': 128, 'RepetitionTime': 2.2, 'SAR': 0.215444, 'ScanOptions': 'IR', 'ScanningSequence': 'GR_IR', 'SequenceName': 'tfl3d1', 'SequenceVariant': 'SP_MP', 'SeriesDescription': 't1_mpr_cor_p2_serface_coil', 'SeriesNumber': 8, 'ShimSetting': [5896, -5442, 1687, 162, -213, -6, -62, 146], 'SliceThickness': 1, 'SoftwareVersions': 'syngo_MR_B17', 'StationName': 'MRC35302', 'TxRefAmp': 353.861}
* modality : T1w
* out_dir : /home/kilimanjaro2/Research/monkeyStuff/outputReports
* provenance : {'md5sum': 'f6709f4c73ea023053e3fdd9fccbf26b', 'version': '0+untagged.2628.g289cee2.dirty', 'software': 'mriqc', 'webapi_url': 'https://mriqc.nimh.nih.gov/api/v1', 'webapi_port': None, 'settings': {'testing': False}, 'warnings': {'small_air_mask': False, 'large_rot_frame': False}}
* rec_id : <undefined>
* root : {'summary_csf_mean': 160.07443237304688, 'summary_csf_stdv': 77.0881576538086, 'summary_csf_median': 154.7310791015625, 'summary_csf_mad': 77.04991157425815, 'summary_csf_p95': 298.0826416015625, 'summary_csf_p05': 40.92225646972656, 'summary_csf_k': -0.02692215661326136, 'summary_csf_n': 6701.0, 'summary_gm_mean': 646.5322265625, 'summary_gm_stdv': 45.28156661987305, 'summary_gm_median': 646.431884765625, 'summary_gm_mad': 49.40153840609348, 'summary_gm_p95': 719.0096649169922, 'summary_gm_p05': 573.9876983642578, 'summary_gm_k': -0.3710872673977037, 'summary_gm_n': 61002.0, 'summary_wm_mean': 1009.0335083007812, 'summary_wm_stdv': 89.6391830444336, 'summary_wm_median': 1000.0402221679688, 'summary_wm_mad': 95.3646051875058, 'summary_wm_p95': 1168.7696533203125, 'summary_wm_p05': 880.848876953125, 'summary_wm_k': -0.1618253438955204, 'summary_wm_n': 127551.0, 'summary_bg_mean': 32.51543045043945, 'summary_bg_stdv': 67.88570404052734, 'summary_bg_median': 20.438499450683594, 'summary_bg_mad': 11.754944858030662, 'summary_bg_p95': 73.21625862121581, 'summary_bg_p05': 6.532280969619752, 'summary_bg_k': 121.25339907502631, 'summary_bg_n': 690932.0, 'snr_csf': 2.0070467112906507, 'snr_wm': 11.15624069784611, 'snr_gm': 14.275711609587335, 'snr_total': 9.146333006241365, 'snrd_csf': 8.623601376539755, 'snrd_wm': 55.73507459882849, 'snrd_gm': 36.027480217112625, 'snrd_total': 33.46205206416029, 'cnr': 2.9171006309128025, 'fber': 600.0811157226562, 'efc': 0.7152571509595217, 'wm2max': 0.6270423168185647, 'qi_1': 0.00011091593929955452, 'cjv': 0.4093968616720737, 'fwhm_x': 5.98956, 'fwhm_y': 7.19652, 'fwhm_z': 5.49306, 'fwhm_avg': 6.22638, 'icvs_csf': 0.1470790702932391, 'icvs_gm': 0.46728560816356113, 'icvs_wm': 0.38563532154319974, 'rpve_csf': 15.348087429230825, 'rpve_gm': 5.015182490164974, 'rpve_wm': 6.161822194315344, 'size_x': 138, 'size_y': 195, 'size_z': 128, 'spacing_x': 0.5, 'spacing_y': 0.5, 'spacing_z': 0.5, 'inu_range': 0.34940123558044434, 'inu_med': 1.15684175491333, 'tpm_overlap_csf': 0.10775530338287354, 'tpm_overlap_gm': 0.4644337296485901, 'tpm_overlap_wm': 0.46268269419670105, 'qi_2': 0.0008084858429067759, 'bids_meta': {'subject_id': '001', 'modality': 'T1w', 'AcquisitionMatrixPE': 128, 'AcquisitionNumber': 1, 'AcquisitionTime': '08:31:11.347500', 'BaseResolution': 128, 'ConversionSoftware': 'dcm2niix', 'ConversionSoftwareVersion': 'v1.0.20171215 GCC4.8.4', 'DeviceSerialNumber': '35302', 'DwellTime': 3e-05, 'EchoTime': 0.00338, 'FlipAngle': 15, 'ImageOrientationPatientDICOM': [1, 0, 0, 0, 0, -1], 'ImageType': ['ORIGINAL', 'PRIMARY', 'M', 'ND', 'NORM'], 'InPlanePhaseEncodingDirectionDICOM': 'ROW', 'InstitutionAddress': 'ZHONG_SHAN_BEI_3663_SHANGHAI_f87c9c_District_CN_200062', 'InstitutionName': 'East_China_Normal_University', 'InstitutionalDepartmentName': 'Department', 'InversionTime': 0.9, 'MRAcquisitionType': '3D', 'MagneticFieldStrength': 3, 'Manufacturer': 'Siemens', 'ManufacturersModelName': 'TrioTim', 'Modality': 'MR', 'PartialFourier': 1, 'PatientPosition': 'HFS', 'PercentPhaseFOV': 100, 'PhaseEncodingSteps': 128, 'PhaseResolution': 1, 'PixelBandwidth': 130, 'ProcedureStepDescription': 'zhangmiao_20150320_ACC', 'ProtocolName': 't1_mpr_cor_p2_serface_coil', 'PulseSequenceDetails': '%SiemensSeq%_tfl', 'ReceiveCoilName': 'Loop_11', 'ReconMatrixPE': 128, 'RepetitionTime': 2.2, 'SAR': 0.215444, 'ScanOptions': 'IR', 'ScanningSequence': 'GR_IR', 'SequenceName': 'tfl3d1', 'SequenceVariant': 'SP_MP', 'SeriesDescription': 't1_mpr_cor_p2_serface_coil', 'SeriesNumber': 8, 'ShimSetting': [5896, -5442, 1687, 162, -213, -6, -62, 146], 'SliceThickness': 1, 'SoftwareVersions': 'syngo_MR_B17', 'StationName': 'MRC35302', 'TxRefAmp': 353.861, 'dataset': '<unset>'}, 'provenance': {'md5sum': 'f6709f4c73ea023053e3fdd9fccbf26b', 'version': '0+untagged.2628.g289cee2.dirty', 'software': 'mriqc', 'webapi_url': 'https://mriqc.nimh.nih.gov/api/v1', 'webapi_port': None, 'settings': {'testing': False}, 'warnings': {'small_air_mask': False, 'large_rot_frame': False}}}
* run_id : <undefined>
* session_id : <undefined>
* subject_id : 001
* task_id : <undefined>


Execution Outputs
-----------------


* out_file : /home/kilimanjaro2/Research/monkeyStuff/outputReports/sub-001/anat/sub-001_T1w.json


Runtime info
------------


* duration : 0.001225
* hostname : kilimanjaro2-B250M-DS3H
* prev_wd : /home/kilimanjaro2/Research/monkeyStuff/mriqc
* working_dir : /home/kilimanjaro2/Research/monkeyStuff/mriqc/work/mriqc_wf/anatMRIQC/ComputeIQMs/_in_file_..home..kilimanjaro2..Research..monkeyStuff..bidsData..sub-001..anat..sub-001_T1w.nii.gz/datasink


Environment
~~~~~~~~~~~


* BASH_ENV : /usr/share/modules/init/bash
* CLUTTER_IM_MODULE : xim
* COLORTERM : truecolor
* CONDA_DEFAULT_ENV : mriqc36
* CONDA_EXE : /home/kilimanjaro2/anaconda3/bin/conda
* CONDA_PREFIX : /home/kilimanjaro2/.conda/envs/mriqc36
* CONDA_PREFIX_1 : /home/kilimanjaro2/anaconda3
* CONDA_PROMPT_MODIFIER : (mriqc36) 
* CONDA_PYTHON_EXE : /home/kilimanjaro2/anaconda3/bin/python
* CONDA_SHLVL : 2
* DBUS_SESSION_BUS_ADDRESS : unix:path=/run/user/1000/bus
* DEFAULTS_PATH : /usr/share/gconf/ubuntu.default.path
* DESKTOP_SESSION : ubuntu
* DISPLAY : :1
* ENV : /usr/share/modules/init/profile.sh
* FSLDIR : /usr/local/fsl
* FSLGECUDAQ : cuda.q
* FSLLOCKDIR : 
* FSLMACHINELIST : 
* FSLMULTIFILEQUIT : TRUE
* FSLOUTPUTTYPE : NIFTI_GZ
* FSLREMOTECALL : 
* FSLTCLSH : /usr/local/fsl/bin/fsltclsh
* FSLWISH : /usr/local/fsl/bin/fslwish
* GDMSESSION : ubuntu
* GJS_DEBUG_OUTPUT : stderr
* GJS_DEBUG_TOPICS : JS ERROR;JS LOG
* GNOME_DESKTOP_SESSION_ID : this-is-deprecated
* GNOME_SHELL_SESSION_MODE : ubuntu
* GNOME_TERMINAL_SCREEN : /org/gnome/Terminal/screen/1da9f0a3_4685_4755_829e_081abe61c181
* GNOME_TERMINAL_SERVICE : :1.109
* GPG_AGENT_INFO : /run/user/1000/gnupg/S.gpg-agent:0:1
* GTK_IM_MODULE : ibus
* GTK_MODULES : gail:atk-bridge
* HOME : /home/kilimanjaro2
* IM_CONFIG_PHASE : 2
* KMP_DUPLICATE_LIB_OK : True
* KMP_INIT_AT_FORK : FALSE
* LANG : en_IN
* LESSCLOSE : /usr/bin/lesspipe %s %s
* LESSOPEN : | /usr/bin/lesspipe %s
* LOGNAME : kilimanjaro2
* LS_COLORS : rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
* MANDATORY_PATH : /usr/share/gconf/ubuntu.mandatory.path
* OLDPWD : /home/kilimanjaro2/Research/monkeyStuff/mriqc/mriqc
* PATH : /usr/local/fsl/bin:/home/kilimanjaro2/.conda/envs/mriqc36/bin:/home/kilimanjaro2/anaconda3/condabin:/home/kilimanjaro2/Research/mrtrix3/bin:/home/kilimanjaro2/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/kilimanjaro2/abin
* PWD : /home/kilimanjaro2/Research/monkeyStuff/mriqc
* QT4_IM_MODULE : xim
* QT_ACCESSIBILITY : 1
* QT_IM_MODULE : ibus
* R_LIBS : /home/kilimanjaro2/R
* SESSION_MANAGER : local/kilimanjaro2-B250M-DS3H:@/tmp/.ICE-unix/4298,unix/kilimanjaro2-B250M-DS3H:/tmp/.ICE-unix/4298
* SHELL : /bin/bash
* SHLVL : 1
* SSH_AGENT_PID : 4440
* SSH_AUTH_SOCK : /run/user/1000/keyring/ssh
* TERM : xterm-256color
* TEXTDOMAIN : gdm
* TEXTDOMAINDIR : /usr/share/locale/
* USER : kilimanjaro2
* USERNAME : kilimanjaro2
* VTE_VERSION : 5202
* WINDOWPATH : 2
* XAUTHORITY : /run/user/1000/gdm/Xauthority
* XDG_CONFIG_DIRS : /etc/xdg/xdg-ubuntu:/etc/xdg
* XDG_CURRENT_DESKTOP : ubuntu:GNOME
* XDG_DATA_DIRS : /usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop
* XDG_MENU_PREFIX : gnome-
* XDG_RUNTIME_DIR : /run/user/1000
* XDG_SEAT : seat0
* XDG_SESSION_DESKTOP : ubuntu
* XDG_SESSION_ID : 3
* XDG_SESSION_TYPE : x11
* XDG_VTNR : 2
* XMODIFIERS : @im=ibus
* _ : ./mriqc.sh
* _CE_CONDA : 
* _CE_M : 

