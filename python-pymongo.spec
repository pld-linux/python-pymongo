#
# Conditional build:
%bcond_without  python2         # Python 2.x module
%bcond_without  python3         # Python 3.x module
%bcond_with	tests	# run tests (seem broken)

%define 	module	pymongo
Summary:	Python driver for MongoDB
Summary(pl.UTF-8):	Sterownik Pythona do MongoDB
Name:		python-%{module}
Version:	2.7.1
Release:	3
License:	Apache v2.0
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/p/pymongo/pymongo-%{version}.tar.gz
# Source0-md5:	4e4c75e5362f422edb47d27ea6d17a96
URL:		http://api.mongodb.org/python/current/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-distribute
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-distribute
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-libs
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PyMongo distribution contains tools for interacting with MongoDB
database from Python. The bson package is an implementation of the
BSON format for Python. The pymongo package is a native Python driver
for MongoDB. The gridfs package is a gridfs implementation on top of
pymongo.

%description -l pl.UTF-8
Dystrybucja PyMongo zawiera narzędzia do współpracy z bazą danych
MongoDB z poziomu Pythona. Pakiet bson to implementacja formatu BSON
dla Pythona. Pakiet pymongo to natywny sterownik Pythona dla MongoDB.
Pakiet gridfs to implementacja gridfs w oparciu o pymongo.

%package -n python3-%{module}
Summary:	Python driver for MongoDB
Summary(pl.UTF-8):	Sterownik Pythona do MongoDB
Group:		Development/Languages/Python
Requires:	python3-libs
Requires:	python3-modules

%description -n python3-%{module}
The PyMongo distribution contains tools for interacting with MongoDB
database from Python. The bson package is an implementation of the
BSON format for Python. The pymongo package is a native Python driver
for MongoDB. The gridfs package is a gridfs implementation on top of
pymongo.

%description -n python3-%{module} -l pl.UTF-8
Dystrybucja PyMongo zawiera narzędzia do współpracy z bazą danych
MongoDB z poziomu Pythona. Pakiet bson to implementacja formatu BSON
dla Pythona. Pakiet pymongo to natywny sterownik Pythona dla MongoDB.
Pakiet gridfs to implementacja gridfs w oparciu o pymongo.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst doc/api doc/examples doc/*.rst
%dir %{py_sitedir}/bson
%{py_sitedir}/bson/*.py[co]
%attr(755,root,root) %{py_sitedir}/bson/_cbson.so
%dir %{py_sitedir}/gridfs
%{py_sitedir}/gridfs/*.py[co]
%dir %{py_sitedir}/pymongo
%{py_sitedir}/pymongo/*.py[co]
%attr(755,root,root) %{py_sitedir}/pymongo/_cmessage.so
%{py_sitedir}/pymongo-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst doc/api doc/examples doc/*.rst
%dir %{py3_sitedir}/bson
%{py3_sitedir}/bson/*.py
%{py3_sitedir}/bson/__pycache__
%attr(755,root,root) %{py3_sitedir}/bson/_cbson.*.so
%dir %{py3_sitedir}/gridfs
%{py3_sitedir}/gridfs/*.py
%{py3_sitedir}/gridfs/__pycache__
%dir %{py3_sitedir}/pymongo
%{py3_sitedir}/pymongo/*.py
%{py3_sitedir}/pymongo/__pycache__
%attr(755,root,root) %{py3_sitedir}/pymongo/_cmessage.*.so
%{py3_sitedir}/pymongo-%{version}-py*.egg-info
%endif
