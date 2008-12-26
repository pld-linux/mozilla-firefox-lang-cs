%define		_lang		cs
Summary:	Czech resources for Firefox
Summary(pl.UTF-8):	Czeskie pliki językowe dla Firefoksa
Name:		mozilla-firefox-lang-%{_lang}
Version:	3.0.5
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/%{_lang}.xpi
# Source0-md5:	e26efec3e8dace92f26226eaed4735af
URL:		http://www.mozilla.org/
BuildRequires:	unzip
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_firefoxdir	%{_datadir}/mozilla-firefox
%define		_chromedir	%{_firefoxdir}/chrome

%description
Czech resources for Firefox.

%description -l pl.UTF-8
Czeskie pliki językowe dla Firefoksa.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_firefoxdir}/defaults/profile}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/* $RPM_BUILD_ROOT%{_chromedir}
sed -e 's@chrome/%{_lang}\.jar@%{_lang}.jar@' $RPM_BUILD_ROOT%{_libdir}/chrome.manifest \
	> $RPM_BUILD_ROOT%{_chromedir}/%{_lang}.manifest
mv -f $RPM_BUILD_ROOT%{_libdir}/*.rdf $RPM_BUILD_ROOT%{_firefoxdir}/defaults/profile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_lang}.jar
%{_chromedir}/%{_lang}.manifest
# file conflict:
#%{_firefoxdir}/defaults/profile/*.rdf
