#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		toml
Summary:	Python Library for Tom's Obvious, Minimal Language
Summary(pl.UTF-8):	Pythonowa biblioteka do formatu TOML (Tom's Obvious, Minimal Language)
Name:		python-%{module}
Version:	0.10.2
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/toml/
Source0:	https://files.pythonhosted.org/packages/source/t/toml/%{module}-%{version}.tar.gz
# Source0-md5:	59bce5d8d67e858735ec3f399ec90253
URL:		https://github.com/uiri/toml
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python library for parsing and creating TOML.

%description -l pl.UTF-8
Pythonowa biblioteka do analizy i tworzenia plików TOML.

%package -n python3-%{module}
Summary:	Python Library for Tom's Obvious, Minimal Language
Summary(pl.UTF-8):	Pythonowa biblioteka do formatu TOML (Tom's Obvious, Minimal Language)
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
A Python library for parsing and creating TOML.

%description -n python3-%{module} -l pl.UTF-8
Pythonowa biblioteka do analizy i tworzenia plików TOML.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
# disable test_{valid,invalid}_tests: no toml-test/tests/{valid,invalid} data
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests -k 'not (test_invalid_tests or test_valid_tests)'
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
# disable test_{valid,invalid}_tests: no toml-test/tests/{valid,invalid} data
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests -k 'not (test_invalid_tests or test_valid_tests)'
%endif
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
%doc LICENSE README.rst test.toml
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst test.toml
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
