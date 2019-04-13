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

Currenly this package works for and provides packages for iOS and macOS. Pull Requests for other platforms are very welcome. 

## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache. This includes all necessary requirements

	# iOS
    $ conan create . demo/testing -o skia:metal=True -o skia:gpu=True --profile ios_profile
    # iOS Simulator
    $ conan create . demo/testing -o skia:metal=False -o skia:gpu=True --profile ios_sim_profile
    # macOS
	$ conan create . demo/testing -o skia:metal=False -o skia:gpu=False


### Available Options

| Option        | Default | Possible Values  |
| ------------- |:--------|:----------------:|
| metal         | False   |  [True, False]   |
| gpu           | False   |  [True, False]   |

skia has many more options available, Pull requests that add new feature options are welcome.

## Updating skia

To update to a new version of skia update the submodule in the skia subfolder. Skia changes a lot so expect problems. 


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package skia.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](LICENSE)