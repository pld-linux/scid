Summary:	Chess database
Summary(pl.UTF-8):	Szachowa baza danych
Name:		scid
Version:	3.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/scid/%{name}-%{version}.tar.gz
# Source0-md5:	3c9483a7990a2629a35a787c1c29eee0
URL:		http://scid.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scid (for "Shane's Chess Information Database" is a free chess
database application for Unix and Microsoft Windows operating systems.

Scid converts to and from PGN (Portable Game Notation) format, which
is the standard for text-based chess information exchange, but uses
its own fast compact format for storing files.

%description -l pl.UTF-8
Scid (od "Shane's Chess Information Database" - bazy danych informacji
szachowych Shane'a) to wolnodostępna aplikacja szachowej bazy danych
dla systemów operacyjnych Unix oraz Microsoft Windows.

Scid konwertuje do i z formatu PGN (Portable Game Notation - przenośna
notacja gry), który jest standardem wymiany tekstowych informacji
szachowych, ale używa własnego, szybkiego formatu do przechowywania
plików.

%prep
%setup -q

%{__perl} -pi -e 's@/usr/X11R6/lib@/usr/X11R6/%{_lib}@' configure

%build
# it's not autoconf configure
./configure \
	COMPILE="%{__cxx}" \
	LINK="%{__cxx}" \
	OPTIMIZE="%{rpmcflags} -fno-rtti -fno-exceptions" \
	BINDIR=%{_bindir} \
	SHAREDIR=%{_datadir}/scid

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README THANKS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
