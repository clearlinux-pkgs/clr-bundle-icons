#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-bundle-icons
Version  : 7
Release  : 5
URL      : http://localhost/cgit/projects/clr-bundle-icons/snapshot/clr-bundle-icons-7.tar.gz
Source0  : http://localhost/cgit/projects/clr-bundle-icons/snapshot/clr-bundle-icons-7.tar.gz
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
%setup -q -n clr-bundle-icons-7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547821732
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1547821732
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/clear/bundle-icons/R-basic.svg
/usr/share/clear/bundle-icons/R-extras.svg
/usr/share/clear/bundle-icons/atom.svg
/usr/share/clear/bundle-icons/bundle.svg
/usr/share/clear/bundle-icons/cloud-control.svg
/usr/share/clear/bundle-icons/desktop-autostart.svg
/usr/share/clear/bundle-icons/desktop.svg
/usr/share/clear/bundle-icons/dev-utils.svg
/usr/share/clear/bundle-icons/editors.svg
/usr/share/clear/bundle-icons/emacs.svg
/usr/share/clear/bundle-icons/firefox.svg
/usr/share/clear/bundle-icons/go-basic.svg
/usr/share/clear/bundle-icons/gvim.png
/usr/share/clear/bundle-icons/java-basic.svg
/usr/share/clear/bundle-icons/machine-learning-basic.svg
/usr/share/clear/bundle-icons/machine-learning-tensorflow.svg
/usr/share/clear/bundle-icons/network-basic.svg
/usr/share/clear/bundle-icons/octave.svg
/usr/share/clear/bundle-icons/python-basic.svg
/usr/share/clear/bundle-icons/python-extras.svg
/usr/share/clear/bundle-icons/thunderbird.svg
