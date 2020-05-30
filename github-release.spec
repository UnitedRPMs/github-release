%global debug_package %{nil}

%global commit0 a2845f06c59c7a3ff01a7c1971f17ef6ca060451
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           github-release
Version:        0.8.1
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

* Sat May 30 2020 David Va <davidva AT tuta DOT io> 0.8.1-2.gita2845f0
- Updated to current commit

* Sat May 02 2020 David Va <davidva AT tuta DOT io> 0.8.1-1.gitc4d67c5
- Updated to 0.8.1

* Fri May 01 2020 David Va <davidva AT tuta DOT io> 0.8.0-1.git5663bb0
- Updated to 0.8.0

* Mon Oct 29 2018 David Va <davidva AT tuta DOT io> 0.7.2-2.gitb61ce1a
- Updated to current commit

* Wed Nov 15 2017 David Vasquez <davidjeremias82 at gmail dot com> 0.7.2-1.git744a70e
- Initial build rpm
