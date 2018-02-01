%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%define name pip
%define version 9.0.1
%define unmangled_version 9.0.1
%define unmangled_version 9.0.1
%define release 1

Summary: The PyPA recommended tool for installing Python packages.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: The pip developers <python-virtualenv@groups.google.com>
Url: https://pip.pypa.io/

%description
pip
===

The `PyPA recommended
<https://packaging.python.org/en/latest/current/>`_
tool for installing Python packages.

* `Installation <https://pip.pypa.io/en/stable/installing.html>`_
* `Documentation <https://pip.pypa.io/>`_
* `Changelog <https://pip.pypa.io/en/stable/news.html>`_
* `Github Page <https://github.com/pypa/pip>`_
* `Issue Tracking <https://github.com/pypa/pip/issues>`_
* `User mailing list <http://groups.google.com/group/python-virtualenv>`_
* `Dev mailing list <http://groups.google.com/group/pypa-dev>`_
* User IRC: #pypa on Freenode.
* Dev IRC: #pypa-dev on Freenode.


.. image:: https://img.shields.io/pypi/v/pip.svg
   :target: https://pypi.python.org/pypi/pip

.. image:: https://img.shields.io/travis/pypa/pip/master.svg
   :target: http://travis-ci.org/pypa/pip

.. image:: https://img.shields.io/appveyor/ci/pypa/pip.svg
   :target: https://ci.appveyor.com/project/pypa/pip/history

.. image:: https://readthedocs.org/projects/pip/badge/?version=stable
   :target: https://pip.pypa.io/en/stable

Code of Conduct
---------------

Everyone interacting in the pip project's codebases, issue trackers, chat
rooms, and mailing lists is expected to follow the `PyPA Code of Conduct`_.

.. _PyPA Code of Conduct: https://www.pypa.io/en/latest/code-of-conduct/


%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
