Name:           redbutton-author
Version:        20090727
Release:        3
Group:          Development/Other
License:        GPLv2+
Summary:        Redbutton author for MHEG5 content
Source:         redbutton-author-%{version}.tar.gz
URL:            http://redbutton.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	flex
BuildRequires:	bison

%description
This package provides an authoring program for MHEG5, which is used to make
user interface on TVs.
It is part of the redbutton tools suite.

%prep
%setup -q

%build
make

%install
%__rm -rf %{buildroot}
mkdir -p %buildroot%_bindir
#make install DESTDIR=%buildroot # happens "/bin" to DESTDIR
install -m 755 mhegc %buildroot%_bindir
install -m 755 mhegd %buildroot%_bindir

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/mhegc
%_bindir/mhegd



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 20090727-2mdv2011.0
+ Revision: 614704
- the mass rebuild of 2010.1 packages

* Sun Nov 29 2009 Olivier Faurax <ofaurax@mandriva.org> 20090727-1mdv2010.1
+ Revision: 471572
- Added missing .spec
- import redbutton-author


* Fri Oct 19 2009 Olivier Faurax <olivier.faurax@laposte.net> 20090727-1neo2009.1
- Initial package

