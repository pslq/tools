%global __os_install_post %{nil}
%define debug_package %{nil}
%define __os_install_post %{nil}




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
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/opt/ibm/xlf/15.1.6/bin:/opt/ibm/xlC/13.1.6/bin:/root/bin" ./compile.sh
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/opt/ibm/xlf/15.1.6/bin:/opt/ibm/xlC/13.1.6/bin:/root/bin" ./output/bazel build //scripts:bazel-complete.bash
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/opt/ibm/xlf/15.1.6/bin:/opt/ibm/xlC/13.1.6/bin:/root/bin" ./output/bazel shutdown
echo 'export PATH="/opt/oss-mldl/bin:${PATH}"' > profile.sh

 
%install
install -d -o root -g root -m 0755 %{buildroot}/opt/oss-mldl/bin %{buildroot}/etc/profile.d
cp output/bazel  %{buildroot}/opt/oss-mldl/bin
install -o root -g root -m 555 profile.sh %{buildroot}/etc/profile.d/bazel-pslq.sh

%files
%attr(0755,root,root)  /opt/oss-mldl/bin/bazel
%attr(0755,root,root)  /etc/profile.d/bazel-pslq.sh
