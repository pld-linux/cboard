# TODO:
# - make some nice desktop
# - add some icon
Summary:	An ncurses frontend to GNU Chess
Summary(pl.UTF-8):	Frontend ncurses dla GNU Chess
Name:		cboard
Version:	0.2.4
Release:	2
License:	GPL v2
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/bjk/%{name}-%{version}.tar.gz
# Source0-md5:	9ce34b2201537881a4089e53442405fe
URL:		http://arbornet.org/~bjk/cboard/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-ext-devel
Requires:	gnuchess
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CBoard is a console frontend to GNU Chess, using the ncurses library
for the interface. It can edit PGN tags, annotate moves with NAG, and
more.

%description -l pl.UTF-8
CBoard jest frontendem dla GNU Chess, używającym interfejsu biblioteki
ncurses. Potrafi modyfikować znaczniki PGN, komentować ruchy za pomocą
NAG i wiele innych.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcflags} -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog KnownBugs NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.data
%{_mandir}/man6/*.6*
