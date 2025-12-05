pkgname = "cli11"
pkgver = "2.6.1" 
pkgrel = 0
build_style = "cmake"

configure_args = [
    "-DCLI11_BUILD_Docs=OFF",
    "-DCLI11_BUILD_EXAMPLES=OFF", 
    "-DCLI11_BUILD_TESTS=OFF"
]

hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = []

pkgdesc = "Command line parser for C++11"
license = "BSD-3-Clause"
url = "https://github.com/CLIUtils/CLI11"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "377691f3fac2b340f12a2f79f523c780564578ba3d6eaf5238e9f35895d5ba95"

def post_install(self):
    self.install_license("LICENSE")
