%define repo gnome312

Name:           russianfedora-%{repo}-release
Version:        20
Release:        1.R
Summary:        Russian Fedora (%{repo}) Repository Configuration

Group:          System Environment/Base
License:        BSD
URL:            http://russianfedora.pro
Source0:	russianfedora-%{repo}-x86_64.repo
Source1:        russianfedora-%{repo}-i386.repo

Requires:       system-release >= %{version}

%description
This repository contain addons to rhughes GNOME 3.12 repositories

%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install
# Create dirs
install -d -m755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# Yum .repo files
%ifarch x86_64
%{__install} -p -m644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/russianfedora-%{repo}.repo
%else
%{__install} -p -m644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/russianfedora-%{repo}.repo
%endif

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*


%changelog
* Thu Apr  3 2014 Arkady L. Shane <ashejn@russianfedora.ru> - 20-1.R
- initial build
