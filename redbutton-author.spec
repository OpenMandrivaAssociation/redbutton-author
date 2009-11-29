Name:           redbutton-author
Version:        20090727
Release:        %mkrel 1
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
* Sun Nov 29 2009 Olivier Faurax <olivier.faurax@laposte.net> 20090727-1mdv2009.1
- Initial package

