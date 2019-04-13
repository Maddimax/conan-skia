from conans import ConanFile, CMake, tools, errors
import os, re
from six import StringIO  # Python 2 and 3 compatible

def find_all_headers(root):
    result = []
    entries = os.walk(root)
    for entry in entries:
        for file in entry[2]:
            if file.endswith('.h'):
                result.append(os.path.join(entry[0], file))

    return result

def fix(all_headers, src):
    f = open(src, "r")

    base = os.path.dirname(src)

    regex = r'^#include\s*"([^"]*)"'    
    result = ""

    for line in f:
        match = re.match(regex, line)
        if match:
            if not os.path.exists(os.path.join(base, match.group(1))):
                matches = [x for x in all_headers if os.path.basename(x) == os.path.basename(match.group(1))]
                if len(matches) == 1:
                    relpath = os.path.relpath(matches[0], base)
                    result += '#include "%s"\n' % relpath
                    continue
        result += line

    f.close()

    f = open(src, "w")
    f.write(result) 

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

class SkiaConan(ConanFile):
    name = "skia"
    version = "master"
    license = "<Put the package license here>"
    author = "Marcus Tillmanns <maddimax@gmail.com>"
    url = "https://github.com/Maddimax/conan-skia.git"
    description = "A 2D/3D Vector rendering engine"
    topics = ("render", "vector", "2d", "3d")
    settings = "os", "compiler", "build_type", "arch"

    skia_options = {
        "skia_enable_atlas_text" : [True, False],
        "skia_enable_ccpr" : [True, False],
        "skia_enable_discrete_gpu" : [True, False],
        "skia_enable_flutter_defines" : [True, False],
        "skia_enable_fontmgr_android" : [True, False],
        "skia_enable_fontmgr_custom" : [True, False],
        "skia_enable_fontmgr_custom_empty" : [True, False],
        "skia_enable_fontmgr_empty" : [True, False],
        "skia_enable_fontmgr_fuchsia" : [True, False],
        "skia_enable_fontmgr_win" : [True, False],
        "skia_enable_fontmgr_win_gdi" : [True, False],
        "skia_enable_gpu" : [True, False],
        "skia_enable_nima" : [True, False],
        "skia_enable_nvpr" : [True, False],
        "skia_enable_particles" : [True, False],
        "skia_enable_pdf" : [True, False],
        "skia_enable_skottie" : [True, False],
        "skia_enable_skpicture" : [True, False],
        "skia_enable_skshaper" : [True, False],
        "skia_enable_spirv_validation" : [True, False],
        "skia_enable_tools" : [True, False],
        "skia_enable_vulkan_debug_layers" : [True, False],
        "skia_generate_workarounds" : [True, False],
        "skia_use_angle" : [True, False],
        "skia_use_dng_sdk" : [True, False],
        "skia_use_egl" : [True, False],
        "skia_use_expat" : [True, False],
        "skia_use_fixed_gamma_text" : [True, False],
        "skia_use_fontconfig" : [True, False],
        "skia_use_fonthost_mac" : [True, False],
        "skia_use_freetype" : [True, False],
        "skia_use_harfbuzz" : [True, False],
        "skia_use_icu" : [True, False],
        "skia_use_libheif" : [True, False],
        "skia_use_libjpeg_turbo" : [True, False],
        "skia_use_libpng" : [True, False],
        "skia_use_libwebp" : [True, False],
        "skia_use_lua" : [True, False],
        "skia_use_metal" : [True, False],
        "skia_use_opencl" : [True, False],
        "skia_use_piex" : [True, False],
        "skia_use_sfntly" : [True, False],
        "skia_use_system_expat" : [True, False],
        "skia_use_system_harfbuzz" : [True, False],
        "skia_use_system_icu" : [True, False],
        "skia_use_system_libjpeg_turbo" : [True, False],
        "skia_use_system_libpng" : [True, False],
        "skia_use_system_libwebp" : [True, False],
        "skia_use_system_zlib" : [True, False],
        "skia_use_vulkan" : [True, False],
        "skia_use_wuffs" : [True, False],
        "skia_use_x11" : [True, False],
        "skia_use_xps" : [True, False],
        "skia_use_zlib" : [True, False],
        "is_official_build" : [True, False]
    }

    options = merge_two_dicts({ "shared": [True, False] }, skia_options)

    default_options = {
        "shared":False,
        "harfbuzz:with_icu" : True,
        # Skia options
        "skia_enable_atlas_text" : False,
        "skia_enable_ccpr" : True,
        "skia_enable_discrete_gpu" : True,
        "skia_enable_flutter_defines" : False,
        "skia_enable_fontmgr_android" : False,
        "skia_enable_fontmgr_custom" : False,
        "skia_enable_fontmgr_custom_empty" : False,
        "skia_enable_fontmgr_empty" : False,
        "skia_enable_fontmgr_fuchsia" : False,
        "skia_enable_fontmgr_win" : False,
        "skia_enable_fontmgr_win_gdi" : False,
        "skia_enable_gpu" : False,
        "skia_enable_nima" : False,
        "skia_enable_nvpr" : True,
        "skia_enable_particles" : True,
        "skia_enable_pdf" : True,
        "skia_enable_skottie" : True,
        "skia_enable_skpicture" : True,
        "skia_enable_skshaper" : True,
        "skia_enable_spirv_validation" : False,
        "skia_enable_tools" : False,
        "skia_enable_vulkan_debug_layers" : False,
        "skia_generate_workarounds" : False,
        "skia_use_angle" : False,
        "skia_use_dng_sdk" : True,
        "skia_use_egl" : False,
        "skia_use_expat" : True,
        "skia_use_fixed_gamma_text" : False,
        "skia_use_fontconfig" : False,
        "skia_use_fonthost_mac" : True,
        "skia_use_freetype" : False,
        "skia_use_harfbuzz" : True,
        "skia_use_icu" : True,
        "skia_use_libheif" : False,
        "skia_use_libjpeg_turbo" : True,
        "skia_use_libpng" : True,
        "skia_use_libwebp" : True,
        "skia_use_lua" : False,
        "skia_use_metal" : False,
        "skia_use_opencl" : False,
        "skia_use_piex" : True,
        "skia_use_sfntly" : True,
        "skia_use_system_expat" : True,
        "skia_use_system_harfbuzz" : True,
        "skia_use_system_icu" : True,
        "skia_use_system_libjpeg_turbo" : True,
        "skia_use_system_libpng" : False,
        "skia_use_system_libwebp" : False,
        "skia_use_system_zlib" : False,
        "skia_use_vulkan" : False,
        "skia_use_wuffs" : False,
        "skia_use_x11" : False,
        "skia_use_xps" : True,
        "skia_use_zlib" : True,
        "is_official_build" : True
    }

    generators = "cmake"
    build_policy = "missing"

    scm = {
        "type": "git",
        "url": "auto",
        "revision": "auto",
        "submodule" : "shallow"
    }

    revision_mode = "scm"

    def get_skia_option_value(self, option_name):
        buf = StringIO()
        self.run('bin/gn args out/conan-build --list=%s --short' % (option_name), output=buf, cwd='skia')
        output = buf.getvalue()

        pattern = r'%s = (.*)' % (option_name)
        match = re.match(pattern, output)
        if match:
            if match.group(1) == 'true':
                return True
            elif match.group(1) == 'false':
                return False

        raise errors.ConanInvalidConfiguration("Could not parse gn comfiguration options")

    def requirements(self):
        if self.options.skia_use_system_icu and self.options.skia_use_icu:
            self.requires("icu/63.1@bincrafters/stable")
        if self.options.skia_use_system_libjpeg_turbo and self.options.skia_use_libjpeg_turbo:
            self.requires("libjpeg-turbo/1.5.2@bincrafters/stable")
        if self.options.skia_use_system_harfbuzz and self.options.skia_use_harfbuzz:
            self.requires("harfbuzz/2.4.0@maddimax/stable")
        if self.options.skia_use_system_libpng and self.options.skia_use_libpng:
            self.requires("libpng/1.6.36@bincrafters/stable")

    def source(self):
        # Fix include paths ...
        self.output.info("Fixing headers:")
        all_headers = find_all_headers(os.path.join(self.source_folder, "skia"))
        for header in all_headers:
            fix(all_headers, header)
        
        if len(all_headers) == 0:
            print("Error: No header files found")
            exit(1)

        self.output.info("Fixed %i files" % (len(all_headers)))

        # Fetch dependencies
        self.run('/usr/local/bin/python skia/tools/git-sync-deps')

    def configure(self):
        if self.options.skia_use_metal:
            if not self.settings.os == "iOS" and not self.settings.os == "Macos":
                raise errors.ConanInvalidConfiguration("Metal is only supported on darwin platforms: %s" % self.settings.os) 

    def build(self):
        flags = []
        for k,v in self.deps_cpp_info.dependencies:
            self.output.info("Adding dependency: %s - %s" %(k, v.rootpath))
            flags += ['\\"-I%s/include\\"' % (v.rootpath), '\\"-I%s/include/%s\\"' % (v.rootpath, k)]

        flag_str = 'extra_cflags_cc=[%s]' % ",".join(flags)

        opts = [flag_str]

        for k,v in self.options.items():
            if k in self.skia_options:
                opts += [("%s=%s" % (k,v)).lower()]

        if self.settings.build_type == "Debug":
            opts += ["is_debug=true"]
        else:
            opts += ["is_debug=false"]

        if self.settings.os == "iOS":
            opts += ['target_os=\\"ios\\"']
            if self.settings.arch == "armv8":
                opts += ['target_cpu=\\"arm64\\"']
            else:
                opts += ['target_cpu=\\"x86_64\\"']

        if len(opts) > 0:
            opts = '"--args=%s"' % " ".join(opts)
        else:
            opts = ""

        self.output.info("gn options: %s" % (opts))

        self.run('bin/gn gen out/conan-build %s ' %(opts), cwd="skia")
        failed = False
        for k,v in self.options.items():
            if k in self.skia_options:       
                actual = self.get_skia_option_value(k)
                if not ("%s" % actual) == ("%s" % v):
                    failed = True
                    self.output.warn("Mismatch in %s: %s => %s" % ( k, v, actual ))
        if failed:
            raise errors.ConanInvalidConfiguration("Final gn configuration did not match requested config")
    
        self.run('ninja -C out/conan-build', cwd="skia")

    def package(self):
        self.copy("*.h", dst="include/skia", src="skia", keep_path=True)
        self.copy("*.dll", dst="bin", src="skia/out/conan-build",keep_path=False)
        self.copy("*.so", dst="lib", src="skia/out/conan-build",keep_path=False)
        self.copy("*.dylib", dst="lib", src="skia/out/conan-build",keep_path=False)
        self.copy("*.a", dst="lib", src="skia/out/conan-build", keep_path=False)

#        if self.settings.build_type == "Release":
#            libs = os.listdir(os.path.join(self.package_folder, "lib"))
#            self.output.info("Trying to strip: %s" %(libs))
#            for lib in libs:
#                self.run('strip -S %s' % (os.path.join(self.package_folder, "lib" ,lib)))

    def package_info(self):
        libs = os.listdir(os.path.join(self.package_folder, "lib"))
        libs = [(x[3:])[:-2] for x in libs]

        self.cpp_info.libs = libs
        if self.settings.os == "Macos":
            self.cpp_info.exelinkflags += ["-framework AppKit"]
            if self.options.skia_use_metal:
                self.cpp_info.defines += ["SK_METAL=1"]
                self.cpp_info.exelinkflags += ["-framework Metal", "-framework MetalKit", "-framework AppKit"]
