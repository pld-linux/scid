Summary:	Chess database
Summary(pl):	Szachowa baza danych
Name:		scid
Version:	3.5
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	0748b222ec1c06a5a1764e6515e04e70
URL:		http://scid.sourceforge.net/index.html
BuildRequires:	tcl-devel
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chess database

%description -l pl
Szachowa baza danych

%prep
%setup -q

%build
%configure \
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
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
