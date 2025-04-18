#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v23
# autospec commit: 936534a
#
Name     : nextcloud-desktop
Version  : 3.16.2
Release  : 7
URL      : https://github.com/nextcloud/desktop/archive/v3.16.2/desktop-3.16.2.tar.gz
Source0  : https://github.com/nextcloud/desktop/archive/v3.16.2/desktop-3.16.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC-BY-3.0 GPL-2.0 LGPL-2.1 MIT
Requires: nextcloud-desktop-bin = %{version}-%{release}
Requires: nextcloud-desktop-data = %{version}-%{release}
Requires: nextcloud-desktop-lib = %{version}-%{release}
Requires: nextcloud-desktop-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cups-dev
BuildRequires : doxygen
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : karchive-dev
BuildRequires : kguiaddons-dev
BuildRequires : kio-dev
BuildRequires : librsvg-bin
BuildRequires : mesa-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(cloudproviders)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libp11)
BuildRequires : pkgconfig(smbclient)
BuildRequires : pypi-sphinx
BuildRequires : qt5compat-dev
BuildRequires : qt6base-dev
BuildRequires : qt6svg-dev
BuildRequires : qt6webengine-dev
BuildRequires : qt6websockets-dev
BuildRequires : qtbase-dev
BuildRequires : qtkeychain-dev
BuildRequires : shared-mime-info
BuildRequires : texlive
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Remove-QUIET-keyword-from-find_package-calls.patch

%description
- Recompile and install recent enough version of dolphin and kio (git from oct 2015)

%package bin
Summary: bin components for the nextcloud-desktop package.
Group: Binaries
Requires: nextcloud-desktop-data = %{version}-%{release}
Requires: nextcloud-desktop-license = %{version}-%{release}

%description bin
bin components for the nextcloud-desktop package.


%package data
Summary: data components for the nextcloud-desktop package.
Group: Data

%description data
data components for the nextcloud-desktop package.


%package dev
Summary: dev components for the nextcloud-desktop package.
Group: Development
Requires: nextcloud-desktop-lib = %{version}-%{release}
Requires: nextcloud-desktop-bin = %{version}-%{release}
Requires: nextcloud-desktop-data = %{version}-%{release}
Provides: nextcloud-desktop-devel = %{version}-%{release}
Requires: nextcloud-desktop = %{version}-%{release}

%description dev
dev components for the nextcloud-desktop package.


%package lib
Summary: lib components for the nextcloud-desktop package.
Group: Libraries
Requires: nextcloud-desktop-data = %{version}-%{release}
Requires: nextcloud-desktop-license = %{version}-%{release}

%description lib
lib components for the nextcloud-desktop package.


%package license
Summary: license components for the nextcloud-desktop package.
Group: Default

%description license
license components for the nextcloud-desktop package.


%prep
%setup -q -n desktop-3.16.2
cd %{_builddir}/desktop-3.16.2
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744140151
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1744140151
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nextcloud-desktop
cp %{_builddir}/desktop-%{version}/COPYING %{buildroot}/usr/share/package-licenses/nextcloud-desktop/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/desktop-%{version}/COPYING.documentation %{buildroot}/usr/share/package-licenses/nextcloud-desktop/8f545dc92cfddaf46764df9a77825bd3db01df11 || :
cp %{_builddir}/desktop-%{version}/cmake/modules/COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/nextcloud-desktop/ff3ed70db4739b3c6747c7f624fe2bad70802987 || :
cp %{_builddir}/desktop-%{version}/cmake/modules/Copyright.txt %{buildroot}/usr/share/package-licenses/nextcloud-desktop/756076d07b8eec7d83f8e90aacf4bfdcb2105114 || :
cp %{_builddir}/desktop-%{version}/src/3rdparty/QProgressIndicator/LICENSE %{buildroot}/usr/share/package-licenses/nextcloud-desktop/7c952efc81e54865f643a20cde021177a23e7ddd || :
cp %{_builddir}/desktop-%{version}/src/csync/COPYING %{buildroot}/usr/share/package-licenses/nextcloud-desktop/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/desktop-%{version}/test/csync/COPYING %{buildroot}/usr/share/package-licenses/nextcloud-desktop/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nextcloud
/usr/bin/nextcloudcmd

