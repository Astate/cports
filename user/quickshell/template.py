pkgname = "quickshell"
pkgver = "0.2.1"
pkgrel = 0
build_style = "cmake"

# Quickshell nécessite C++20
configure_args = ["-DCMAKE_CXX_STANDARD=20",
     "-DCRASH_REPORTER=OFF",
     "-DCMAKE_DISABLE_PRECOMPILE_HEADERS=ON",
     "-DCMAKE_BUILD_TYPE=RelWithDebInfo"
 ]

# Outils de compilation (sur l'hôte)
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "wayland-progs",
    "qt6-qtbase",
]

# Bibliothèques de développement (pour le lien)
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
    "qt6-qtbase-private-devel",
    "wayland-devel",
    "wayland-protocols",
    "linux-pam-devel",
    "pipewire-devel",
    "cli11",
    "polkit-devel",
    "jemalloc-devel",

]

# Dépendances d'exécution (Indispensables pour le lancement)
depends = [
    "qt6-qtdeclarative",
    "qt6-qtwayland",
]

pkgdesc = "QtQuick based shell for Wayland"
license = "GPL-3.0-or-later"
url = "https://git.outfoxxed.me/quickshell/quickshell"

# Source git master
source = f"{url}/archive/master.tar.gz"
# Mettre une somme factice pour le premier fetch
sha256 = "c0fbea3fb653770811298bb1f8d062703eda7158aeec569e5cfc98601d5afcab"
