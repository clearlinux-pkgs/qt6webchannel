#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
Name     : qt6webchannel
Version  : 6.8.0
Release  : 21
URL      : https://download.qt.io/official_releases/qt/6.8/6.8.0/submodules/qtwebchannel-everywhere-src-6.8.0.zip
Source0  : https://download.qt.io/official_releases/qt/6.8/6.8.0/submodules/qtwebchannel-everywhere-src-6.8.0.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qt6webchannel-lib = %{version}-%{release}
Requires: qt6webchannel-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is a small NodeJS implementation on how to connect to a QWebChannel.
This example implements a small chat client using the command line. It connects
to the server provided by the other example 'examples/standalone/standalone'. Of
course the port the server listens on must be known.

%package dev
Summary: dev components for the qt6webchannel package.
Group: Development
Requires: qt6webchannel-lib = %{version}-%{release}
Provides: qt6webchannel-devel = %{version}-%{release}
Requires: qt6webchannel = %{version}-%{release}

%description dev
dev components for the qt6webchannel package.


%package lib
Summary: lib components for the qt6webchannel package.
Group: Libraries
Requires: qt6webchannel-license = %{version}-%{release}

%description lib
lib components for the qt6webchannel package.


%package license
Summary: license components for the qt6webchannel package.
Group: Default

%description license
license components for the qt6webchannel package.


%prep
%setup -q -n qtwebchannel-everywhere-src-6.8.0
cd %{_builddir}/qtwebchannel-everywhere-src-6.8.0
pushd ..
cp -a qtwebchannel-everywhere-src-6.8.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732606698
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
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

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
export SOURCE_DATE_EPOCH=1732606698
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6webchannel
cp %{_builddir}/qtwebchannel-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6webchannel/79453f55fa8ee32d7b95581473edcbfd043e088f || :
cp %{_builddir}/qtwebchannel-everywhere-src-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/qt6webchannel/dc8f2e570bf431427dbc3bab9d4d551b53a60208 || :
cp %{_builddir}/qtwebchannel-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6webchannel/7713a1753ce88f2c7e6b054ecc8e4c786df76300 || :
cp %{_builddir}/qtwebchannel-everywhere-src-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6webchannel/c70af14df11e3908dfc10397b1ba4b1f346661f3 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QtWebChannel/6.8.0/QtWebChannel/private/qmetaobjectpublisher_p.h
/usr/include/QtWebChannel/6.8.0/QtWebChannel/private/qwebchannel_p.h
/usr/include/QtWebChannel/6.8.0/QtWebChannel/private/signalhandler_p.h
/usr/include/QtWebChannel/QWebChannel
/usr/include/QtWebChannel/QWebChannelAbstractTransport
/usr/include/QtWebChannel/QtWebChannel
/usr/include/QtWebChannel/QtWebChannelDepends
/usr/include/QtWebChannel/QtWebChannelVersion
/usr/include/QtWebChannel/qtwebchannelexports.h
/usr/include/QtWebChannel/qtwebchannelversion.h
/usr/include/QtWebChannel/qwebchannel.h
/usr/include/QtWebChannel/qwebchannelabstracttransport.h
/usr/include/QtWebChannel/qwebchannelglobal.h
/usr/include/QtWebChannelQuick/6.8.0/QtWebChannelQuick/private/qqmlwebchannelattached_p.h
/usr/include/QtWebChannelQuick/QQmlWebChannel
/usr/include/QtWebChannelQuick/QtWebChannelQuick
/usr/include/QtWebChannelQuick/QtWebChannelQuickDepends
/usr/include/QtWebChannelQuick/QtWebChannelQuickVersion
/usr/include/QtWebChannelQuick/qqmlwebchannel.h
/usr/include/QtWebChannelQuick/qtwebchannelquickexports.h
/usr/include/QtWebChannelQuick/qtwebchannelquickversion.h
/usr/include/QtWebChannelQuick/qwebchannelquickglobal.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtWebChannelTestsConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6WebChannelQuickpluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6WebChannelQuickpluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6WebChannelQuickpluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6WebChannelQuickpluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6WebChannelQuickpluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6WebChannelQuickpluginTargets.cmake
/usr/lib64/cmake/Qt6WebChannel/Qt6WebChannelAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6WebChannel/Qt6WebChannelConfig.cmake
/usr/lib64/cmake/Qt6WebChannel/Qt6WebChannelConfigVersion.cmake
/usr/lib64/cmake/Qt6WebChannel/Qt6WebChannelConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6WebChannel/Qt6WebChannelDependencies.cmake
/usr/lib64/cmake/Qt6WebChannel/Qt6WebChannelTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6WebChannel/Qt6WebChannelTargets.cmake
/usr/lib64/cmake/Qt6WebChannel/Qt6WebChannelVersionlessAliasTargets.cmake
/usr/lib64/cmake/Qt6WebChannel/Qt6WebChannelVersionlessTargets.cmake
/usr/lib64/cmake/Qt6WebChannelQuick/Qt6WebChannelQuickAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6WebChannelQuick/Qt6WebChannelQuickConfig.cmake
/usr/lib64/cmake/Qt6WebChannelQuick/Qt6WebChannelQuickConfigVersion.cmake
/usr/lib64/cmake/Qt6WebChannelQuick/Qt6WebChannelQuickConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6WebChannelQuick/Qt6WebChannelQuickDependencies.cmake
/usr/lib64/cmake/Qt6WebChannelQuick/Qt6WebChannelQuickTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6WebChannelQuick/Qt6WebChannelQuickTargets.cmake
/usr/lib64/cmake/Qt6WebChannelQuick/Qt6WebChannelQuickVersionlessAliasTargets.cmake
/usr/lib64/cmake/Qt6WebChannelQuick/Qt6WebChannelQuickVersionlessTargets.cmake
/usr/lib64/libQt6WebChannel.prl
/usr/lib64/libQt6WebChannel.so
/usr/lib64/libQt6WebChannelQuick.prl
/usr/lib64/libQt6WebChannelQuick.so
/usr/lib64/pkgconfig/Qt6WebChannel.pc
/usr/lib64/pkgconfig/Qt6WebChannelQuick.pc
/usr/lib64/qt6/mkspecs/modules/qt_lib_webchannel.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_webchannel_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_webchannelquick.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_webchannelquick_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6WebChannel.so.6.8.0
/V3/usr/lib64/libQt6WebChannelQuick.so.6.8.0
/V3/usr/lib64/qt6/qml/QtWebChannel/libwebchannelquickplugin.so
/usr/lib64/libQt6WebChannel.so.6
/usr/lib64/libQt6WebChannel.so.6.8.0
/usr/lib64/libQt6WebChannelQuick.so.6
/usr/lib64/libQt6WebChannelQuick.so.6.8.0
/usr/lib64/qt6/metatypes/qt6webchannel_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6webchannelquick_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/WebChannel.json
/usr/lib64/qt6/modules/WebChannelQuick.json
/usr/lib64/qt6/qml/QtWebChannel/libwebchannelquickplugin.so
/usr/lib64/qt6/qml/QtWebChannel/plugins.qmltypes
/usr/lib64/qt6/qml/QtWebChannel/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6webchannel/7713a1753ce88f2c7e6b054ecc8e4c786df76300
/usr/share/package-licenses/qt6webchannel/79453f55fa8ee32d7b95581473edcbfd043e088f
/usr/share/package-licenses/qt6webchannel/c70af14df11e3908dfc10397b1ba4b1f346661f3
/usr/share/package-licenses/qt6webchannel/dc8f2e570bf431427dbc3bab9d4d551b53a60208
