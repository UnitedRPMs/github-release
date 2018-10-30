%global debug_package %{nil}

%global commit0 b61ce1a1426379d208f188311954fde680ac99f0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           github-release
Version:        0.7.2
Release:    	2%{?gver}%{dist}
Summary:        Small commandline app that allows you to easily create and delete releases of your projects on Github

Group:          Development/Tools
License:        MIT
URL:            https://github.com/aktau/github-release
Source:         https://github.com/aktau/github-release/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:	golang
BuildRequires:	git

%description
A small commandline app written in Go that allows you to easily create and 
delete releases of your projects on Github. In addition it allows you to 
attach files to those releases.

%prep
%autosetup -n %{name}-%{commit0}

%build
export GOPATH=$PWD/.gopath
make

%install
  install -dm755 %{buildroot}/%{_bindir}
  install -Dm755 %{name} \
    %{buildroot}/%{_bindir}/%{name}


%files
%license LICENSE
%{_bindir}/%{name}


%changelog

* Mon Oct 29 2018 David Va <davidva AT tuta DOT io> 0.7.2-2.gitb61ce1a
- Updated to current commit

* Wed Nov 15 2017 David Vasquez <davidjeremias82 at gmail dot com> 0.7.2-1.git744a70e
- Initial build rpm
