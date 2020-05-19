Node: anatMRIQC (AirMaskWorkflow (RotationMask (anatomical)
===========================================================


 Hierarchy : mriqc_wf.anatMRIQC.AirMaskWorkflow.RotationMask
 Exec ID : RotationMask.a15


Original Inputs
---------------


* in_file : /home/kilimanjaro2/Research/monkeyStuff/mriqc/work/mriqc_wf/anatMRIQC/_in_file_..home..kilimanjaro2..Research..monkeyStuff..bidsData..sub-016..anat..sub-016_T1w.nii.gz/conform/sub-016_T1w_conformed.nii.gz


Execution Inputs
----------------


* in_file : /home/kilimanjaro2/Research/monkeyStuff/mriqc/work/mriqc_wf/anatMRIQC/_in_file_..home..kilimanjaro2..Research..monkeyStuff..bidsData..sub-016..anat..sub-016_T1w.nii.gz/conform/sub-016_T1w_conformed.nii.gz


Execution Outputs
-----------------


* out_file : /home/kilimanjaro2/Research/monkeyStuff/mriqc/work/mriqc_wf/anatMRIQC/AirMaskWorkflow/_in_file_..home..kilimanjaro2..Research..monkeyStuff..bidsData..sub-016..anat..sub-016_T1w.nii.gz/RotationMask/sub-016_T1w_conformed_rotmask.nii.gz


Runtime info
------------


* duration : 0.417837
* hostname : kilimanjaro2-B250M-DS3H
* prev_wd : /home/kilimanjaro2/Research/monkeyStuff/mriqc
* working_dir : /home/kilimanjaro2/Research/monkeyStuff/mriqc/work/mriqc_wf/anatMRIQC/AirMaskWorkflow/_in_file_..home..kilimanjaro2..Research..monkeyStuff..bidsData..sub-016..anat..sub-016_T1w.nii.gz/RotationMask


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

