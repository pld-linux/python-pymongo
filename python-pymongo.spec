#
# Conditional build:
%bcond_without	python2	# Python 2.x module
%bcond_without	python3	# Python 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (TestSrvPooling requires network)

%define 	module	pymongo
Summary:	Python driver for MongoDB
Summary(pl.UTF-8):	Sterownik Pythona do MongoDB
Name:		python-%{module}
# keep 3.x here for python2 support
Version:	3.13.0
Release:	2
License:	Apache v2.0
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/p/pymongo/pymongo-%{version}.tar.gz
# Source0-md5:	3965b85631b7d482c78a38ae028f4f0a
URL:		https://api.mongodb.com/python/current/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-bson = %{version}-%{release}
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PyMongo distribution contains tools for interacting with MongoDB
database from Python.

%description -l pl.UTF-8
Dystrybucja PyMongo zawiera narzędzia do współpracy z bazą danych
MongoDB z poziomu Pythona.

%package -n python-bson
Summary:	Python bson library
Summary(pl.UTF-8):	Biblioteka bson dla Pythona
Group:		Development/Languages/Python
Conflicts:	python-pymongo < 3.7.1

%description -n python-bson
BSON is a binary-encoded serialization of JSON-like documents. BSON is
designed to be lightweight, traversable, and efficient. BSON, like
JSON, supports the embedding of objects and arrays within other
objects and arrays.

%description -n python-bson -l pl.UTF-8
BSON to binarna serializacja dokumentów w stylu JSON. BSON jest
zaprojektowany jako lekki, dający się przechodzić i wydajny. BSON,
podobnie jak JSON, obsługuje osadzanie obiektów i tablic wewnątrz
innych obiektów i tablic.

%package -n python-gridfs
Summary:	Python GridFS driver for MongoDB
Summary(pl.UTF-8):	Pythonowy sterownik GridFS dla MongoDB
Group:		Development/Languages/Python
Requires:	python-pymongo = %{version}-%{release}

%description -n python-gridfs
GridFS is a storage specification for large objects in MongoDB.

%description -n python-gridfs -l pl.UTF-8
GridFS to specyfikacja przechowywania danych dużych obiektów w
MongoDB.

%package -n python3-%{module}
Summary:	Python driver for MongoDB
Summary(pl.UTF-8):	Sterownik Pythona do MongoDB
Group:		Development/Languages/Python
Requires:	python3-bson = %{version}-%{release}
Requires:	python3-modules >= 1:3.5

%description -n python3-%{module}
The PyMongo distribution contains tools for interacting with MongoDB
database from Python.

%description -n python3-%{module} -l pl.UTF-8
Dystrybucja PyMongo zawiera narzędzia do współpracy z bazą danych
MongoDB z poziomu Pythona.

%package -n python3-bson
Summary:	Python bson library
Summary(pl.UTF-8):	Biblioteka bson dla Pythona
Group:		Development/Languages/Python
Conflicts:	python3-pymongo < 3.7.1

%description -n python3-bson
BSON is a binary-encoded serialization of JSON-like documents. BSON is
designed to be lightweight, traversable, and efficient. BSON, like
JSON, supports the embedding of objects and arrays within other
objects and arrays.

%description -n python3-bson -l pl.UTF-8
BSON to binarna serializacja dokumentów w stylu JSON. BSON jest
zaprojektowany jako lekki, dający się przechodzić i wydajny. BSON,
podobnie jak JSON, obsługuje osadzanie obiektów i tablic wewnątrz
innych obiektów i tablic.

%package -n python3-gridfs
Summary:	Python GridFS driver for MongoDB
Summary(pl.UTF-8):	Pythonowy sterownik GridFS dla MongoDB
Group:		Development/Languages/Python
Requires:	python-pymongo = %{version}-%{release}

%description -n python3-gridfs
GridFS is a storage specification for large objects in MongoDB.

%description -n python3-gridfs -l pl.UTF-8
GridFS to specyfikacja przechowywania danych dużych obiektów w
MongoDB.

%package apidocs
Summary:	API documentation for Python MongoDB modules
Summary(pl.UTF-8):	Dokumentacja API modułów Pythona MongoDB
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for Python MongoDB modules.

%description apidocs -l pl.UTF-8
Dokumentacja API modułów Pythona MongoDB.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
sphinx-build-2 -b html doc doc/_build/html
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
%doc README.rst THIRD-PARTY-NOTICES
%dir %{py_sitedir}/pymongo
%{py_sitedir}/pymongo/*.py[co]
%attr(755,root,root) %{py_sitedir}/pymongo/_cmessage.so
%{py_sitedir}/pymongo-%{version}-py*.egg-info

%files -n python-bson
%defattr(644,root,root,755)
%dir %{py_sitedir}/bson
%{py_sitedir}/bson/*.py[co]
%attr(755,root,root) %{py_sitedir}/bson/_cbson.so

%files -n python-gridfs
%defattr(644,root,root,755)
%dir %{py_sitedir}/gridfs
%{py_sitedir}/gridfs/*.py[co]
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst THIRD-PARTY-NOTICES
%dir %{py3_sitedir}/pymongo
%{py3_sitedir}/pymongo/*.py
%{py3_sitedir}/pymongo/__pycache__
%attr(755,root,root) %{py3_sitedir}/pymongo/_cmessage.*.so
%{py3_sitedir}/pymongo-%{version}-py*.egg-info

%files -n python3-bson
%defattr(644,root,root,755)
%dir %{py3_sitedir}/bson
%{py3_sitedir}/bson/*.py
%{py3_sitedir}/bson/__pycache__
%attr(755,root,root) %{py3_sitedir}/bson/_cbson.*.so

%files -n python3-gridfs
%defattr(644,root,root,755)
%dir %{py3_sitedir}/gridfs
%{py3_sitedir}/gridfs/*.py
%{py3_sitedir}/gridfs/__pycache__
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_images,_static,api,developer,examples,*.html,*.js}
%endif
