Name:		obs-gstreamer
Version:	0.4.0
Release:	4
License:	GPLv2.0
Group:		Video
Summary:	GStreamer OBS Studio plugin
Url:		https://github.com/fzwoch/obs-gstreamer/
Source0:	https://github.com/fzwoch/obs-gstreamer/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

# This patch revert commit https://github.com/fzwoch/obs-gstreamer/commit/4ca74407b0e056df5d8d57526bf41dfcb100f333
# Reverted due installation plugins just inside /usr/lib64/ and not to /usr/lib64/obs-plugins/ and that cause issues with detecting it by obs.
#Patch0:   revert-install-dir-changes.patch

BuildRequires:	meson
BuildRequires:  pkgconfig(libobs)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)

Requires: obs-studio
Requires: vulkan-loader
Requires: gstreamer1.0-vaapi
Requires: gstreamer1.0-plugins-base
Requires: gstreamer1.0-plugins-good
Requires: gstreamer1.0-plugins-bad
Requires: gstreamer1.0-plugins-ugly

%description
1. An OBS Studio source plugin to feed GStreamer launch pipelines into OBS Studio.
This plugin has interesting use cases but may be difficult to understand and is clunky use if you are not familiar with GStreamer.

2. An OBS Studio encoder plugin to use GStreamer encoder elements into OBS Studio.
This may be interesting for people trying to run OBS Studio to different platforms like the RaspberryPi or NVIDIA Tegra.

3. An OBS Studio video filter plugin to use GStreamer pipelines as video filters in OBS Studio.
This may be handy to quickly get some simple filters in but also complex pipelines are possible as long as no rate or dimension changes are done.

4. An OBS Studio audio filter plugin to use GStreamer pipelines as audio filters in OBS Studio.
This may be handy to quickly get some simple filters in but also complex pipelines are possible as long as no rate or dimension changes are done.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%meson --libdir=%{_libdir}/obs-plugins

%meson_build

%install
%meson_install

%files
%{_libdir}/obs-plugins/obs-gstreamer.so
