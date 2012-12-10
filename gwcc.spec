%define name	gwcc
%define version	0.9.8
%define release %mkrel 6

Name: 	 	%{name}
Summary: 	Power user workstation and networking control center
Version: 	%{version}
Release: 	%{release}

Source0:		%{name}-%{version}.tar.bz2
URL:		http://gwcc.sourceforge.net/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRequires:	pkgconfig 
BuildRequires:  imagemagick 
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
%makeinstall_std

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=%{name}
Name=Gnome Workstation Command Center
Comment=Network and workstation tools
Categories=Settings;GTK;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 pixmaps/desktop.xpm $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 pixmaps/desktop.xpm $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 pixmaps/desktop.xpm $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name || touch %{name}.lang

%files -f %{name}.lang
%defattr(-,root,root)
%doc README
%{_bindir}/%name
%{_datadir}/applications/mandriva-%name.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/gnome/apps/Utilities/gnomewcc.desktop
%{_datadir}/pixmaps/%name



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.8-6mdv2011.0
+ Revision: 619321
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.9.8-5mdv2010.0
+ Revision: 429349
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.9.8-4mdv2009.0
+ Revision: 246731
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 0.9.8-2mdv2008.1
+ Revision: 131747
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import gwcc


* Mon Oct 03 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.8-2mdk
- BuildRequires fix

* Mon Oct 18 2004 Austin Acton <austin@mandrake.org> 0.9.8-1mdk
- initial package
