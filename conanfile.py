from conans import ConanFile
import os, shutil
from conans.tools import download, unzip, replace_in_file, check_md5
from conans import CMake
from conans import tools

class BitprimMpirConan(ConanFile):
    name = "mpir"
    version = "3.0.0"
    url = "https://github.com/bitprim/bitprim-conan-mpir"
    ZIP_FOLDER_NAME = "mpir-%s" % version
    generators = "cmake"
    settings =  "os", "compiler", "arch", "build_type"
    build_policy = "missing"

    options = {"shared": [True, False],
               "disable_assembly": [True, False],
               "enable_fat": [True, False],
               "enable_cxx": [True, False],
               "disable-fft": [True, False],
               "enable-assert": [True, False]}

    default_options = "shared=False", "disable_assembly=False", "enable_fat=False", \
                      "enable_cxx=True", "disable-fft=False", "enable-assert=False"

    # requires = "m4/1.4.18@bitprim/stable"

    def source(self):
        # http://mpir.org/mpir-3.0.0.tar.bz2

        zip_name = "mpir-%s.tar.bz2" % self.version
        # download("http://gmplib.org/download/gmp/%s" % zip_name, zip_name)
        download("http://mpir.org/%s" % zip_name, zip_name)

        # check_md5(zip_name, "4c175f86e11eb32d8bf9872ca3a8e11d") #TODO
        unzip(zip_name)
        os.unlink(zip_name)

    def config(self):
        pass
        # del self.settings.compiler.libcxx

    # def generic_env_configure_vars(self, verbose=False):
    #     """Reusable in any lib with configure!!"""
    #     command = ""
    #     if self.settings.os == "Linux" or self.settings.os == "Macos":
    #         libs = 'LIBS="%s"' % " ".join(["-l%s" % lib for lib in self.deps_cpp_info.libs])
    #         ldflags = 'LDFLAGS="%s"' % " ".join(["-L%s" % lib for lib in self.deps_cpp_info.lib_paths])
    #         archflag = "-m32" if self.settings.arch == "x86" else ""
    #         cflags = 'CFLAGS="-fPIC %s %s"' % (archflag, " ".join(self.deps_cpp_info.cflags))
    #         cpp_flags = 'CPPFLAGS="-fPIC %s %s"' % (archflag, " ".join(self.deps_cpp_info.cppflags))
    #         command = "env %s %s %s %s" % (libs, ldflags, cflags, cpp_flags)
    #     elif self.settings.os == "Windows" and self.settings.compiler == "Visual Studio":
    #         cl_args = " ".join(['/I"%s"' % lib for lib in self.deps_cpp_info.include_paths])
    #         lib_paths= ";".join(['"%s"' % lib for lib in self.deps_cpp_info.lib_paths])
    #         command = "SET LIB=%s;%%LIB%% && SET CL=%s" % (lib_paths, cl_args)
    #         if verbose:
    #             command += " && SET LINK=/VERBOSE"
    #     if self.settings.os == "Windows" and self.settings.compiler == "gcc":
    #         libs = 'LIBS="%s"' % " ".join(["-l%s" % lib for lib in self.deps_cpp_info.libs])
    #         ldflags = 'LDFLAGS="%s"' % " ".join(["-L%s" % lib for lib in self.deps_cpp_info.lib_paths])
    #         archflag = "-m32" if self.settings.arch == "x86" else ""
    #         cflags = 'CFLAGS="-fPIC %s %s"' % (archflag, " ".join(self.deps_cpp_info.cflags))
    #         cpp_flags = 'CPPFLAGS="-fPIC %s %s"' % (archflag, " ".join(self.deps_cpp_info.cppflags))
    #         command = "env %s %s %s %s" % (libs, ldflags, cflags, cpp_flags)

    #     return command

    def build(self):
        self.output.warn("*** Detected OS: %s" % (self.settings.os))
        if self.settings.compiler == "Visual Studio":
            self.output.warn("*** Detected Visual Studio version: %s" % (self.settings.compiler.version))
            
        # config_options_string = ""

        # for option_name in self.options.values.fields:
        #     activated = getattr(self.options, option_name)
        #     if activated:
        #         self.output.info("Activated option! %s" % option_name)
        #         config_options_string += " --%s" % option_name.replace("_", "-")

        # self.output.warn("*** Detected OS: %s" % (self.settings.os))

        # if self.settings.os == "Macos":
        #     config_options_string += " --with-pic"

        
        # disable_assembly = "--disable-assembly" if self.settings.arch == "x86" else ""

        # configure_command = "cd %s && %s ./configure --with-pic --enable-static --enable-shared %s %s" % (self.ZIP_FOLDER_NAME, self.generic_env_configure_vars(), config_options_string, disable_assembly)
        # self.output.warn(configure_command)
        # self.run(configure_command)

        # # if self.settings.os == "Linux" or self.settings.os == "Macos":
        # if self.settings.os != "Windows":
        #     self.run("cd %s && make" % self.ZIP_FOLDER_NAME)
        # else:
        #     # self.run("dir C:\MinGw\bin\")
        #     self.run("cd %s && C:\MinGw\bin\make" % self.ZIP_FOLDER_NAME)

    # def imports(self):
    #     self.copy("m4", dst=".", src="bin")

    # def package(self):
    #     self.copy("*.h", "include", "%s" % (self.ZIP_FOLDER_NAME), keep_path=True)
    #     if self.options.shared:
    #         self.copy(pattern="*.so*", dst="lib", src=self.ZIP_FOLDER_NAME, keep_path=False)
    #         self.copy(pattern="*.dll*", dst="bin", src=self.ZIP_FOLDER_NAME, keep_path=False)
    #     else:
    #         self.copy(pattern="*.a", dst="lib", src="%s" % self.ZIP_FOLDER_NAME, keep_path=False)

    #     self.copy(pattern="*.lib", dst="lib", src="%s" % self.ZIP_FOLDER_NAME, keep_path=False)
        
    # def package_info(self):
    #     self.cpp_info.libs = ['gmp']


