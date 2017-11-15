%global commit0 744a70ee16ff8e6be45bfabb8b233d7f1e058a2b
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           github-release
Version:        0.7.2
Release:    	1%{?gver}%{dist}
Summary:        Small commandline app that allows you to easily create and delete releases of your projects on Github

Group:          Development/Tools
License:        MIT
URL:            https://github.com/aktau/github-release
Source:         https://github.com/aktau/github-release/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:	golang

%description
A small commandline app written in Go that allows you to easily create and 
delete releases of your projects on Github. In addition it allows you to 
attach files to those releases.

%prep
%autosetup -n %{name}-%{commit0}

%build
make

%install
  install -dm755 %{buildroot}/%{_bindir}
  install -Dm755 %{name} \
    %{buildroot}/%{_bindir}/%{name}


%files
%license LICENSE
%{_bindir}/%{name}


%changelog

* Wed Nov 15 2017 David Vasquez <davidjeremias82 at gmail dot com> 0.7.2-1.git744a70e
- Initial build rpm