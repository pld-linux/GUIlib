Summary:	Simple GUI framework for use with SDL
Summary(pl.UTF-8):	Prosty szkielet GUI do używania z SDL
Name:		GUIlib
Version:	1.2.1
Release:	1
License:	Public Domain
Group:		Libraries
Source0:	http://www.libsdl.org/projects/GUIlib/src/%{name}-%{version}.tar.gz
# Source0-md5:	a0114b925d79d6c66161e24cbeaa88b1
URL:		http://www.libsdl.org/projects/GUIlib/
BuildRequires:	SDL-devel >= 1.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple GUI framework, for use with SDL. It is very
flexible, but is by no means a complete windowing system. It contains
a C++ GUI class with a very rudimentary C interface, and a set of
useful widget classes.

%description -l pl.UTF-8
To jest bardzo prosty szkielet GUI (graficznego interfejsu
użytkownika) do używania z SDL. Jest bardzo elastyczny, ale w żaden
sposób nie jest pełnym systemem okienkowym. Zawiera klasę GUI w C++
z bardzo podstawowym interfejsem w C oraz zestaw przydatnych klas
widgetów.

%package devel
Summary:	GUIlib header files
Summary(pl.UTF-8):	Pliki nagłówkowe GUIlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2
Requires:	libstdc++-devel

%description devel
GUIlib header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe GUIlib.

%package static
Summary:	GUIlib static library
Summary(pl.UTF-8):	Statyczna biblioteka GUIlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GUIlib static library.

%description static -l pl.UTF-8
Statyczna biblioteka GUIlib.

%prep
%setup -q

%{__rm} acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install hello.cpp hello_C.c *.bmp keyboard.cpp okay.c \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%attr(755,root,root) %{_libdir}/libGUI-1.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libGUI-1.2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGUI.so
%{_libdir}/libGUI.la
%{_includedir}/GUI
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libGUI.a
