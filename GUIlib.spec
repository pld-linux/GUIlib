Summary:	Simple GUI framework for use with SDL
Summary(pl):	Prosty szkielet GUI do u¿ywania z SDL
Name:		GUIlib
Version:	1.1.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.libsdl.org/projects/GUIlib/src/%{name}-%{version}.tar.gz
# Source0-md5:	9d5d88cdb42dd8611e31f5e3f8a3084e
URL:		http://www.libsdl.org/projects/GUIlib/
BuildRequires:	SDL-devel >= 1.0.1
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple GUI framework, for use with SDL. It is very
flexible, but is by no means a complete windowing system. It contains
a C++ GUI class with a very rudimentary C interface, and a set of
useful widget classes.

%description -l pl
To jest bardzo prosty szkielet GUI (graficznego interfejsu
u¿ytkownika) do u¿ywania z SDL. Jest bardzo elastyczny, ale w ¿aden
sposób nie jest pe³nym systemem okienkowym. Zawiera klasê GUI w C++
z bardzo podstawowym interfejsem w C oraz zestaw przydatnych klas
widgetów.

%package devel
Summary:	GUIlib header files
Summary(pl):	Pliki nag³ówkowe GUIlib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
GUIlib header files.

%description devel -l pl
Pliki nag³ówkowe GUIlib.

%package static
Summary:	GUIlib static library
Summary(pl):	Statyczna biblioteka GUIlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
GUIlib static library.

%description static -l pl
Statyczna biblioteka GUIlib.

%prep
%setup -q

# remove old libtool.m4 from acinclude.m4
head -165 acinclude.m4 > acinclude.tmp
mv -f acinclude.tmp acinclude.m4

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
%doc CHANGES README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/GUI
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
