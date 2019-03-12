#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-bundle-icons
Version  : 10
Release  : 8
URL      : http://localhost/cgit/projects/clr-bundle-icons/snapshot/clr-bundle-icons-10.tar.gz
Source0  : http://localhost/cgit/projects/clr-bundle-icons/snapshot/clr-bundle-icons-10.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0 MIT
Requires: clr-bundle-icons-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the clr-bundle-icons package.
Group: Data

%description data
data components for the clr-bundle-icons package.


%prep
%setup -q -n clr-bundle-icons-10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552428820
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1552428820
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/clear/bundle-icons/R-basic.svg
/usr/share/clear/bundle-icons/R-extras.svg
/usr/share/clear/bundle-icons/atom.svg
/usr/share/clear/bundle-icons/baobab.png
/usr/share/clear/bundle-icons/blender.png
/usr/share/clear/bundle-icons/boinc-client.png
/usr/share/clear/bundle-icons/bundle.svg
/usr/share/clear/bundle-icons/c-basic.svg
/usr/share/clear/bundle-icons/cheese.png
/usr/share/clear/bundle-icons/cloud-control.svg
/usr/share/clear/bundle-icons/darktable.png
/usr/share/clear/bundle-icons/darktable.svg
/usr/share/clear/bundle-icons/desktop-autostart.svg
/usr/share/clear/bundle-icons/desktop.svg
/usr/share/clear/bundle-icons/dev-utils.svg
/usr/share/clear/bundle-icons/editors.svg
/usr/share/clear/bundle-icons/emacs.svg
/usr/share/clear/bundle-icons/eog.png
/usr/share/clear/bundle-icons/evince.png
/usr/share/clear/bundle-icons/file-roller.png
/usr/share/clear/bundle-icons/firefox.svg
/usr/share/clear/bundle-icons/geany.png
/usr/share/clear/bundle-icons/gedit.png
/usr/share/clear/bundle-icons/gimp.png
/usr/share/clear/bundle-icons/gimp.svg
/usr/share/clear/bundle-icons/gnome-calculator.png
/usr/share/clear/bundle-icons/gnome-characters.png
/usr/share/clear/bundle-icons/gnome-color-manager.png
/usr/share/clear/bundle-icons/gnome-disk-utility.png
/usr/share/clear/bundle-icons/gnome-logs.png
/usr/share/clear/bundle-icons/gnome-music.png
/usr/share/clear/bundle-icons/gnome-photos.png
/usr/share/clear/bundle-icons/gnome-todo.png
/usr/share/clear/bundle-icons/gnome-weather.png
/usr/share/clear/bundle-icons/go-basic.svg
/usr/share/clear/bundle-icons/gparted.png
/usr/share/clear/bundle-icons/gvim.png
/usr/share/clear/bundle-icons/inkscape.png
/usr/share/clear/bundle-icons/java-basic.svg
/usr/share/clear/bundle-icons/joe.png
/usr/share/clear/bundle-icons/machine-learning-basic.svg
/usr/share/clear/bundle-icons/machine-learning-tensorflow.svg
/usr/share/clear/bundle-icons/meld.png
/usr/share/clear/bundle-icons/nautilus.png
/usr/share/clear/bundle-icons/network-basic.svg
/usr/share/clear/bundle-icons/nodejs-basic.svg
/usr/share/clear/bundle-icons/octave.svg
/usr/share/clear/bundle-icons/perl-basic.svg
/usr/share/clear/bundle-icons/perl-extras.svg
/usr/share/clear/bundle-icons/php-basic.svg
/usr/share/clear/bundle-icons/pidgin.png
/usr/share/clear/bundle-icons/pidgin.svg
/usr/share/clear/bundle-icons/python-basic.svg
/usr/share/clear/bundle-icons/python-extras.svg
/usr/share/clear/bundle-icons/python2-basic.svg
/usr/share/clear/bundle-icons/python3-basic.svg
/usr/share/clear/bundle-icons/quassel.png
/usr/share/clear/bundle-icons/rhythmbox.png
/usr/share/clear/bundle-icons/seahorse.png
/usr/share/clear/bundle-icons/stellarium.png
/usr/share/clear/bundle-icons/synergy.png
/usr/share/clear/bundle-icons/thunderbird.svg
/usr/share/clear/bundle-icons/totem.png
/usr/share/clear/bundle-icons/v4l-utils.png
/usr/share/clear/bundle-icons/virt-manager.png
/usr/share/clear/bundle-icons/vlc.png
/usr/share/clear/bundle-icons/weechat.png
/usr/share/clear/bundle-icons/xemacs.svg
