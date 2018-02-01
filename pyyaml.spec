%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')


%define name		PyYAML
%define release     	pslq_gcc_huge
%define version		3.12
%define _topdir		/home/pqueiroz/pacotes/pyyaml
%define buildroot	%{_topdir}/%{name}-%{version}-root

BuildRoot:	%{buildroot}
Summary:        PSLQ Compilation of PyYAML
Name:           %{name}
License:	APL
Version:        %{version}
Release:        %{release}
Source:         PyYAML-3.12.tar.gz
Prefix:         /opt/oss-mldl
Group:          Development/Tools
Autoreq:	0 
Requires:	Python = 3.6.4-pslq_gcc_huge
Requires:	yaml-cpp >= 0.5.1




 
%description
PSLQ Compilation of six on top of Advance Toolchain and IBM mathematical Libraries
For more information about this package, please check: https://github.com/pslq/tools

WARNING:
  This package have been made for educational purposes, there is no support of anykind implicit on it
  For a supported solution it's advisable to look for either the distrivution packages or IBM's Advance Toolchain

%prep
%setup -q
 
 
%build
F77FLAGS="%{fla}" CFLAGS="%{fla}" CXXFLAGS="%{fla}" FCFLAGS="%{fla}" CPPFLAGS="-I/opt/oss-mldl/include " LDFLAGS="%{lb_flags}" LIBS="%{lb_list}" /opt/oss-mldl/bin/python3 setup.py build

%install
rm -rf %{buildroot}
install -d %{buildroot}
/opt/oss-mldl/bin/python3 setup.py install --root %{buildroot}

 
%files
/opt/oss-mldl/*
