%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')


# This is a sample spec file for bazel

%define name		bazel
%define release     	pslq
%define version		0.9.0
%define _topdir		/home/pqueiroz/pacotes/bazel
%define buildroot	%{_topdir}/%{name}-%{version}-root
 
BuildRoot:	%{buildroot}
Summary:        PSLQ bazel
License:        APL
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source:         bazel-0.9.0-dist.zip
Prefix:         /opt/oss-mldl
Group:          Development/Tools
Requires:	java-1.8.0-openjdk >= 1.8.0.131



 
%description
PSLQ Compilation of bazel

%prep
%setup -q -c -n %{name}-%{version}
 
 
%build
./compile.sh
./output/bazel build //scripts:bazel-complete.bash
./output/bazel shutdown
echo 'export PATH="/opt/oss-mldl/bin:${PATH}"' > profile.sh

 
%install
install -d -o root -g root -m 0755 %{buildroot}/opt/oss-mldl/bin %{buildroot}/etc/profile.d
install -o root -g root -m 0755 output/bazel  %{buildroot}/opt/oss-mldl/bin
install -o root -g root -m 555 profile.sh %{buildroot}/etc/profile.d/bazel-pslq.sh

%files
/opt/oss-mldl/bin/*
/etc/profile.d/bazel-pslq.sh