%files data
%defattr(-,root,root,-)
/usr/share/applications/com.nextcloud.desktopclient.nextcloud.desktop
/usr/share/caja-python/extensions/syncstate-Nextcloud.py
/usr/share/dbus-1/services/com.nextcloudgmbh.Nextcloud.service
/usr/share/icons/hicolor/1024x1024/apps/Nextcloud.png
/usr/share/icons/hicolor/128x128/apps/Nextcloud.png
/usr/share/icons/hicolor/128x128/apps/Nextcloud_error.png
/usr/share/icons/hicolor/128x128/apps/Nextcloud_error_shared.png
/usr/share/icons/hicolor/128x128/apps/Nextcloud_ok.png
/usr/share/icons/hicolor/128x128/apps/Nextcloud_ok_shared.png
/usr/share/icons/hicolor/128x128/apps/Nextcloud_sync.png
/usr/share/icons/hicolor/128x128/apps/Nextcloud_sync_shared.png
/usr/share/icons/hicolor/128x128/apps/Nextcloud_warn.png
/usr/share/icons/hicolor/128x128/apps/Nextcloud_warn_shared.png
/usr/share/icons/hicolor/16x16/apps/Nextcloud.png
/usr/share/icons/hicolor/16x16/apps/Nextcloud_error.png
/usr/share/icons/hicolor/16x16/apps/Nextcloud_error_shared.png
/usr/share/icons/hicolor/16x16/apps/Nextcloud_ok.png
/usr/share/icons/hicolor/16x16/apps/Nextcloud_ok_shared.png
/usr/share/icons/hicolor/16x16/apps/Nextcloud_sync.png
/usr/share/icons/hicolor/16x16/apps/Nextcloud_sync_shared.png
/usr/share/icons/hicolor/16x16/apps/Nextcloud_warn.png
/usr/share/icons/hicolor/16x16/apps/Nextcloud_warn_shared.png
/usr/share/icons/hicolor/24x24/apps/Nextcloud.png
/usr/share/icons/hicolor/256x256/apps/Nextcloud.png
/usr/share/icons/hicolor/256x256/apps/Nextcloud_error.png
/usr/share/icons/hicolor/256x256/apps/Nextcloud_error_shared.png
/usr/share/icons/hicolor/256x256/apps/Nextcloud_ok.png
/usr/share/icons/hicolor/256x256/apps/Nextcloud_ok_shared.png
/usr/share/icons/hicolor/256x256/apps/Nextcloud_sync.png
/usr/share/icons/hicolor/256x256/apps/Nextcloud_sync_shared.png
/usr/share/icons/hicolor/256x256/apps/Nextcloud_warn.png
/usr/share/icons/hicolor/256x256/apps/Nextcloud_warn_shared.png
/usr/share/icons/hicolor/32x32/apps/Nextcloud.png
/usr/share/icons/hicolor/32x32/apps/Nextcloud_error.png
/usr/share/icons/hicolor/32x32/apps/Nextcloud_error_shared.png
/usr/share/icons/hicolor/32x32/apps/Nextcloud_ok.png
/usr/share/icons/hicolor/32x32/apps/Nextcloud_ok_shared.png
/usr/share/icons/hicolor/32x32/apps/Nextcloud_sync.png
/usr/share/icons/hicolor/32x32/apps/Nextcloud_sync_shared.png
/usr/share/icons/hicolor/32x32/apps/Nextcloud_warn.png
/usr/share/icons/hicolor/32x32/apps/Nextcloud_warn_shared.png
/usr/share/icons/hicolor/48x48/apps/Nextcloud.png
/usr/share/icons/hicolor/48x48/apps/Nextcloud_error.png
/usr/share/icons/hicolor/48x48/apps/Nextcloud_error_shared.png
/usr/share/icons/hicolor/48x48/apps/Nextcloud_ok.png
/usr/share/icons/hicolor/48x48/apps/Nextcloud_ok_shared.png
/usr/share/icons/hicolor/48x48/apps/Nextcloud_sync.png
/usr/share/icons/hicolor/48x48/apps/Nextcloud_sync_shared.png
/usr/share/icons/hicolor/48x48/apps/Nextcloud_warn.png
/usr/share/icons/hicolor/48x48/apps/Nextcloud_warn_shared.png
/usr/share/icons/hicolor/512x512/apps/Nextcloud.png
/usr/share/icons/hicolor/64x64/apps/Nextcloud.png
/usr/share/icons/hicolor/64x64/apps/Nextcloud_error.png
/usr/share/icons/hicolor/64x64/apps/Nextcloud_error_shared.png
/usr/share/icons/hicolor/64x64/apps/Nextcloud_ok.png
/usr/share/icons/hicolor/64x64/apps/Nextcloud_ok_shared.png
/usr/share/icons/hicolor/64x64/apps/Nextcloud_sync.png
/usr/share/icons/hicolor/64x64/apps/Nextcloud_sync_shared.png
/usr/share/icons/hicolor/64x64/apps/Nextcloud_warn.png
/usr/share/icons/hicolor/64x64/apps/Nextcloud_warn_shared.png
/usr/share/icons/hicolor/72x72/apps/Nextcloud_error.png
/usr/share/icons/hicolor/72x72/apps/Nextcloud_error_shared.png
/usr/share/icons/hicolor/72x72/apps/Nextcloud_ok.png
/usr/share/icons/hicolor/72x72/apps/Nextcloud_ok_shared.png
/usr/share/icons/hicolor/72x72/apps/Nextcloud_sync.png
/usr/share/icons/hicolor/72x72/apps/Nextcloud_sync_shared.png
/usr/share/icons/hicolor/72x72/apps/Nextcloud_warn.png
/usr/share/icons/hicolor/72x72/apps/Nextcloud_warn_shared.png
/usr/share/mime-packages/nextcloud.xml
/usr/share/nautilus-python/extensions/syncstate-Nextcloud.py
/usr/share/nemo-python/extensions/syncstate-Nextcloud.py

