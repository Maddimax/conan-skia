[![Download](https://api.bintray.com/packages/3dlights/conan/skia%3Amaddimax/images/download.svg) ](https://bintray.com/3dlights/conan/skia%3Amaddimax/_latestVersion)

## Conan package recipe for *skia*

Skia provides 2D / 3D Vector rendering

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/3dlights/conan/skia%3Amaddimax).

It builds only the library, without any demos or tools found in skia

## Issues

If you wish to report an issue or make a request for a package, please do so here:

[Issues Tracker](https://github.com/Maddimax/conan-skia/issues)


## For Users

### Basic setup

    $ conan install skia/master@maddimax/master

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    skia/master@maddimax/master

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.

## Supported OS

Currenly this package works for and provides packages for iOS and macOS. Pull Requests for other platforms are very welcome ( see [Issues Tracker](https://github.com/Maddimax/conan-skia/issues) )


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache. This includes all necessary requirements

	# add bincrafters public-conan repository
	$ conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan
	# Add our repository
	$ conan remote add maddimax https://api.bintray.com/conan/3dlights/conan

	# iOS
    $ conan create . demo/testing -o skia:metal=True -o skia:gpu=True --profile ios_profile --build missing
    # iOS Simulator
    $ conan create . demo/testing -o skia:metal=False -o skia:gpu=True --profile ios_sim_profile --build missing
    # macOS
	$ conan create . demo/testing -o skia:metal=False -o skia:gpu=False --build missing


### Available Options

| Option        | Default | Possible Values  |
| ------------- |:--------|:----------------:|
| skia_enable_atlas_text | False | [True,False] |
| skia_enable_ccpr | True | [True,False] |
| skia_enable_discrete_gpu | True | [True,False] |
| skia_enable_flutter_defines | False | [True,False] |
| skia_enable_fontmgr_android | False | [True,False] |
| skia_enable_fontmgr_custom | False | [True,False] |
| skia_enable_fontmgr_custom_empty | False | [True,False] |
| skia_enable_fontmgr_empty | False | [True,False] |
| skia_enable_fontmgr_fuchsia | False | [True,False] |
| skia_enable_fontmgr_win | False | [True,False] |
| skia_enable_fontmgr_win_gdi | False | [True,False] |
| skia_enable_gpu | False | [True,False] |
| skia_enable_nima | False | [True,False] |
| skia_enable_nvpr | True | [True,False] |
| skia_enable_particles | True | [True,False] |
| skia_enable_pdf | True | [True,False] |
| skia_enable_skottie | True | [True,False] |
| skia_enable_skpicture | True | [True,False] |
| skia_enable_skshaper | True | [True,False] |
| skia_enable_spirv_validation | False | [True,False] |
| skia_enable_tools | False | [True,False] |
| skia_enable_vulkan_debug_layers | False | [True,False] |
| skia_generate_workarounds | False | [True,False] |
| skia_use_angle | False | [True,False] |
| skia_use_dng_sdk | True | [True,False] |
| skia_use_egl | False | [True,False] |
| skia_use_expat | True | [True,False] |
| skia_use_fixed_gamma_text | False | [True,False] |
| skia_use_fontconfig | False | [True,False] |
| skia_use_fonthost_mac | True | [True,False] |
| skia_use_freetype | False | [True,False] |
| skia_use_harfbuzz | True | [True,False] |
| skia_use_icu | True | [True,False] |
| skia_use_libheif | False | [True,False] |
| skia_use_libjpeg_turbo | True | [True,False] |
| skia_use_libpng | True | [True,False] |
| skia_use_libwebp | True | [True,False] |
| skia_use_lua | False | [True,False] |
| skia_use_metal | False | [True,False] |
| skia_use_opencl | False | [True,False] |
| skia_use_piex | True | [True,False] |
| skia_use_sfntly | True | [True,False] |
| skia_use_system_expat | True | [True,False] |
| skia_use_system_harfbuzz | True | [True,False] |
| skia_use_system_icu | True | [True,False] |
| skia_use_system_libjpeg_turbo | True | [True,False] |
| skia_use_system_libpng | False | [True,False] |
| skia_use_system_libwebp | False | [True,False] |
| skia_use_system_zlib | False | [True,False] |
| skia_use_vulkan | False | [True,False] |
| skia_use_wuffs | False | [True,False] |
| skia_use_x11 | False | [True,False] |
| skia_use_xps | True | [True,False] |
| skia_use_zlib | True | [True,False] |
| is_official_build | True | [True,False] |

> Note: This package tries to verify that gn actually accepted the configuration you set, and might raise an exception if it does not.

Skia has a bunch more options available, Pull requests adding those are very welcome.

## Updating skia

To update to a new version of skia update the submodule in the skia subfolder. Skia changes a lot so expect problems. 


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package skia.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](LICENSE)