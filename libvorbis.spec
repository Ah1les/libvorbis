Summary:	The Vorbis General Audio Compression Codec
Summary(pl):	Kodek kompresji audio - Vorbis
Summary(pt_BR):	Biblioteca libvorbis
Summary(ru):	����� �������� ���������� Vorbis
Summary(uk):	����� ������ϧ ������Ӧ� Vorbis
Name:		libvorbis
Version:	1.1.0
Release:	1
Epoch:		1
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.gz
# Source0-md5:	bb764aeabde613d1a424a29b1f15e7e6
Patch0:		%{name}-ac_fixes.patch
Patch1:		%{name}-make.patch
URL:		http://www.vorbis.com/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gcc >= 5:3.0
BuildRequires:	libtool
BuildRequires:	libogg-devel >= 2:1.0
Requires:	libogg >= 2:1.0
Obsoletes:	libvorbis0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libogg-devel >= 2:1.0
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
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

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

mv -f $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} devel-docs

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc devel-docs/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/vorbis
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
