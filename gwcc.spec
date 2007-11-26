%define name	gwcc
%define version	0.9.8
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Power user workstation and networking control center
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://gwcc.sourceforge.net/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig 
BuildRequires:  ImageMagick 
BuildRequires:  xpm-devel 
BuildRequires:  gtk-devel
BuildRequires:  gnome-libs-devel

%description
GWCC allows users to execute network utilities (ping, nslookup, traceroute),
workstation commands (netstat, df, lpr), and do cool things like process grep
from a single tabbed window. Command flags are highly configurable, results
windows are saveable and printable, and there is a System Stats tab showing
you process info, current users, Apache server status, Samba status, and
more.

%prep
%setup -q
mv src/prefs.c src/prefs.c.orig
echo '#include "errno.h"' > src/prefs.c
cat src/prefs.c.orig >> src/prefs.c

%build
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="Gnome Workstation Command Center" longtitle="Network and workstation tools" section="System/Configuration/GNOME"
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/desktop.xpm $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/desktop.xpm $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/desktop.xpm $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/gnome/apps/Utilities/gnomewcc.desktop
%{_datadir}/pixmaps/%name