%files dev
%defattr(-,root,root,-)
/usr/include/nextcloudsync/creds/abstractcredentials.h
/usr/include/nextcloudsync/creds/httpcredentials.h
/usr/include/nextcloudsync/mirall/account.h
/usr/include/nextcloudsync/mirall/configfile.h
/usr/include/nextcloudsync/mirall/networkjobs.h
/usr/include/nextcloudsync/mirall/progressdispatcher.h
/usr/include/nextcloudsync/mirall/syncengine.h
/usr/include/nextcloudsync/mirall/syncfileitem.h
/usr/include/nextcloudsync/mirall/syncresult.h
/usr/lib64/libnextcloud_csync.so
/usr/lib64/libnextcloudsync.so
/usr/lib64/nextcloudsync_vfs_suffix.so
/usr/lib64/nextcloudsync_vfs_xattr.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnextcloud_csync.so.0
/usr/lib64/libnextcloud_csync.so.3.16.2
/usr/lib64/libnextcloudsync.so.0
/usr/lib64/libnextcloudsync.so.3.16.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nextcloud-desktop/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/nextcloud-desktop/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/nextcloud-desktop/756076d07b8eec7d83f8e90aacf4bfdcb2105114
/usr/share/package-licenses/nextcloud-desktop/7c952efc81e54865f643a20cde021177a23e7ddd
/usr/share/package-licenses/nextcloud-desktop/8f545dc92cfddaf46764df9a77825bd3db01df11
/usr/share/package-licenses/nextcloud-desktop/ff3ed70db4739b3c6747c7f624fe2bad70802987
