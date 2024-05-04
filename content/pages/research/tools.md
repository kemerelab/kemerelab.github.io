---
title: Resources
save_as: research/tools.html
url: research/tools.html
---

## Research Tools

We are developing a wide variety of tools for open source and high throughput neuroengineering. 
Many items are available at our lab repository
[http://github.com/kemerelab](http://github.com/kemerelab). Some are highlighted below.

### Software
!!! tool "GhostiPy"
    [GhostiPy](https://github.com/kemerelab/ghostipy/) 
    is a spectral (frequency-domain) analysis toolkit. At it's core, it provides an efficient 
    engine which can perform out-of-core convolutions on extremely large data sets. Other
    useful features include: 

    + Helper functions for optimal filter design
    + Wavelet spectrogram generation, including the Morse wavelet family implemented in frequency domain
    + Multi-taper spectrogram estimation (a la [Chronux](http://chronux.org/), but in Python)
    + The synchrosqueeze transform

    Get started using `pip install ghostipy`, or take a look at 
    [example notebooks](https://github.com/kemerelab/ghostipy/tree/master/examples/2021paper) in the repository.

    _We are looking for volunteers to improve our documentation!_



!!!tool "NelPy"
    [NelPy](https://github.com/nelpy/nelpy/)
    is an experimental data analysis toolkit for Python. It is designed to make it straightforward
    to combine different aspects of experimental data that have different sampling rates or time
    bases, such as animal position and local field potentials. It also facilitates defining periods
    of time during which analyses should be done ("epochs"), so, for instance, one can write

        :::python
        speed = nel.utils.ddt_asa(pos, smooth=True, sigma=1.0, norm=True)
        run_epochs = nel.utils.get_run_epochs(speed, v1=5, v2=2)

        run_times = st[run_epochs, unit_id].time
        x_pos_run, y_pos_run = pos(run_times)
        rest_times = st[~run_epochs, unit_id].time
        x_pos_rest, y_pos_rest = pos(run_times)
          

    Using these data, one can very quickly generate something like this: ![Nelpy Example](/images/research-features/tools/nelpy.png)


!!!tool "Trodes and TrodesRippleDisruption"
    We are contributors to the [Trodes](https://bitbucket.org/mkarlsso/trodes/) project by [SpikeGadgets](https://spikegadgets.com/).
    Trodes is an neural data acquisition system designed to be cross-platform, and to enable a tetrode-friendly visualization
    during experiments. It also enables C++ or Python-based plugins for real time data acquisition.

    We are maintaining a fork that enables data acquisition using OpenEphys or Intan Technologies USB-based systems.

    In addition, we are actively developing the
    [Trodes Ripple Disruption Module](https://github.com/ckemere/TrodesRippleDisruptionModule),
    which facilitates closed loop detection and perturbation of hippocampal sharp-wave ripple events. Our module also uses
    a simple RaspberryPi based Ethernet-triggered pulse generator, the
     [pi-stimserver](https://github.com/kemerelab/pi-stimserver).

### Public relations
!!!tool "RatPack"
    <img src="/images/research-features/tools/ratpack.png" alt="Ratpack" width="200" style="float: left; margin: 5px;"/>

    The [RatPack](https://github.com/kemerelab/ratpack) is an open source collection of drawings of rats and mice. 
    _We invite contributors!_

### Miniscope and Imaging-Related

!!!tool "MiniFAST"
    <img src="/images/research-features/tools/MiniFASTmouse.jpg" alt="MiniFAST on Mouse" width="200" style="float: left; margin: 5px;"/>

    We developed the [MiniFAST](https://github.com/jjuneau1/MiniFAST) 
    variant of the UCLA miniscope as part of our work towards enabling imaging of fast genetically-encoded 
    fluorescent neural activity sensors. We are happy to share more design information to facilitate external
    users.
    
    More information can also be found in our preprint: [**MiniFAST: A sensitive and fast miniaturized microscope 
    for _in vivo_ neural recording.** Jill Juneau, Guillaume Duret, Joshua P. Chu, Alexander V. Rodriguez,
    Savva Morozov, Daniel Aharoni, Jacob T. Robinson, François St-Pierre, Caleb Kemere.
    2020.](http://biorxiv.org/lookup/doi/10.1101/2020.11.03.367466)


!!!tool "Useful items for Widefield imaging"
    We developed a couple of useful things for widefield imaging which can be found in 
    [this repository](https://github.com/kemerelab/WidefieldMicroscopy). First, a simple PCB which plugs into a
    [Teensy 3.6](https://www.pjrc.com/teensy/)
    to facilitate BNC-based pulse sequences, e.g., to drive different wavelength LEDs for hemodynamic
    normalization. Second, a 3D-printed cone which mounts to an 
    [Olympus MVX 10](https://www.olympus-lifescience.com/en/microscopes/macro/mvx10/) widefield objective to block
    out external light from a small field of view.


### 3D Printed

!!!tool "Ultralight Probe Microdrive"
    The UPM is a 3D printed design that leverages a shoulder screw design inspired by the Open Ephys 
    [shuttledrive](https://github.com/open-ephys/shuttle-drive)
    and [Jadhav Lab](https://gitlab.com/JMOlson/TetDrive-Jadhav-Metal) designs, in combination
    with the [microdrive](https://github.com/buzsakilab/3d_print_designs/tree/master/Microdrives/Metal_recoverable) design 
    by Mihály Vöröslakos in the Buzsaki Lab. Total weight is ~0.7g. Designs can be found
    at [github.com/ckemere/UltralightProbeMicrodrive](https://github.com/ckemere/UltralightProbeMicrodrive)

    <img src="/images/research-features/tools/microdrive-assembly.gif" alt="Microdrive" width="640"/>

    We have also developed a cap and cover designed to integrate with a [Diagnostic Biochips](https://diagnosticbiochips.com/)
    probe. Developed for 15g singing mice, the complete cap and microdrive assembly are less than 2.5g.

### Virtual Reality

!!!tool "TreadmillIO"
    The [TreadmillIO](https://github.com/kemerelab/treadmillio) 
    project combines a USB-based data acquisition system with Python based software. We
    have used it for VR experiments in head-fixed mice as well as controlling reward for freely moving animals.

    <img src="/images/research-features/tools/treadmillio-interface-pcb.jpg" alt="Treadmill IO PCB" width="400"/>


    For visual stimuli, we use a distributed renderer, which runs on a Raspberry Pi platform 
    [PyRenderMaze](https://github.com/kemerelab/PyRenderMaze/).

    <img src="/images/research-features/tools/PyRenderMazeExample.gif" alt="PyRenderMaze Example" width="400"/>

    While TreadmillIO provides low latency virtual auditory stimuli, there is also a 
    [beta version](https://github.com/kemerelab/treadmillio_sound_server) of a distributed
    auditory stimuli generator also based on a RasperryPi, which we have used in experiments.

### Deep Brain Stimulation

!!!tool "Chronic DBS Module w/Bluetooth"
    The most recent generation of our chronic brain stimulator is the **MiniStiMo**. It's a
    coin cell battery-powered, constant current biphasic stimulator with a 5V compliance
    voltage (capable of 100 µA stimulation with a 20 kOhm electrode). Stimulation current
    and frequency can be controlled with an IOS Bluetooth app.

    There are three Github repositories:

      + [MiniStiMo PCB Design](https://github.com/ckemere/MiniStiMo-PCB)
      + [MiniStiMo Firmware](https://github.com/ckemere/MiniStiMo-Firmware)
      + [MiniStiMo App](https://github.com/ckemere/MiniStiMo-App)

    <img src="/images/research-features/tools/BuiltModule.png" alt="MiniStiMo" width="400"/>



