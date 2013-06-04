#
# Conditional build:
%bcond_with	tests	# run tests (seem broken)

%define 	module	pymongo
Summary:	Python driver for MongoDB
Summary(pl.UTF-8):	Sterownik Pythona do MongoDB
Name:		python-%{module}
Version:	2.5.2
Release:	1
License:	Apache v2.0
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/pymongo/%{module}-%{version}.tar.gz
# Source0-md5:	d1ada91f0ec474534eab88429fb6ce5e
URL:		http://api.mongodb.org/python/current/
BuildRequires:	python-devel
BuildRequires:	python-distribute
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

%prep
%setup -q -n %{module}-%{version}

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build

%{?with_tests:%{__python} setup.py test}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

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
