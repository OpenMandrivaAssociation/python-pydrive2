Name:		python-pydrive2
Version:	1.21.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pydrive2/pydrive2-%{version}.tar.gz
Summary:	Google Drive API made easy. Maintained fork of PyDrive.
URL:		https://pypi.org/project/pydrive2/
License:	Apache License 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Google Drive API made easy. Maintained fork of PyDrive.

%files
%{py_sitedir}/pydrive2
%{py_sitedir}/PyDrive2-*.*-info
