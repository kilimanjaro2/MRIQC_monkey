Node: anatMRIQC (ComputeIQMs (smoothness (afni)
===============================================


 Hierarchy : mriqc_wf.anatMRIQC.ComputeIQMs.smoothness
 Exec ID : smoothness.a0


Original Inputs
---------------


* acf : False
* args : -ShowMeClassicFWHM
* arith : <undefined>
* automask : False
* combine : True
* compat : <undefined>
* demed : <undefined>
* detrend : True
* environ : {}
* geom : <undefined>
* in_file : /home/kilimanjaro2/Research/monkeyStuff/mriqc/work/mriqc_wf/anatMRIQC/_in_file_..home..kilimanjaro2..Research..monkeyStuff..bidsData..sub-001..anat..sub-001_T1w.nii.gz/conform/sub-001_T1w_conformed.nii.gz
* mask : /home/kilimanjaro2/Research/monkeyStuff/secondN4/sub-001/out_mask.nii.gz
* out_detrend : <undefined>
* out_file : <undefined>
* out_subbricks : <undefined>
* unif : <undefined>


Execution Inputs
----------------


* acf : False
* args : -ShowMeClassicFWHM
* arith : <undefined>
* automask : False
* combine : True
* compat : <undefined>
* demed : <undefined>
* detrend : True
* environ : {}
* geom : <undefined>
* in_file : /home/kilimanjaro2/Research/monkeyStuff/mriqc/work/mriqc_wf/anatMRIQC/_in_file_..home..kilimanjaro2..Research..monkeyStuff..bidsData..sub-001..anat..sub-001_T1w.nii.gz/conform/sub-001_T1w_conformed.nii.gz
* mask : /home/kilimanjaro2/Research/monkeyStuff/secondN4/sub-001/out_mask.nii.gz
* out_detrend : <undefined>
* out_file : <undefined>
* out_subbricks : <undefined>
* unif : <undefined>


Execution Outputs
-----------------


* acf_param : <undefined>
* fwhm : (2.99478, 3.59826, 2.74653, 3.09324)
* out_acf : <undefined>
* out_detrend : <undefined>
* out_file : <undefined>
* out_subbricks : <undefined>


Runtime info
------------


* cmdline : 3dFWHMx -ShowMeClassicFWHM -combine -detrend -input /home/kilimanjaro2/Research/monkeyStuff/mriqc/work/mriqc_wf/anatMRIQC/_in_file_..home..kilimanjaro2..Research..monkeyStuff..bidsData..sub-001..anat..sub-001_T1w.nii.gz/conform/sub-001_T1w_conformed.nii.gz -mask /home/kilimanjaro2/Research/monkeyStuff/secondN4/sub-001/out_mask.nii.gz -detprefix sub-001_T1w_conformed_detrend -out sub-001_T1w_conformed_subbricks.out > sub-001_T1w_conformed_fwhmx.out
* duration : 4.214579
* hostname : kilimanjaro2-B250M-DS3H
* prev_wd : /home/kilimanjaro2/Research/monkeyStuff/mriqc
* working_dir : /home/kilimanjaro2/Research/monkeyStuff/mriqc/work/mriqc_wf/anatMRIQC/ComputeIQMs/_in_file_..home..kilimanjaro2..Research..monkeyStuff..bidsData..sub-001..anat..sub-001_T1w.nii.gz/smoothness


Terminal output
~~~~~~~~~~~~~~~





Terminal - standard output
~~~~~~~~~~~~~~~~~~~~~~~~~~





Terminal - standard error
~~~~~~~~~~~~~~~~~~~~~~~~~


 +
 +
  
 3
 d
 F
 W
 H
 M
 x
 :
  
 A
 F
 N
 I
  
 v
 e
 r
 s
 i
 o
 n
 =
 A
 F
 N
 I
 _
 2
 0
 .
 1
 .
 0
 1
  
 (
 A
 p
 r
  
 1
 4
  
 2
 0
 2
 0
 )
  
 [
 6
 4
 -
 b
 i
 t
 ]
 

 +
 +
  
 A
 u
 t
 h
 o
 r
 e
 d
  
 b
 y
 :
  
 T
 h
 e
  
 B
 o
 b
 

 
 [
 7
 m
 *
 +
  
 W
 A
 R
 N
 I
 N
 G
 :
 
 [
 0
 m
  
 U
 s
 i
 n
 g
  
 t
 h
 e
  
 '
 C
 l
 a
 s
 s
 i
 c
 '
  
 G
 a
 u
 s
 s
 i
 a
 n
  
 F
 W
 H
 M
  
 i
 s
  
 n
 o
 t
  
 r
 e
 c
 o
 m
 m
 e
 n
 d
 e
 d
  
 :
 (
 

  
 +
  
  
 T
 h
 e
  
 '
 -
 a
 c
 f
 '
  
 m
 e
 t
 h
 o
 d
  
 g
 i
 v
 e
 s
  
 a
  
 F
 W
 H
 M
  
 e
 s
 t
 i
 m
 a
 t
 e
  
 w
 h
 i
 c
 h
  
 i
 s
  
 m
 o
 r
 e
  
 r
 o
 b
 u
 s
 t
 ;
 

  
 +
  
  
 h
 o
 w
 e
 v
 e
 r
 ,
  
 a
 s
 s
 u
 m
 i
 n
 g
  
 t
 h
 e
  
 s
 p
 a
 t
 i
 a
 l
  
 c
 o
 r
 r
 e
 l
 a
 t
 i
 o
 n
  
 o
 f
  
 F
 M
 R
 I
  
 n
 o
 i
 s
 e
  
 h
 a
 s
 

  
 +
  
  
 a
  
 G
 a
 u
 s
 s
 i
 a
 n
  
 s
 h
 a
 p
 e
  
 i
 s
  
 n
 o
 t
  
 a
  
 g
 o
 o
 d
  
 m
 o
 d
 e
 l
 .
 

 *
 *
  
 A
 F
 N
 I
  
 c
 o
 n
 v
 e
 r
 t
 s
  
 N
 I
 F
 T
 I
 _
 d
 a
 t
 a
 t
 y
 p
 e
 =
 6
 4
  
 (
 F
 L
 O
 A
 T
 6
 4
 )
  
 i
 n
  
 f
 i
 l
 e
  
 /
 h
 o
 m
 e
 /
 k
 i
 l
 i
 m
 a
 n
 j
 a
 r
 o
 2
 /
 R
 e
 s
 e
 a
 r
 c
 h
 /
 m
 o
 n
 k
 e
 y
 S
 t
 u
 f
 f
 /
 s
 e
 c
 o
 n
 d
 N
 4
 /
 s
 u
 b
 -
 0
 0
 1
 /
 o
 u
 t
 _
 m
 a
 s
 k
 .
 n
 i
 i
 .
 g
 z
  
 t
 o
  
 F
 L
 O
 A
 T
 3
 2
 

  
  
  
  
  
 W
 a
 r
 n
 i
 n
 g
 s
  
 o
 f
  
 t
 h
 i
 s
  
 t
 y
 p
 e
  
 w
 i
 l
 l
  
 b
 e
  
 m
 u
 t
 e
 d
  
 f
 o
 r
  
 t
 h
 i
 s
  
 s
 e
 s
 s
 i
 o
 n
 .
 

  
  
  
  
  
 S
 e
 t
  
 A
 F
 N
 I
 _
 N
 I
 F
 T
 I
 _
 T
 Y
 P
 E
 _
 W
 A
 R
 N
  
 t
 o
  
 Y
 E
 S
  
 t
 o
  
 s
 e
 e
  
 t
 h
 e
 m
  
 a
 l
 l
 ,
  
 N
 O
  
 t
 o
  
 s
 e
 e
  
 n
 o
 n
 e
 .
 

 +
 +
  
 N
 u
 m
 b
 e
 r
  
 o
 f
  
 v
 o
 x
 e
 l
 s
  
 i
 n
  
 m
 a
 s
 k
  
 =
  
 1
 0
 4
 7
 7
 9
 2
 

 
 [
 7
 m
 *
 +
  
 W
 A
 R
 N
 I
 N
 G
 :
 
 [
 0
 m
  
 -
 d
 e
 m
 e
 d
  
 a
 n
 d
 /
 o
 r
  
 -
 c
 o
 r
 d
 e
 r
  
 a
 n
 d
 /
 o
 r
  
 -
 u
 n
 i
 f
  
 i
 g
 n
 o
 r
 e
 d
 :
  
 o
 n
 l
 y
  
 1
  
 i
 n
 p
 u
 t
  
 s
 u
 b
 -
 b
 r
 i
 c
 k
 s
 

 +
 +
  
 s
 t
 a
 r
 t
  
 C
 l
 a
 s
 s
 i
 c
  
 F
 W
 H
 M
  
 c
 a
 l
 c
 u
 l
 a
 t
 i
 o
 n
 s
 

  
 +
  
 C
 l
 a
 s
 s
 i
 c
  
 F
 W
 H
 M
  
 d
 o
 n
 e
  
 (
 0
 .
 0
 0
  
 C
 P
 U
  
 s
  
 t
 h
 u
 s
  
 f
 a
 r
 )
 

 +
 +
  
 s
 t
 a
 r
 t
  
 A
 C
 F
  
 c
 a
 l
 c
 u
 l
 a
 t
 i
 o
 n
 s
  
 o
 u
 t
  
 t
 o
  
 r
 a
 d
 i
 u
 s
  
 =
  
 9
 .
 2
 8
  
 m
 m
 

  
 +
  
 A
 C
 F
  
 d
 o
 n
 e
  
 (
 0
 .
 0
 0
  
 C
 P
 U
  
 s
  
 t
 h
 u
 s
  
 f
 a
 r
 )
 

 +
 +
  
 A
 C
 F
  
 1
 D
  
 f
 i
 l
 e
  
 [
 r
 a
 d
 i
 u
 s
  
 A
 C
 F
  
 m
 i
 x
 e
 d
 _
 m
 o
 d
 e
 l
  
 g
 a
 u
 s
 s
 i
 a
 n
 _
 N
 E
 W
 m
 o
 d
 e
 l
 ]
  
 w
 r
 i
 t
 t
 e
 n
  
 t
 o
  
 3
 d
 F
 W
 H
 M
 x
 .
 1
 D
 

 +
 +
  
 1
 d
 p
 l
 o
 t
 :
  
 A
 F
 N
 I
  
 v
 e
 r
 s
 i
 o
 n
 =
 A
 F
 N
 I
 _
 2
 0
 .
 1
 .
 0
 1
  
 (
 A
 p
 r
  
 1
 4
  
 2
 0
 2
 0
 )
  
 [
 6
 4
 -
 b
 i
 t
 ]
 

 +
 +
  
 A
 u
 t
 h
 o
 r
 e
 d
  
 b
 y
 :
  
 R
 W
 C
  
 e
 t
  
 a
 l
 .
 

 p
 n
 m
 t
 o
 p
 n
 g
 :
  
 4
 1
  
 c
 o
 l
 o
 r
 s
  
 f
 o
 u
 n
 d
 

  
 +
  
 a
 n
 d
  
 1
 d
 p
 l
 o
 t
 -
 e
 d
  
 t
 o
  
 f
 i
 l
 e
  
 3
 d
 F
 W
 H
 M
 x
 .
 1
 D
 .
 p
 n
 g


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

