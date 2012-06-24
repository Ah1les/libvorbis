Summary:	The Vorbis General Audio Compression Codec
Summary(pl):	Kodek kompresji audio - Vorbis
Summary(pt_BR):	Biblioteca libvorbis
Summary(ru):	����� �������� ���������� Vorbis
Summary(uk):	����� ������ϧ ������Ӧ� Vorbis
Name:		libvorbis
Version:	1.0
Release:	6
Epoch:		1
License:	BSD
Group:		Libraries
Source0:	http://www.xiph.org/ogg/vorbis/download/%{name}-%{version}.tar.gz
# Source0-md5: d1ad94fe8e240269c790e18992171e53
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-make.patch
Patch2:		%{name}-testfix.patch
URL:		http://www.xiph.org/ogg/
%requires_eq	libogg
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gcc >= 5:3.0
BuildRequires:	libtool
BuildRequires:	libogg-devel >= 2:%{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libvorbis0

%description
Ogg Vorbis is a fully open, non-proprietary, patent-and-royalty-free,
general-purpose compressed audio format for audio and music at fixed
and variable bitrates from 16 to 128 kbps/channel.

%description -l pl
Ogg Vorbis jest ca�kowicie otwartym, nie b�d�cym niczyj� w�asno�ci�,
wolnym od patent�w, og�lnego przeznaczenia kodekiem audio i muzyki o
sta�ej i zmiennej bitrate od 16 do 128 kbps/kana�.

%description -l ru
Ogg Vorbis - ��� ��������� ��������, ��������� �� �������� � ���������
���������� ������ ������ ����������� � ������������� � ������������
��������� �� 16 �� 128 ������� � ������� �� �����.

%description -l uk
Ogg Vorbis - �� ���Φ��� צ�������, צ����� צ� �����Ԧ� �� ����������
צ��������� ������ �������������� ��Ħ� � Ʀ�������� �� �ͦ����
¦������� צ� 16 �� 128 ˦��¦� � ������� �� �����.

%description -l pt_BR
Ogg Vorbis e' um formato de �udio aberto de prop�sito geral,
n�o-propriet�rio e isento de patentes e royalties, para �udio e musica
de alta qualidade (44.1-48.0kHz, 16+ bit, polifonico) com bitrate fixo
ou vari�vel de 16 a 128 kbps/canal. Isso coloca Vorbis na mesma
categoria de MPEG-1 audio layer 3, MPEG-3 audio (AAC e TwinVQ) e PAQ.

%package devel
Summary:	Development files for OGG Vorbis library
Summary(pl):	Pliki nag��wkowe i dokumentacja developerska
Summary(pt_BR):	Bibliotecas para desenvolvimento com o vorbis
Summary(ru):	���������� Vorbis - ����������
Summary(uk):	��̦����� Vorbis - ��������
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}
Requires:	libogg-devel
Obsoletes:	libvorbis0-devel

%description devel
The libvorbis-devel package contains the header files and
documentation needed to develop applications with libvorbis.

%description devel -l pl
Pliki nag��wkowe i dokumentacja developerska potrzebna do rozwijania
aplikacji korzystaj�cych z biblioteki libvorbis.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para desenvolvimento com o codec
Vorbis.

%description devel -l ru
����� libvorbis-devel �������� ����� ���������� � ������������ ���
���������� �������� � libvorbis.

%description devel -l uk
����� libvorbis-devel ͦ����� ����� �������˦� �� ���������æ� ���
�������� ������� � libvorbis.

%package static
Summary:	Static development library for OGG Vorbis
Summary(es):	Bibliotecas est�ticas
Summary(pl):	Biblioteka statyczna OGG Vorbis
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com o vorbis
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}

%description static
The libvorbis-static package contains the static libraries of
libvorbis.

%description static -l pl
Biblioteka statyczna OGG Vorbis.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com o codec Vorbis.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

rm -f doc/Makefile* doc/*/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README COPYING
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/vorbis
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
